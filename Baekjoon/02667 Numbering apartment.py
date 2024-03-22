N = int(input())
map = []
for _ in range(N):
    map.extend([int(elem) for elem in list(input())])

E = []
for i in range(N):
    for j in range(N):
        idx = i*N + j
        add = []
        if map[idx] == 1:
            if i!=0 and map[idx-N] == 1:
                add.append(idx-N)
            if i!=(N-1) and map[idx+N] == 1:
                add.append(idx+N)
            if j!=0 and map[idx-1] == 1:
                add.append(idx-1)
            if j!=(N-1) and map[idx+1] == 1:
                add.append(idx+1)
        E.append(add)

not_visited = map.copy()
size = []

def explore(vertex, num):
    not_visited[vertex] = 0
    size[num] += 1
    for u in E[vertex]:
        if not_visited[u] == 1:
            explore(u, num)


while (1 in not_visited):
    v = not_visited.index(1)
    size.append(0)
    explore(v, len(size)-1)

print(len(size))
size.sort()
for i in size:
    print(i)