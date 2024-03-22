"""
TC1

input:
6 4
0000
1110
1000
0000
0111
0000

output: 9

-------- 

TC2

input:
2 2
01
10

output: 3

-------- 

TC3

input:
2 2
00
00

output: 3


"""

from collections import deque

N, M = list(map(int, input().split()))
map = []
for _ in range(N):
    map.extend([int(elem) for elem in list(input())])

E = []
for i in range(N):
    for j in range(M):
        ind = i*M+j
        add = []
        if map[ind] == 0:
            if i!=0 and map[ind-M]==0:
                add.append(ind-M)
            if i!=(N-1) and map[ind+M]==0:
                add.append(ind+M)
            if j!=0 and map[ind-1]==0:
                add.append(ind-1)
            if j!=(M-1) and map[ind+1]==0:
                add.append(ind+1)
        E.append(add)

# Start from (1,1)
dist1 = [float("inf")] * (N*M)
dist1[0] = 0
Q = deque([0])
while len(Q) != 0:
    u = Q.popleft()
    for v in E[u]:
        if dist1[v] == float("inf"):
            Q.append(v)
            dist1[v] = dist1[u] + 1

# Start from (N,M)
dist2 = [float("inf")] * (N*M)
dist2[-1] = 0
Q = deque([N*M-1])
while len(Q) != 0:
    u = Q.popleft()
    for v in E[u]:
        if dist2[v] == float("inf"):
            Q.append(v)
            dist2[v] = dist2[u] + 1

dist_break = N*M+1
for i in range(N):
    for j in range(M):
        ind = i*M+j
        if map[ind] == 0:
            continue
        if i!=0 and i!=(N-1) and map[ind-M]==0 and map[ind+M]==0:
            dist_break = min([dist_break, dist1[ind-M]+dist2[ind+M], dist1[ind+M]+dist2[ind-M]])
        if j!=0 and j!=(M-1) and map[ind-1]==0 and map[ind+1]==0:
            dist_break = min([dist_break, dist1[ind-1]+dist2[ind+1], dist1[ind+1]+dist2[ind-1]])
        if i==0 and j==(M-1):   # upper right corner
            dist_break = min([dist_break, dist1[ind-1]+dist2[ind+M], dist1[ind+M]+dist2[ind-1]])
        if i==(N-1) and j==0:   # lower left corner
            dist_break = min([dist_break, dist1[ind-M]+dist2[ind+1], dist1[ind+1]+dist2[ind-M]])

if dist1[-1]==float("inf") and dist_break==N*M+1:
    print(-1)
else:
    print(min(dist1[-1]+1, dist_break+3))
