from nltk.corpus import gutenberg

emma = gutenberg.sents('austen-emma.txt')

# Okay, that's not the most readable or cleanest solution, but it was fun to write :3
sentences = [
    sentence for _, sentence in filter(
        lambda x: str(x[0]).endswith('3')
        and len(x[1]) == 4
        and x[1][1].startswith('t'),
        enumerate(emma)
    )
]

print(sentences)
