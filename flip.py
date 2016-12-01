def flip(a):
    numone = 0
    numzero = 0
    len =0
    a1= 1
    b1 = 0
    while(a!=0):
        num = a%10
        if(num == 1):
            numone = numone + 1
        else:
            numzero = numzero + 1
        a = a/10
        len = len + 1
    if (numone == len - 1 and numzero == 1):
        return True,b1
    elif(numone == 1 and numzero == len - 1):
        return True,a1
    else:
        return False,a1
if __name__ == "__main__":
    a = raw_input("Enter the number\n")
    val,num = flip(int(a))
    if(val == True and num == 1):
        print "Yes we can flip 1 to make all digits 0 "
    elif(val ==True and num == 0):
        print "Yes we can flip 0 to make all digits 1"
    else:
        print "No matter whichever digit you flip, you will not get the desired string."
