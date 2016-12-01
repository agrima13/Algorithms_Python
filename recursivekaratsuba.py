import math


def karatsuba(x,y):

    if x <10 or y <10 :
        return x*y

    else:
       n = max(len(str(x)), len(str(y)))
       half = n/2

       a = x // math.pow(10,half)
       b = x % math.pow(10,half)
       c = y // math.pow(10,half)
       d = y % math.pow(10,half)

       #p1 = karatsuba(a,c)
       #p2 = karatsuba(b,d)
       #p3 = karatsuba(a+b,c+d)

       p1 = a * c
       p2 = b * d
       p3 = (a+b)*(c+d)



       return math.pow(10,(half*2))*p1 + math.pow(10,half)*(p3 - (p1+p2)) + p2




if __name__ == '__main__':
    x = int(raw_input("Enter the first number\n"))
    y = int(raw_input("Enter the second number\n"))

    answer = karatsuba(x,y)
    print answer