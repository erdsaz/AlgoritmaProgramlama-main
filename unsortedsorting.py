def highest(mylist):
    for i in range(len(mylist)):
        for j in range(i+1,len(mylist)):
            if mylist[j]>mylist[i]:
                mylist[i],mylist[j]=mylist[j],mylist[i]
    return mylist[0]

  
  
  
  
  
def highest2(mylist2): 
    max=mylist2[0]
    for index in range(1,range(mylist2)):
        if mylist2[index]>max:
            max=mylist2[index]
    return max   
    

