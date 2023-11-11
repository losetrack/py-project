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

hanoi_plus(4,"A","B","C")