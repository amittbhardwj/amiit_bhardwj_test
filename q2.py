"""
Author : Amitt Bhardwj
"""

"""
It comapres two strings and tell if first string is 
equeal to, greater than or less than second string.
"""
def comapare(str1,str2):
    if str1>str2:
        return (str1 + " is greater than " + str2)
    elif str1 == str2:
        return (str1 + " is equal to " + str2)
    else :
        return (str1 + " is less than " + str2)