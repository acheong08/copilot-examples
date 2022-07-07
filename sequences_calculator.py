# Calculator for sequences
import math

# Find the nth term of the geometric sequence
def geometric_sequence(a, r, n):
    """
    Calculates the nth term of a geometric sequence
    """
    return a * (r ** n)

# Find the nth term of the arithmetic sequence
def arithmetic_sequence(a, d, n):
    """
    Calculates the nth term of an arithmetic sequence
    """
    return a + (d * n)

# Find the nth term of the fibonacci sequence
def fibonacci_sequence(n):
    """
    Calculates the nth term of a fibonacci sequence
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

# Find the nth term of the factorial sequence
def factorial_sequence(n):
    """
    Calculates the nth term of a factorial sequence
    """
    if n == 0:
        return 1
    else:
        return n * factorial_sequence(n-1)

def main():
    print("Geometric sequence:")
    a = float(input("Enter a: "))
    r = float(input("Enter r: "))
    n = int(input("Enter n: "))
    print("The", n, "term of the geometric sequence is", geometric_sequence(a, r, n))
    print("Arithmetic sequence:")
    a = float(input("Enter a: "))
    d = float(input("Enter d: "))
    n = int(input("Enter n: "))
    print("The", n, "term of the arithmetic sequence is", arithmetic_sequence(a, d, n))
    print("Fibonacci sequence:")
    n = int(input("Enter n: "))
    print("The", n, "term of the fibonacci sequence is", fibonacci_sequence(n))
    print("Factorial sequence:")
    n = int(input("Enter n: "))
    print("The", n, "term of the factorial sequence is", factorial_sequence(n))