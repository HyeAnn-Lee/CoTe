n = int(input())
max_n = 40
fibo_list = [0] * (max_n+1)

count_recur = 0
count_dp = 0

def fibo_recur(n):
    global count_recur

    if n==1 or n==2:
        count_recur += 1
        return 1
    return fibo_recur(n-1) + fibo_recur(n-2)

def fibo_dp(n):
    global count_dp
    
    fibo_list[1] = fibo_list[2] = 1
    for i in range(3, n+1):
        count_dp += 1
        fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]
    return fibo_list[n]

fibo_recur(n)
fibo_dp(n)
print(count_recur, count_dp)