from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.corpus import stopwords

# reading text
with open("labeled_clean_tweets.txt", "r") as f:
    data = f.read()
tw = data.split("\n")

# assemble tuple list
# 0: date, 1: text, 2: sentiment
tup_list = []
for i in range(0, len(tw)-3, 3):
    tup_list.append((tw[i], tw[i + 1], tw[i + 2]))

for t in tup_list:
    print(t[1])

# cleaning text
clean = []
sw = stopwords.words('english')
for t in tup_list:
    clean.append(' '.join([w.lower() for w in t[1].split() if w not in sw]))

print(clean)
