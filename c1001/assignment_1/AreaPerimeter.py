import math

x1 = int(input("Enter value for x1: "))
y1 = int(input("Enter value for y1: "))
x2 = int(input("Enter value for x2: "))
y2 = int(input("Enter value for y2: "))

w = abs(y1 - y2)
h = abs(x1 - x2)

print(f"The perimeter of the rectangle is {round(2*w + 2*h, 2)}")

print(f"The area of the rectangle is {round(w*h, 2)}")

print(f"The length of the diagonal is {round(math.sqrt(w**2 + h**2), 2)}")
