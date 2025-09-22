'''
@ASSESSME.USERID: bm9697
@ASSESSME.AUTHOR: Borna Marić
@ASSESSME.DESCRIPTION: Assignment 3.1
@ASSESSME.ANALYZE: YES
'''


import math


def fact(n):
    if n > 0:
       return math.factorial(n)
    return 0

def root(n):
    if n < 0:
      return 0
    return math.sqrt(float(n))

def trunk(n):
   return math.trunc(n) 


def main():
    value1 = int(input("Enter a numeric value: "))
    print(value1, "Factorial =", fact(value1))

    value2 = float(input("Enter a numeric value: "))
    print("The square root of", value2, "=", root(value2))

    value3 = float(input("Enter a numeric value: "))
    print(value3, "truncated =", trunk(value3))


 


if __name__ == "__main__":
    main()