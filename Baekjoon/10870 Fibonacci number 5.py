'''
피보나치 수 역시 단순 for문으로도 구할 수 있지만, 학습을 위해 재귀를 써 봅시다.
'''

def fibbo(x):
    if x==0:
        return 0
    if x==1:
        return 1
    return fibbo(x-1)+fibbo(x-2)

n = int(input())

print(fibbo(n))