"""
이분 탐색을 응용하여 최솟값이나 최댓값을 찾는 문제 2
"""

N, M = list(map(int, input().split()))
trees = list(map(int, input().split()))

max_M = 2000000000
min_M = 1

while (max_M - min_M != 1):
    H = (max_M+min_M)//2
    get = 0
    for tree in trees:
        get += max(0, tree-H)
    
    if get > M:     # too many trees. increase H.
        min_M = H
    else:           # need more trees. decrease H.
        max_M = H

print(max_M)