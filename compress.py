from collections import OrderedDict
import sys

def compress(a):
    lengthstr= len(a)
    d = OrderedDict()
    count = 1
    for i in range(lengthstr):

        checkchar = a[i]
        for j in range(i+1,lengthstr):
            if(a[j]==checkchar and a[j] not in d):
                count=count+1
        if(checkchar not in d):
            d[checkchar]=count


        count = 1
    newlenstr = len(d)*2
    if(lengthstr > newlenstr):
        for key,value in d.iteritems():
            sys.stdout.write (key+str(value))
    else:
        print a
if __name__ == "__main__":
    a= raw_input("Enter the string\n")
    compress(a)