"""
이분 탐색을 응용하여 최솟값이나 최댓값을 찾는 문제 2

<TC1>
2 4
5 5
will output: 3

<TC2>
5 1
2 2 2 2 2
will output: 1

"""

N, M = list(map(int, input().split()))
trees = list(map(int, input().split()))

max_M = max(trees)
min_M = 1

while True:
    H = (max_M+min_M)//2
    get = 0
    for tree in trees:
        get += max(0, tree-H)
    
    if get == M:    # found!
        break
    elif get > M:     # too many trees. increase H.
        min_M = H
    else:           # need more trees. decrease H.
        max_M = H

    if max_M - min_M <= 1:
        break

print(H)