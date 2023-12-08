import time 

def find_prime(n):
    time_start = time.time()
    number_pn = 0
 
    Primes = [True]*(n+1)
    p = 2
    Primes[0] = False
    Primes[1] = False
 
    while p*p <= n:
        if Primes[p] == True:
            for j in range(p*p,n+1,p):
                Primes[j] = False
        p += 1
 
    for i in range(2,n):
        if Primes[i]:
            number_pn += 1

    time_end = time.time()
    return time_end - time_start, number_pn   

print(find_prime(1000000))