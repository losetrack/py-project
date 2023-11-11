# The first question
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

# The third problem
def Josephus_question_3(n):
    a = n//2
    b = a//2
    m = b+1
    l = n-2*m
    return 2*l+1


# test
print (f"circle(5): 1-{Josephus_question_1(5)}  2-{Josephus_question_2(5)}")
print (f"circle(6): 1-{Josephus_question_1(6)}  2-{Josephus_question_2(6)}")