"""
파일을 합쳐 하나로 모으는 최소 비용을 구하는 문제
"""

T = int(input())
for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))

    cost = [[0]*K for _ in range(K)]

    for i in range(K-1):
        for j in range(K-i-1):
            cost_list = []
            for k in range(j, i+j+1):
                cost_list.append(cost[j][k]+cost[k+1][i+j+1])
            cost[j][i+j+1] = min(cost_list) + sum(files[j:i+j+2])

    print(cost[0][-1])