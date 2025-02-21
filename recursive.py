def func(n):
    if n==1:
        return 1 
    return n*func(n-1)

func(20)


def totalsum(list):

    if len(list)==0:
        return 0
    return list[0]+totalsum(list[1:])
