N = int(input())

num = -1
for i in range(N//3+1):
    if (N-3*i)%5 == 0:
        num = i + ((N-3*i)//5)
        break
print(num)