
def indef(noun):
    """
    Returns the noun with the correct article.
    :param noun: A noun
    :returns: Article + noun
    """
    det = 'an' if noun[0].lower() in 'aeiou' else 'a'
    return "{det} {noun}".format(**locals())


def swap(token):
    """
    Swaps the first and last part of tokens of even length.
    :param token: A token
    :returns: The token with first and last parts swapped,
              if the length is even, else the unchanged token.
    """
    l = len(token)
    if l % 2 == 1:
        return token

    l = int(l / 2)
    return token[l:] + token[:l]


print(indef('apple'))
print(indef('pear'))

print(swap('python'))
print(swap('pythonn'))
