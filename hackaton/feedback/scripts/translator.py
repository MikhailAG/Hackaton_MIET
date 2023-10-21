import translators as ts
def translate_to_russian(text):
  return ts.translate_text(from_language='ru', to_language='en', query_text=text, translator='google')