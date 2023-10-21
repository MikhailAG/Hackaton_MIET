import os, sys
import django
import re
import pymorphy2
import nltk
sys.path.append('/home/windof/hakaton/Hackaton_MIET/hackaton')
os.environ['DJANGO_SETTINGS_MODULE'] = 'hackaton.settings'
django.setup()
from feedback.models import Feedbacks
from feedback.models import Users
from feedback.scripts.textblob_script import sentiment
from feedback.scripts.translator import translate_to_english

morph = pymorphy2.MorphAnalyzer(lang='ru')
nltk.download('stopwords')
stops = nltk.corpus.stopwords.words('russian')
unique_stops = set(stops)

def get_feedback_objects(user):
    return list(Feedbacks.objects.filter(user=user))

def get_feedbacks_english(feedbacks):
    return list(map(lambda u: u.body_english if u.body_english != None else translate_to_english(u.body), feedbacks))

def get_feedbacks_russian(feedbacks):
    return list(map(lambda u: u.body, feedbacks))

def generate_feedback(user):
  feedback_objects = get_feedback_objects(user)
  reviews_russian = get_feedbacks_russian(feedback_objects)
  reviews_english = get_feedbacks_english(feedback_objects)
  single_russian = "\n".join(reviews_russian)
  single_english = "\n".join(reviews_english)
  sent = sentiment(single_english)
  adjectives = extract_adjectives_from_text(single_russian)
  if len(adjectives) < 5:
      return "Недостаточно отзывов для анализа сотрудника"
  obj = {1: 'Негативный', 2: 'Нейтральный', 3: 'Положительный'}
  feedback = f"Маркеры сотрудника: {adjectives}, средний отзыв: {obj[sent]}"
  return feedback

def extract_adjectives_from_text(text):
    phrases = []
    phrases_normalized = []
    clean_text = re.sub(r'\s+', ' ', re.sub(r'[\d\W]', ' ', text))
    words = clean_text.split()
    for i in range(len(words)):
        parsed_word = morph.parse(words[i])[0]
        normalized_word = parsed_word.normal_form
        if parsed_word.tag.POS == 'ADJF' and len(normalized_word) > 4:
            next_normalized = morph.parse(words[i+1])[0].normal_form
            phrase = f"{words[i]} {words[i+1]}"
            phrase_normalized = f"{normalized_word} {next_normalized}"
            if not phrase_normalized in phrases_normalized:
                phrases_normalized.append(phrase_normalized)
                norm_phrase = normalize_phrase(phrase)
                if norm_phrase == None:
                    continue
                phrases.append(norm_phrase)
    return ', '.join(phrases)

def normalize_phrase(phrase):
    parsed_adjective = morph.parse(phrase.split(' ')[0])[0]
    parsed_noun = morph.parse(phrase.split(' ')[1])[0]
    case = parsed_noun.tag.case
    number = parsed_noun.tag.number
    if case == None or number == None:
        return None
    transformed_adjective = parsed_adjective.inflect({case, number}).word
    return f"{transformed_adjective} {phrase.split(' ')[1]}"
