"""
    Author: Amir Reza Esmaeeil Beygi
    Date : september 4th 20203

    This code is developed to generate Fibonacci sequence. 

"""
def fibo (a:int):
    a=a-1
    if a<-1 :
        #print("number is not valid!")
        raise ValueError ("number is not valid! \nThe number is negative!")
    else :
        x_1=1
        x_2=1
        print(x_1)
        if a>-1 :
            print(x_2)
        for i in range(a):
            x_1=x_1 + x_2
            x_2=x_1 - x_2
            print(x_1)		



#	0	1	1	2	3	5	8
#		x2	x1	
#			x1	x2
