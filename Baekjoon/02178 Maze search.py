from collections import deque

N, M = list(map(int, input().split()))
map = []
for _ in range(N):
    map.extend([int(elem) for elem in list(input())])

E = []
for i in range(N):
    for j in range(M):
        ind = i*M + j
        if map[ind] == 0:
            continue

        add = []
        if i!=0 and map[ind-M]==1:
            add.append((ind, ind-M))
        if i!=N-1 and map[ind+M]==1:
            add.append((ind, ind+M))
        if j!=0 and map[ind-1]==1:
            add.append((ind, ind-1))
        if j!=M-1 and map[ind+1]==1:
            add.append((ind, ind+1))
        E.extend(add)

dist = [float("inf")] * (N*M)
dist[0] = 0
queue = deque([0])
while len(queue) != 0:
    u = queue.popleft()
    for v1, v2 in E:
        if v1 == u and dist[v2] == float("inf"):
            queue.append(v2)
            dist[v2] = dist[v1] + 1

print(dist[-1]+1)