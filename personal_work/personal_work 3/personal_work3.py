def str2list (a:str):      #将str转换为list
    lst = []

    if "-" in a:
        for i in a[:0:-1]:
            lst.append(int(i))
        return lst
    
    else:
        for i in a[::-1]:
            lst.append(int(i))
        return lst

def add_ (str1, str2):     #正整数相加
        a,b = str2list(str1), str2list(str2)

        z = [0]*(max(len(a),len(b))+1)

        for i in range(len(z)):
            if i < len(a):
                z[i] += a[i]
            if i < len(b):
                z[i] += b[i]

        for i in range(len(z)-1):
            z[i+1] += z[i]//10
            z[i] %= 10

        if z[len(z)-1] == 0:
            del z[len(z)-1]

        result = ""
        for i in z[::-1]:
            result += str(i)
        
        return result

def sub_ (str1, str2):     #较大数减较小数
    a,b = str2list(str1), str2list(str2)
    
    z = [0]*(max(len(a),len(b)))

    for i in range(len(z)):
        if i < len(a):
            z[i] += a[i]
        if i < len(b):
            z[i] -= b[i]

    for i in range(len(z)-1):
        if z[i] < 0:
            z[i] += 10
            z[i+1] -= 1

    n, k = 1, len(z)
    while n < k:
        if z[-1] == 0:
            del z[-1]
        n += 1

    result = ""
    for i in z[::-1]:
        result += str(i)
        
    return result

def mul_ (str1, str2):     #正整数相乘
    a,b = str2list(str1), str2list(str2)
    if str1 == "0" or str2 == "0":
        return "0"

    result = ""

    def mul_single(a:list,b:int):  #一个数与个位数相乘
        lst = [0]*(len(a)+1)

        for i in range(len(a)):
            lst[i] = a[i] * b

        for i in range(len(a)-1):
            lst[i+1] += lst[i]//10
            lst[i] %= 10

        if lst[len(lst)-1] == 0:
            del lst[len(lst)-1]

        for i in lst:
            flag = False
            if i != 0:
                flag = True
                break
        if flag == False:
            return "0"

        result = ""
        for i in lst[::-1]:
            result += str(i)

        return result
    
    for i in range(len(b)):
        x = mul_single(a,b[i]) + "0"*i
        result = add_(result,x)

    return result

def is_negative (a:str):   #是否负数
    if "-" in a:
        return True
    return False

def larger (a:str, b:str): #a是否大于等于b
    a, b = str2list(a), str2list(b)
    if len(a) > len(b):
        return True
    if len(a) < len(b):
        return False
    if len(a) == len(b):
        for i in range(len(a)-1,-1,-1):
            if a[i] < b[i]:
                return False
            if a[i] > b[i]:
                return True
        return True

#加法
def add (str1,str2):
    if not is_negative(str1) and not is_negative(str2):
        return add_(str1,str2)
    
    if not is_negative(str1) and is_negative(str2):
        if larger(str1,str2):
            return sub_(str1,str2)
        
        if not larger(str1,str2):
            result = sub_(str2,str1)
            result = "-" + result
            return result
        
    if is_negative(str1) and not is_negative(str2):

        if not larger(str1,str2):
            return sub_(str2,str1)
        
        if larger(str1,str2):
            result = sub_(str1,str2)
            if result != "0":
                result = "-" + result
            return result

    if is_negative(str1) and is_negative(str2):
        result = add_(str1,str2)
        result = "-" + result
        return result


#减法
def sub (str1,str2):
    if "-" not in str2:
        a, b = str1, "-"+str2
        return add(a,b)
    else:
        return add(str1,str2[1::])


#乘法
def mul (str1,str2):
    if not is_negative(str1) and not is_negative(str2):
        return mul_(str1,str2)
    
    if is_negative(str1) and is_negative(str2):
        return mul_(str1,str2)
    
    else:
        result = mul_(str1,str2)
        return ("-" + result)
    

#除法
def div (str1,str2):
    if not larger(str1,str2):
        return ("0",str2)
    
    k = len(str1) - len(str2)
    result = []

    remainder = "0"
    y = str1[:len(str2)]
    for i in range(k+1):

        if i > 0:
            y = add(mul(remainder,"10"),str1[len(str2)+i-1])  #被减数

        for j in range(1,11):
            remainder = "0"
            x = sub(y,mul(str(j),str2))

            if x == "0":
                remainder = x
                result.append(j)
                break

            if "-" in x:
                remainder = add(x,str2)
                result.append(j-1)
                break

    n, k = 1, len(result)    #删除多余的0
    while n < k:
        if result[0] == 0:
            del result[0]
        n += 1

    result_ = ""             #转化为str
    for i in result:
        result_ += str(i)

    return result_, remainder


#乘方
def pow (str,n:int):
    k = "1"
    for i in range (n):
        k = mul(k,str) 

    return k

print(add("22222222222222","8773849905050505"))
print(sub("11111111","9877344555"))
print(sub("345676778778","222222"))
print(mul("123456","789"))
print(div("8773849905050505","123"))
print(pow("2",66))
print(add(pow("2",100),pow("3",50)))
print(sub(add(mul("2","100"),mul("123456","789")),div("8773849905050505","123")[0]))
