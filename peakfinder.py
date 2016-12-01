def get_numbers(num):
    #numarray = list()
    numarray = [5, 10, 15, 25, 30, 45, 65, 50, 35, 70]
    '''
    for i in range(num):
        n = raw_input("Enter the number ")
        numarray.append(int(n))
    '''
    return numarray

def peakfinder(numarray):
    for i in range(len(numarray)):
        peak = False
        pos = i
        left = pos - 1
        right = pos + 1
        if( left < 0):
            if(numarray[i] >= numarray[right]):
                peak = True
        elif(right > len(numarray)-1):
            if(numarray[i] >= numarray[left]):
                peak = True
        else:
            if(numarray[i] >= numarray[left] and numarray[i] >=numarray[right]):
                peak = True
        if(peak):
            print numarray[i], "is peek"
            break





if __name__ == '__main__':
    num = 10
    numarray=get_numbers(num)
    print numarray
    peakfinder(numarray)
