# def welcome(name):
#     print(f"Hello, {name} How are you doing today? ")
#     return
# user = input("What is your name? ")

# welcome(user)

# def add(a, b):
#     result = a + b
#     return result
# user1 = float(input("Enter a number: "))
# user2 = float(input("Enter another number: "))
# total = add(user1, user2)
# print(total)

# def get_positive_number():
#     length = float(input("Enter the length of the shape: "))

#     while length < 0:
#         print(f"Sorry!, the length can not be negative ")
#         length = float(input("Enter the length of the shape: "))
#     width = float(input("Enter the width of the shape: "))
    
#     area = length * width
#     print(f"The area is {area}")
# get_positive_number()

# Example 4

import math

# def main():
#   radius = float(input("Enter the radius of a circle: "))
#   area = circle_area(radius)
#   print(f"area: {area:.1f}")
# def circle_area(radius):
#   area = math.pi * radius * radius
#   return area
# main()


# Example 5
# import math
def main():
  # Call the arc_length function with only one argument
  # even though the arc_length function has two parameters.
  len1 = arc_length(9.7)
  print(f"len1: {len1:.1f}")
  # Call the arc_length function again but
  # this time with two arguments.
  len2 = arc_length(4.7, 270)
  print(f"len2: {len2:.1f}")
# Define a function with two parameters. The
# second parameter has a default value of 360.
def arc_length(radius, degrees=360):
  """Compute and return the length of an arc of a circle"""
  circumference = 2 * math.pi * radius
  length = circumference * degrees / 360
  return length
main()


def test_sqrt():
  assert math.sqrt(5) == approx(2.24, rel=0.01)
