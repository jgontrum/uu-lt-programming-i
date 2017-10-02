from nltk.corpus import gutenberg
from collections import defaultdict

corpus = gutenberg.sents('carroll-alice.txt')

freq = defaultdict(int)
firstapp = {}
for i, sentence in enumerate(corpus):
  for word in sentence:
    freq[word] += 1
    firstapp.setdefault(word, i)

print(
  sorted(
    dict(
      filter(
        lambda x: x[1] >= 30 and firstapp[x[0]] >= 200,
        freq.items()
      )
    ).keys()
  )
)
