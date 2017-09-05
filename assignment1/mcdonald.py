

def printverse(animal, sound):
    print("""Old MacDonald had a farm
E-I-E-I-O
And on this farm he had a {animal}
E-I-E-I-O
With a {sound} {sound} here
With a {sound} {sound} there
Here a {sound} there a {sound}
Everywhere a {sound} {sound}
Old Mac Donald had a farm
E-I-E-I-O
""".format(animal=animal,
                    sound=sound))


def printsong():
    combinations = [
        ('cow', 'moo'),
        ('duck', 'quack'),
        ('cat', 'meow'),
        ('dog', 'woof')
    ]
    
    for animal, sound in combinations:
        printverse(animal, sound)
