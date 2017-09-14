import turtle

def polygon(sides, length=50):
  if sides <= 2:
    print("A polygon must have at least 3 sides.")
    return
  for _ in range(sides):
    turtle.forward(length)
    turtle.left(360 / sides)

def main():
  sides = input("To draw a polygon, please enter the number of sides: ")
  polygon(int(sides))
  input()

main()