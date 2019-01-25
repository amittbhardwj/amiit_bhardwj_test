"""
Author : Amitt Bhardwj
"""

x1 = input("Enter first corrdinate of first line ")
x2 = input("Enter second corrdinate of first line ")
x3 = input("Enter first corrdinate of second line ")
x4 = input("Enter second corrdinate of second line ")


if (x1 - x3) == (x2 - x4):
    print('Lines Overlap') 
else:
    print('Lines Do not Overlap')
