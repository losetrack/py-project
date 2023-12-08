import time

def find_prime(n):
    time_start = time.time()
    number_pn = 0

    def is_prime(p):
        if p <= 1:
            return False
        if p == 2 or p == 3:
            return True
        if p % 2 == 0:
            return False
        
        def miller(p,a):
            m, k = p-1, 0
            while m % 2 == 0:
                m, k = m // 2, k+1
            y = pow(a,m,p)

            if y == 1 or y ==p-1:
                return True
            for j in range(k+1):
                y = pow(a,m*2**j,p)
                if y == p-1:
                    return True
                if y == 1:
                    return False
            return False
        
        for i in [2,3]:
            if not miller(p,i):
                return False
        return True

   
    for i in range(2,n):
        if is_prime(i):
            number_pn += 1
    
    time_end = time.time()
    return time_end - time_start, number_pn   

print(find_prime(1000000))