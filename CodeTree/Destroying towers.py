import heapq


def set_attacker(r, c, k):
    attack_history[coor_to_ind(r,c)] = k
    grid[r][c] += N+M
    return (r, c)

def coor_to_ind(r,c):
    return r*M+c

def ind_to_coor(ind):
    return (ind//M, ind%M)

def dijkstra(E, starting_vertex):
    dist = {vertex: float("inf") for vertex in range(N*M)}
    dist[starting_vertex] = 0

    prev = [None] * (N*M)

    p = 0
    PQ = [(0, p, starting_vertex)]  # (dist, priority, node)
    while PQ:
        d, _, u = heapq.heappop(PQ)
        for v in E[u]:
            p += 1
            if dist[v] > d+1:
                dist[v] = d+1
                prev[v] = u
                heapq.heappush(PQ, (d+1, p, v))
        
    return dist, prev


N, M, K = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]
attack_history = [0 for _ in range(N*M)]

for k in range(1, K+1):
    num_dead = sum([row.count(0) for row in grid])
    if num_dead == N*M-1:
        break

    ## 1. Select attacker
    cand = []
    min_attack = 5000
    for i in range(N):
        for j in range(M):
            attack = grid[i][j]
            if attack == 0:
                continue
            if attack < min_attack:
                min_attack = attack
                cand = [(i, j)]
            elif attack == min_attack:
                cand.append((i,j))
    
    ### 1) 공격력이 가장 낮은 포탑이 가장 약한 포탑입니다.
    if len(cand) == 1:
        ATTACKER = set_attacker(*cand[0], k)
    
    ### 2) 2개 이상이라면, 가장 최근에 공격한 포탑
    else:
        history = []
        for c in cand:
            history.append(attack_history[coor_to_ind(*c)])
        max_history = max(history)
        cand1 = []
        for i in range(len(cand)):
            if history[i] == max_history:
                cand1.append(cand[i])
        
        if len(cand1) == 1:
            ATTACKER = set_attacker(*cand1[0], k)
        
        ### 3) 2개 이상이라면, 각 포탑 위치의 행과 열의 합이 가장 큰 포탑
        else:
            sumrc = []
            for r,c in cand1:
                sumrc.append(r+c)
            max_sum = max(sumrc)
            cand2 = []
            for i in range(len(cand1)):
                if sumrc[i] == max_sum:
                    cand2.append(cand1[i])
            
            if len(cand2) == 1:
                ATTACKER = set_attacker(*cand2[0], k)
            
            ### 4) 2개 이상이라면, 각 포탑 위치의 열 값이 가장 큰 포탑
            else:
                max_c = -1
                for r,c in cand2:
                    if c > max_c:
                        max_c = c
                        ATTACKER = set_attacker(r, c, k)

    # print(ATTACKER)

    ## 2. Attack

    cand = []
    max_attack = 1
    for i in range(N):
        for j in range(M):
            attack = grid[i][j]
            if (i,j) == ATTACKER:
                continue
            if attack > max_attack:
                max_attack = attack
                cand = [(i,j)]
            elif attack == max_attack:
                cand.append((i,j))
    
    ### 1) 공격력이 가장 높은 포탑
    if len(cand) == 1:
        ATTACKEE = cand[0]

    ### 2) 2개 이상이라면, 공격한지 가장 오래된 포탑
    else:
        history = []
        for c in cand:
            history.append(attack_history[coor_to_ind(*c)])
        min_history = min(history)
        for i in range(len(history)-1, -1, -1):
            if history[i] != min_history:
                cand.pop(i)
        if len(cand) == 1:
            ATTACKEE = cand[0]

        ### 3) 2개 이상이라면, 각 포탑 위치의 행과 열의 합이 가장 작은 포탑
        else:
            sumrc = []
            for r,c in cand:
                sumrc.append(r+c)
            min_sum = min(sumrc)
            for i in range(len(sumrc)-1, -1, -1):
                if sumrc[i] != min_sum:
                    cand.pop(i)
            if len(cand) == 1:
                ATTACKEE = cand[0]

            ### 4) 2개 이상이라면, 각 포탑 위치의 열 값이 가장 작은 포탑
            else:
                min_c = M
                for r,c in cand:
                    if c < min_c:
                        min_c = c
                        ATTACKEE = (r,c)

    # print(ATTACKEE)

    E = []
    for i in range(N):
        for j in range(M):
            e = []
            if grid[i][j] != 0:
                cand = [(i, (j+1)%M), ((i+1)%N, j), (i, (j-1)%M), ((i-1)%N, j)]     ## 우 하 좌 상
                for r,c in cand:
                    e.append(coor_to_ind(r,c)) if grid[r][c] != 0 else True
            E.append(e)

    # print(E)
    
    dist, prev = dijkstra(E, coor_to_ind(*ATTACKER))
    # print(dist, prev)
    
    attack = grid[ATTACKER[0]][ATTACKER[1]]
    grid[ATTACKEE[0]][ATTACKEE[1]] -= attack

    battled = [ATTACKER, ATTACKEE]

    if dist[coor_to_ind(*ATTACKEE)] != float("inf"):
        ### 2-1. Lazer attack
        child = coor_to_ind(*ATTACKEE)
        while True:
            parent = prev[child]
            if parent == coor_to_ind(*ATTACKER):
                break
            r,c = ind_to_coor(parent)
            grid[r][c] -= attack//2
            battled.append((r,c))
            child = parent

    else:
        ### 2-2. Bomb attack
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                r = (ATTACKEE[0]+i)%N
                c = (ATTACKEE[1]+j)%M
                if (r,c) == ATTACKER or (r,c) == ATTACKEE:
                    continue
                grid[r][c] -= attack//2
                battled.append((r,c))

    ## 3. Set dead to 0
    for i in range(N):
        for j in range(M):
            grid[i][j] = 0 if grid[i][j] < 0 else grid[i][j]

    ## 4. Increase defense
    for i in range(N):
        for j in range(M):
            if grid[i][j] != 0 and (i,j) not in battled:
                grid[i][j] += 1

# print(attack_history)
# print(grid)

max_attack = 0
for row in grid:
    for tower in row:
        max_attack = max(max_attack, tower)

print(max_attack)