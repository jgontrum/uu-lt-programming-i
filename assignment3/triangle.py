def  triangle(a, b, c):
    """
    Prints an error, if a, b and c
    do not describe a valid triangle.
    a, b, c -- angles of the triangle
    """
    if a + b + c != 180:
        print("This is not a valid triangle.")


triangle(45, 35, 90)