import random

# Chaplin
with open("chaplin.txt") as f:
  for line in filter(lambda l: "ee" in l or "oo" in l, f):
    print(line.strip())

# Random Numbers
numbers = [
  random.randrange(1000000)
  for _ in range(1000)
]

numbers_sorted = sorted(numbers)

with open("random-numbers.txt", "w") as f:
  for n in numbers_sorted:
    f.write("%s\n" % n)

