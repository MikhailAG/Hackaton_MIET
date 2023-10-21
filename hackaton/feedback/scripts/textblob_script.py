from textblob import TextBlob
import translators as ts

def sentiment(text):
  eng = ts.translate_text(from_language='ru', to_language='en', query_text=text, translator='google')
  testimonial = TextBlob(eng)
  sent = testimonial.sentiment.polarity
  if sent <= 0:
    return 1
  if sent < 0.33:
    return 2
  return 3