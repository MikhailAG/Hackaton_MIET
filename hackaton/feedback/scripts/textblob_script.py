from textblob import TextBlob
import translators as ts

def sentiment(text):
  testimonial = TextBlob(text)
  sent = testimonial.sentiment.polarity
  if sent <= 0:
    return 1
  if sent < 0.33:
    return 2
  return 3

def objectivity(text):
  testimonial = TextBlob(text)
  obj = testimonial.sentiment.subjectivity
  if obj <= 0:
    return 1
  if obj < 0.33:
    return 2
  return 3

def rating(text):
  testimonial = TextBlob(text)
  sent = testimonial.sentiment.polarity
  return "%.2f" % round((sent + 1) * 2.5, 2)