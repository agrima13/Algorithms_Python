def rotation(a,b):
    str1 = a+a
    k = 0
    count = 0
    for i in range(0,len(str1)):
        if(str1[i]==b[k]):
            count = count +1
            k = k +1
            if(count == len(b)):
                return 'true'
        else:
            continue



if __name__ == "__main__":
    a = raw_input("Enter the first string\n")
    b = raw_input("Enter the second string\n")
    result = rotation(a,b)
    if(result):
        print "First string is a rotation of the second string"
    else:
        print "First string is not a rotation of the second string"