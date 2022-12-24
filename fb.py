import time

def fib_while(n):
    i1 = 1; i2 = 1
    if n == 1 or n == 2:
        return 1
    elif n <= 0:
        return -1 if n != 0 else 0
    else:
        cnt = 2
        while True:
            i1, i2 = i2, i1 + i2
            cnt += 1
            if cnt == n:
                break
        return i2

def fib_recursion(n):
    if n <= 0:
        return -1 if n != 0 else 0
    return fib_recursion(n-1) + fib_recursion(n-2) if n > 2 else 1

def fib_DP(n):
    if n <= 0:
        return -1 if n != 0 else 0
    mem = [0 for _ in range(n+1)]
    mem[1] = 1
    for i in range(2, n+1):
        mem[i] = mem[i-1] + mem[i-2]
    return mem[n]

print("Num : ", end = '')
num = int(input())
start = time.time()
print("fib_while : ", fib_while(num))
print("{} sec".format(time.time()-start))
start = time.time()
print("fib_recursion : ", fib_recursion(num))
print("{} sec".format(time.time()-start))
start = time.time()
print("fib_DP : ", fib_DP(num))
print("{} sec".format(time.time()-start))