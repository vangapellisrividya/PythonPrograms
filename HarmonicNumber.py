'''
    Created on Nov 16, 2021

    @author:srividya
    @Date:  16/11/2021
    @Title: HarmonicNumber

    '''
Num = int(input(" Enter a number: "))
def newharmonic(N) :
    # H1 = 1
    harmonic = 1.00
 
    # loop to apply the forumula
    for i in range(2, N + 1) :
        harmonic += 1 / i
 
    return harmonic 
print(round(newharmonic(Num),5))
