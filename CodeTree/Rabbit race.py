import heapq


def move_to_where(r, c, i):

    def move_right(c, d):
        return min(c+d, 2*M - (c+d))
    
    def move_down(r, d):
        return min(r+d, 2*N - (r+d))
    
    def move_to_origin(cur, d):
        return max(cur-d, 2 - (cur-d))

    '''
    가장 우선순위가 높은 칸
    '''
    d_i = ds[pid_to_idx[i]]
    move = []

    ## LR
    d = d_i % (2*M-2)

    # R
    noop = 2*(M-c)
    if d==0 or d==noop:
        move.append((r,c))
    elif d < noop:
        move.append((r, move_right(c, d)))
    else:
        move.append((r, move_to_origin(c, d-noop)))
    
    # L
    noop = 2*(c-1)
    if d==0 or d==noop:
        move.append((r,c))
    elif d < noop:
        move.append((r, move_to_origin(c, d)))
    else:
        move.append((r, move_right(c, d-noop)))

    ## UD
    d = d_i % (2*N-2)

    # D
    noop = 2*(N-r)
    if d==0 or d==noop:
        move.append((r,c))
    elif d < noop:
        move.append((move_down(r, d), c))
    else:
        move.append((move_to_origin(r, d-noop), c))
    
    # U
    noop = 2*(r-1)
    if d==0 or d==noop:
        move.append((r,c))
    elif d < noop:
        move.append((move_to_origin(r, d), c))
    else:
        move.append((move_down(r, d-noop), c))

    # print(move)

    dest = move[0]
    for mo in move[1:]:
        if sum(dest) < sum(mo):     # 행 번호 + 열 번호가 큰 칸
            dest = mo
        elif sum(dest) == sum(mo):
            dest = max(dest, mo)    # 행 번호가 큰 칸, 열 번호가 큰 칸
    
    return dest

Q = int(input())

command = list(map(int, input().split()))
assert command[0] == 100
### 경주 시작 준비
_, N, M, P, *info = command
pids, ds = info[::2], info[1::2]
pid_to_idx = dict(zip(pids, [*range(P)]))     # idx_to_pid is not necessary. use pids[idx].

scores = [0 for _ in range(P)]
accum_score = 0
rabbit_PQ = [(0, 2, (1,1), pids[p]) for p in range(P)]      # (count, r+c, (r, c), pid)
heapq.heapify(rabbit_PQ)
# print(rabbit_PQ)

for _ in range(Q-2):
    command = list(map(int, input().split()))
    if command[0] == 200:
        ### 경주 진행
        _, K, S = command
        rabbit_get_S = (0,0,0,0)    # (r+c, r, c, pid)
        for _ in range(K):
            ## 우선순위가 높은 토끼
            count, _, (r, c), i = heapq.heappop(rabbit_PQ)

            ## 토끼 이동
            dest = move_to_where(r, c, i)
            
            # 가장 우선순위가 높은 칸을 골라 그 위치로 해당 토끼를 이동시킵니다
            heapq.heappush(rabbit_PQ, (count+1, sum(dest), dest, i))
            # 나머지 P−1마리의 토끼들은 전부 r+c 만큼의 점수를 동시에 얻게 됩니다.
            accum_score += sum(dest)
            scores[pid_to_idx[i]] -= sum(dest)
            
            # S점을 추가로 받을 토끼를 tracking
            if (sum(dest), *dest, i) > rabbit_get_S:
                rabbit_get_S = (sum(dest), *dest, i)

        ## 점수 더하기
        scores[pid_to_idx[rabbit_get_S[3]]] += S

    else:
        ### 이동거리 변경
        _, pid_t, L = command
        ds[pid_to_idx[pid_t]] *= L

command = int(input())
assert command == 400
### 최고의 토끼 선정
print(max(scores) + accum_score)