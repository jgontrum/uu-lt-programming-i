
def mymax(numbers):
    """
    Custom function to return the highest entry of a list.
    :param numbers: List of numbers
    :returns: Highest number in numbers
    """
    if not numbers:
        raise ValueError("This is not a list of numbers.")

    # Invariant: The first comparision should always fail.
    max_number = float("-inf")

    for i in numbers:
        max_number = i if i > max_number else max_number

    return max_number


def odd_even(numbers):
    """
    Creates a list of odd, then even numbers, based on the input.
    :param numbers: List of numbers
    :returns: List of the odd, then the even given numbers.
    """
    odds = []
    evens = []

    for i in numbers:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

    return odds + evens


def endings(token):
    """
    Creates a list of all suffixes of a string.
    :param token: A string.
    :returns: A list of all suffixes, including the input.
    """
    ret = []
    for i in range(len(token)):
        ret.append(token[i:])
    return ret


def caplist(s):
    """
    Creates a list of all capitalized suffixes of a string.
    :param s: A string.
    :returns: A list of a all possible capitalized suffixes.
    """
    ret = []
    for i in range(len(s)):
        prefix = s[:i]
        for a in s[i:]:
            prefix += a.upper()
        ret.append(prefix)
    return ret[::-1]


# Examples
print(mymax([1, 2, 3]))

print(odd_even([]))
print(odd_even([1, 2, 3, 4]))

print(endings("Turing"))
print(endings(""))

print(caplist("orange"))
print(caplist(""))
