'''
    Created on Nov 16, 2021

    @author:srividya
    @Date:  16/11/2021
    @Title: Factors

    '''
import math

Number = int(input("Enter a Number"))
while Number % 2 == 0:
    print(2)
    Number = Number//2
    i=3
for i in range(int(math.sqrt(Number))+1,3):
    while Number%i ==0:
        print(i)
    Number = Number//i
    if Number > 2: 
        print(Number)
