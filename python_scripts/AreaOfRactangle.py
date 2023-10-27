def rectangle_area(length, width):
  """Calculates the area of a rectangle.

  Parameters:
    length (float): Length of the rectangle.
    width (float): Width of the rectangle.

  Returns:
    float: The area of the rectangle.
  """

  return length * width

if __name__ == "__main__":
  length = float(input("Enter the length of the rectangle: "))
  width = float(input("Enter the width of the rectangle: "))

  area = rectangle_area(length, width)

  print("The area of the rectangle is: ", area)

#It will print the area of ractangle
