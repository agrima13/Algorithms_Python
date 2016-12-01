import math


def karatsuba(x,y):

    if x < 10 and y < 10 :
        return x*y

    else:
        if x > y:
            half = math.pow(10, len(str(x))/2)
        else:
            half = math.pow(10, len(str(y))/2)



    a = x // half
    b = x % half
    c = y // half
    d = y % half

    print half

    p1 = a * c
    p2 = b * d
    p3 = (a + b) * (c+d)
    p4 = (p3 - (p1+p2))

    return math.pow(half,2)*p1 + p2 + math.pow(half,1)*p4




if __name__ == '__main__':
    x = int(raw_input("Enter the first number\n"))
    y = int(raw_input("Enter the second number\n"))

    answer = karatsuba(x,y)
    print answer