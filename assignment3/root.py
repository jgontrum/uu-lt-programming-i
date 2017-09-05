from math import sqrt

def _calculate_guess(number, guess):
  return (number / guess + guess) / 2

def find_root(number, iterations=5):
  guess = number * 0.75
  for i in range(iterations):
    guess = _calculate_guess(number, guess)
    print("After iteration {} my guess is {}".format(
      i + 1, guess))    

  return guess

def main():
  number = input("Enter a number to calculate its square root: ")
  number = int(number)
  find_root(number)
  print("The correct square root is ", sqrt(number))

main()
