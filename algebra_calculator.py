# Calculator for quadratic equations
import math

def quadratic_equation(a, b, c):
    """
    Calculates the solutions to a quadratic equation
    """
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("No real solutions")
    elif discriminant == 0:
        x = -b / (2*a)
        print("One solution:", x)
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("Two solutions:", x1, x2)

def main():
    print("ax² + bx + c = 0")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    quadratic_equation(a, b, c)

if __name__ == "__main__":
    main()