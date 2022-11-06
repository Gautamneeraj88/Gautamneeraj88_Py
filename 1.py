"""
1.Write a function that takes the lengths of three sides: side1, side2 and side3 of
the triangle as the input from the user using input function and return the area
and perimeter of the triangle as a tuple. Also, assert that sum of the length of any
two sides is greater than the third side.
"""
def triangle(a, b, c):
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    perimeter = 2*s
    t = (perimeter, area)
    return t

def triangle_check(a, b, c):
    if ((a+b) > c):
         print("a + b > C ", a+b, " > ", c)
    if ((a+c) > b):
        print("a + c > b ", a+c, " > ", b)
    if ((b + c) > a):
        print("b + c > a ", b+c, " > ", a)


a = float(input("Enter triangle side1: "))
b = float(input("Enter triangle side2: "))
c = float(input("Enter triangle side3: "))

print("Primeter and area of the triangle: ", triangle(a, b, c))

triangle_check(a, b, c)