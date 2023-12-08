import time 

def find_prime(n):
    time_start = time.time()
    number_pn = 0

    for i in range(2,n+1):
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            number_pn += 1

    time_end = time.time()
    return time_end - time_start, number_pn       

print(find_prime(1000000))