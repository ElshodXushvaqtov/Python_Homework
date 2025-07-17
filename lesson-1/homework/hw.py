import math

1.
side = float(input("Enter the side of the square: "))
perimeter_square = 4 * side
area_square = side ** 2
print(f"Perimeter of square: {perimeter_square}")
print(f"Area of square: {area_square}")

2.
diameter = float(input("\nEnter the diameter of the circle: "))
circumference = math.pi * diameter
print(f"Circumference of the circle: {circumference}")

3.
a = float(input("\nEnter number a: "))
b = float(input("Enter number b: "))
mean = (a + b) / 2
print(f"Mean of a and b: {mean}")

 4.
sum_ab = a + b
product_ab = a * b
square_a = a ** 2
square_b = b ** 2

print(f"Sum: {sum_ab}")
print(f"Product: {product_ab}")
print(f"Square of a: {square_a}")
print(f"Square of b: {square_b}")
