from math import pi

def circle_area(radius):
  """
  Calculates the area of a circle with given radius.
  :param radius: the radius of the circle
  :return: area of the circle
  """
  return pi * radius**2


def triangle_area(base, height):
  """
  Calculates the area of a given triangle.
  :param base: base of triangle
  :param height: height of triangle
  :return: area of given triangle
  """
  return (base * height) / 2


def tripler(s):
  """
  Returns the tripled string
  :param s: The string that should be trippled
  :return: the trippled string
  """
  return s * 3


print("Circle area", circle_area(2))
print("Triangle area", triangle_area(2, 3))
print("Triple", tripler("baa"))

