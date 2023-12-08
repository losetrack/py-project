# 1.Tower of Hanoi
def hanoi_plus(n,x,y,z):
    if n == 1:
        print (f"{n}: {x}——>{y}")
        print (f"{n}: {y}——>{z}")
        return

    hanoi_plus(n-1,x,y,z)
    print (f"{n}: {x}——>{y}")
    hanoi_plus(n-1,z,y,x)
    print (f"{n}: {y}——>{z}")
    hanoi_plus(n-1,x,y,z)


# 2.The Josephus Problem
# The first problem
def Josephus_question_1(n):
    lst = list(range(1,n+1))
    k = 0
    while len(lst) != 1:
        lst_ = lst.copy()
        for i in lst_:
            k += 1
            if k % 2 == 0:
                lst.remove(i)
    return ("".join(str(i) for i in lst))
    
# The second problem
def Josephus_question_2(n):
    if n == 1:
        return 1
    elif n %2 == 1:
        return 2*Josephus_question_2((n-1)/2) + 1
    elif n % 2 == 0:
        return 2*Josephus_question_2(n/2) - 1

#The third problem
def Josephus_question_3(n):
    a = n//2
    b = a//2
    m = b+1
    l = n-2*m
    return 2*l+1


# 3.棋盘问题
def grid_cover(n: int, i: int, j: int):
    import numpy as np
    
    #创建列表
    lst = []
    for item in range(1,2**n+1):
        lst_item = [i for i in range(1,2**n+1)]
        lst.append(lst_item)
    lst[i-1][j-1] = 0

    #递归函数
    def board(n,i,j,a,b):
        half = int((2**n)/2)

        if n == 0:
            return 

        if i < a+half and j < b+half:        #特殊点在左上方
                lst[a+half-1][b+half-2] = 2
                lst[a+half-1][b+half-1] = 2
                lst[a+half-2][b+half-1] = 2
                board(n-1,i,j,a,b)
                board(n-1,a+half-1,b+half,a,b+half)     #右上
                board(n-1,a+half,b+half,a+half,b+half)  #右下 
                board(n-1,a+half,b+half-1,a+half,b)     #左下
                    
        if i < a+half and j >= b+half:       #在右上方 
                lst[a+half-2][b+half-2] =1
                lst[a+half-1][b+half-2] =1
                lst[a+half-1][b+half-1] =1
                board(n-1,i,j,a,b+half)
                board(n-1,a+half-1,b+half-1,a,b)        #左上
                board(n-1,a+half,b+half-1,a+half,b)     #左下
                board(n-1,a+half,b+half,a+half,b+half)  #右下

        if i >= a+half and j < b+half:       #在左下方
                lst[a+half-2][b+half-2] = 3
                lst[a+half-2][b+half-1] = 3
                lst[a+half-1][b+half-1] = 3
                board(n-1,i,j,a+half,b)
                board(n-1,a+half-1,b+half-1,a,b)        #左上
                board(n-1,a+half-1,b+half,a,b+half)     #右上
                board(n-1,a+half,b+half,a+half,b+half)  #右下

        if i >= a+half and j >= b+half:     #在右下方
                lst[a+half-2][b+half-2] =4
                lst[a+half-2][b+half-1] =4
                lst[a+half-1][b+half-2] =4
                board(n-1,i,j,a+half,b+half)            
                board(n-1,a+half-1,b+half-1,a,b)        #左上
                board(n-1,a+half-1,b+half,a,b+half)     #右上
                board(n-1,a+half,b+half-1,a+half,b)     #左下

    board(n,i,j,1,1)
    return (np.array(lst))