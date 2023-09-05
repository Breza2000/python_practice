"""

    Author: Amir Reza Esmaeeil Beygi
    Date : september 4th 20203

    This code is developed to generate Fibonacci sequence.
    Unlike the oder code this one returns only the number that is requested on the sequence.
    It may be easier to work with.

    Good luck
    
"""

def fibo (a:int):
    x_1=1
    x_2=1
    if a<-1 :
        #print("number is not valid!")
        raise ValueError ("number is not valid! \nThe number is negative!")
    elif a==0 & a==1 :
        return(1)
        #print(1)
    else :
        for i in range(a):
            x_1=x_1 + x_2
            x_2=x_1 - x_2
        #print(x_2)
        return(x_2)

