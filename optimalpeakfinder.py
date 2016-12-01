def findpeak(numarray,low,high):
    mid = (low + high) /2
    if(numarray[mid] >= numarray[mid - 1] and numarray[mid] >= numarray[mid+1]):
        return numarray[mid]
    elif (numarray[mid-1] > numarray[mid]):
        return findpeak(numarray,low,mid -1)
    elif(numarray[mid + 1] > numarray[mid]):
        return findpeak(numarray,mid+1,high)




if __name__ == '__main__':
    numarray = [5, 10, 15, 25, 30, 45, 65, 50, 35, 70]
    low = 0
    high = len(numarray)-1
    element = findpeak(numarray,low,high)
    print "Peak is",element