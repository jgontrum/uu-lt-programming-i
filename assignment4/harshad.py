

def digit_sum(number):
  """
  Calculates the sum of all digits
  :param number:
  :returns: sum of all digits of input number
  """
  # sum_ = 0
  # for i in str(number):
  #   sum_ += int(i)
  # return sum_

  # I'm a friend if one-liners ;)
  return sum([int(a) for a in str(number)])


def is_harshad(number):
  """
  Checks if a number is a Harshad number
  :param number: candidate to check
  :returns: true, if the given number is a Harshad number
  """
  return number % digit_sum(number) == 0

# Print all numbers from 1 to (but not including) 200:
print(list(filter(lambda x: is_harshad(x), range(1, 200))))
