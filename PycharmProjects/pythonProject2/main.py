# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
'''r,pi = 5,3.14
V = (4/3)*pi*(r**3)
print('Volume of a sphere with radius 5 is equal to {0:.2f}'.format(V));

# 2
# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?
price = 24.95*0.6
ship_cost = 3
ship_cost_copy = 0.75
total_sum = price + ship_cost + (price + ship_cost_copy)*59
print('Total wholesale cost for 60 copies is {0:.2f}'.format(total_sum))

# 3
# If I leave my house at 6:52 am and run 1 mile at an easy pace
# (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile
# at easy pace again, what time do I get home for breakfast?
start_time = (6*60 + 52)*60
easy_time = (8*60 + 15)*2
tempo_time = (7*60 + 12)*3

breakfast_hour = (start_time + easy_time + tempo_time)/(60*60)
breakfast_int_hour = int(breakfast_hour)

breakfast_minute  = (breakfast_hour - breakfast_int_hour)*60
breakfast_int_minute = int(breakfast_minute)

print('Breakfast is at {}.{}'.format(breakfast_int_hour,breakfast_int_minute))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/'''

#Exercise 5-1
import time
days = time.time()//(3600*24)
hours = (time.time()-days*(3600*24))//3600
minutes = (time.time()-days*(3600*24) - hours*3600)//60
seconds = time.time()%60

print(str(days)+" days, "+str(hours) + "hours, "+ str(minutes) + "minutes, "+str(seconds) + "seconds")



#Exercise 5-2

def check_fermat(a,b,c,n):
    if(n>2 and (a**n+b**n)==c**n):
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn\'t work.' )

def check_fermat2():
    try:
        a = int(input('Give me a positive integer a: '))
    except ValueError:
        print('NOOOO! That was no valid number.  Try again >:|')
    b = input('Give me a positive integer b: ' )
    c = input('Give me a positive integer c: ')
    n = input('Give me a positive integer n, where n>2:  ')

    check_fermat(a,int(b),int(c),int(n))

#Exercise 5-3
def is_triangle(a,b,c):
    if(a+b>c or a+c>b or b+c>a):
        return False
    elif(a+b==c or a+c==b or a+b==c):
        print('It\'s a degenerate triangle!')
    else:
        return True


#Exercise 6-1
#8100 is the answer

#Exercise 6-2
def Ackermann(m,n):
    if(m==0):
        return n+1
    elif(m>0 and n==0):
        return Ackermann(m-1,1)
    elif(m>0 and n>0):
       return Ackermann(m-1,Ackermann(m,n-1))
    else:
        return('Wrong input, m and n must be non-negative integers!')



#Exercise 5-4
#will print 3+2+1=6
#if recurse(-1,0), then it will be a never-ending infinite loop
#"""the function recurse takes in two arguments n and s, and return s+n+n-1+....+1. However, n could only be non-negative numbers, or else the function will run infinitely

#Exercise 6-4
def is_power(a,b):
    if (a==b):
        return True
    elif(a<b):
        return False
    else:
        return is_power(a/b,b)

#Exercise 6-5
def gcd(a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

print(gcd(0,23))











