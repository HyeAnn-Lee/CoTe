n = int(input())
max_n = 40


def fibo_recur(n):
    if n==1 or n==2:
        return 1
    return fibo_recur(n-1) + fibo_recur(n-2)

def fibo_dp(n):
    count_dp = 0
    
    fibo_list = [0] * (max_n+1)
    fibo_list[1] = fibo_list[2] = 1
    
    for i in range(3, n+1):
        count_dp += 1
        fibo_list[i] = fibo_list[i-1] + fibo_list[i-2]
    return fibo_list[n], count_dp

count_recur = fibo_recur(n)
_, count_dp = fibo_dp(n)
print(count_recur, count_dp)