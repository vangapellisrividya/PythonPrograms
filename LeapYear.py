'''
    Created on Nov 16, 2021

    @author:srividya
    @Date:  16/11/2021
    @Title: LeapYear

    '''
import re

input_year = int(input("Enter the Year: "))
def isvalid(input_year):
    """
    Description:
        This  will give valid digit input_year
    """
    pattern=re.compile('[1-9]?[1-9]{4}')
    return pattern.match(input_year)

if isvalid(input_year):
    print("valid year")
else:
    print("not valid year")
    year=int(input_year)
def is_leap(year):
    if (year%400 == 0) or (year %4 ==0 and year % 100 != 0):
        return True 
    return  False
if is_leap(input_year):
    print("is a leap year")
else:
    print("Not a leap year")