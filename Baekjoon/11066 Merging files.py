"""
파일을 합쳐 하나로 모으는 최소 비용을 구하는 문제
"""

T = int(input())
for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))

    cost = [[0]*K for _ in range(K)]

    # File size
    for i in range(K-1):
        cost[i][i+1] = files[i] + files[i+1]
        for j in range(i+2, K):
            cost[i][j] = cost[i][j-1] + files[j]

    # Merging cost
    for i in range(2, K):
        for j in range(K-i):
            cost[j][i+j] += min([cost[j][k] + cost[k+1][i+j] for k in range(j, i+j)])

    print(cost[0][-1])