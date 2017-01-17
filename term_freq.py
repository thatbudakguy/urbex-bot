#!/usr/bin/python
# *-* coding: ascii
import sys
import string
import json
from collections import Counter
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from unidecode import unidecode

def process(text, tokenizer=TweetTokenizer(), stopwords=[]):
  """Process the text of a tweet:
  - Lowercase
  - Tokenize
  - Stopword removal
  - Digits removal

  Return: list of strings
  """
  text = text.lower()
  tokens = tokenizer.tokenize(text)
  return [unidecode(tok) for tok in tokens if unidecode(tok) not in stopwords and not
          tok.isdigit()]

if __name__ == '__main__':
  fname = sys.argv[1]
  tweet_tokenizer = TweetTokenizer()
  punct = list(string.punctuation)
  stopword_list = stopwords.words('english') + punct + ['rt',
                                                        'via', '...']

  tf = Counter()
  with open(fname, 'r') as f:
    for line in f:
      tweet = json.loads(line)
      tokens = process(text=tweet['text'],
               tokenizer=tweet_tokenizer,
               stopwords=stopword_list)
      tf.update(tokens)
    for tag, count in tf.most_common(20):
      print("{}: {}".format(tag, count))
