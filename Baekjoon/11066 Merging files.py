"""
파일을 합쳐 하나로 모으는 최소 비용을 구하는 문제
"""

T = int(input())
for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))

    cost = [[0]*K for _ in range(K)]

    for i in range(1, K):
        for j in range(K-i):
            min_cost = float("inf")
            for k in range(j, i+j):
                min_cost = min(min_cost, cost[j][k] + cost[k+1][i+j])
            cost[j][i+j] = min_cost + sum(files[j:i+j+1])

    print(cost[0][-1])