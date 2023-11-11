def GridCover(n: int, i: int, j: int):
    import numpy as np

    lst = []
    for item in range(1,2**n+1):
        lst_item = [i for i in range(1,2**n+1)]
        lst.append(lst_item)
    lst[i-1][j-1] = 0

    def board(n,i,j,a,b):

        half = int((2**n)/2)


        if n == 0:
            return 

        if i < a+half and j < b+half:        #左上方
                lst[a+half-1][b+half-2] = 2
                lst[a+half-1][b+half-1] = 2
                lst[a+half-2][b+half-1] = 2
                board(n-1,i,j,a,b)
                board(n-1,a+half-1,b+half,a,b+half)     #右上
                board(n-1,a+half,b+half,a+half,b+half)  #右下 
                board(n-1,a+half,b+half-1,a+half,b)   #左下


                    
        if i < a+half and j >= b+half:       #右上方 
                lst[a+half-2][b+half-2] =1
                lst[a+half-1][b+half-2] =1
                lst[a+half-1][b+half-1] =1
                board(n-1,i,j,a,b+half)
                board(n-1,a+half-1,b+half-1,a,b)        #左上
                board(n-1,a+half,b+half-1,a+half,b)     #左下
                board(n-1,a+half,b+half,a+half,b+half)  #右下

                

        if i >= a+half and j < b+half:       #左下方
                lst[a+half-2][b+half-2] = 3
                lst[a+half-2][b+half-1] = 3
                lst[a+half-1][b+half-1] = 3
                board(n-1,i,j,a+half,b)
                board(n-1,a+half-1,b+half-1,a,b)        #左上
                board(n-1,a+half-1,b+half,a,b+half)     #右上
                board(n-1,a+half,b+half,a+half,b+half)  #右下



        if i >= a+half and j >= b+half:     #右下方
                lst[a+half-2][b+half-2] =4
                lst[a+half-2][b+half-1] =4
                lst[a+half-1][b+half-2] =4
                board(n-1,i,j,a+half,b+half)            
                board(n-1,a+half-1,b+half-1,a,b)        #左上
                board(n-1,a+half-1,b+half,a,b+half)     #右上
                board(n-1,a+half,b+half-1,a+half,b)     #左下

    board(n,i,j,1,1)
    return (np.array(lst))

print(GridCover(3,5,6))


    