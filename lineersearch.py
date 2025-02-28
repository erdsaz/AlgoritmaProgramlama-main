def lineersearch (list, target):
    for index in range(len(list)):
        if list[index]==target:
            return index
    return -1
    
    
def lineersearch2(list,target):   
    counter=0

    for item in list:
        if item == target:
            return counter
        counter+=1
    return False

result=lineersearch([],65535)

"""BINARY SEARCH MIGHT BE A QUIZ SUBJECT"""