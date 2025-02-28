def binarysearch (mylist,target):
    highest=len(mylist)-1
    lowest=0
    middle=highest//2
    while highest>lowest:
        middle=(highest+lowest)//2
        f=mylist[middle]
        if target<f:
            highest=middle
        elif target>f:
            lowest=middle
        else:
            return middle
        return -1

binarysearch(range(100),15)





