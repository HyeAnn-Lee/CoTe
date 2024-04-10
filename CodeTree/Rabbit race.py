import heapq


def who_is_prior():
    '''
    우선순위가 높은 토끼
    '''

    item = heapq.heappop(rabbit_PQ)
    return item

def move_to_where(r, c, i):

    def move_right(c, d):
        return min(c+d, 2*M - (c+d))
    
    def move_left(c, d):
        return max(c-d, 2 - (c-d))
    
    def move_down(r, d):
        return min(r+d, 2*N - (r+d))
    
    def move_up(r, d):
        return max(r-d, 2 - (r-d))

    '''
    가장 우선순위가 높은 칸
    '''
    d_i = ds[pid_to_idx[i]]
    move = []

    ## LR
    d = d_i % (2*M-2)

    # R
    if d==0 or d==2*(M-c):
        move.append((r,c))
    elif d < 2*(M-c):
        move.append((r, move_right(c, d)))
    else:
        move.append((r, move_left(c, d)))
    
    # L
    if d==0 or d==(2*c-1):
        move.append((r,c))
    elif d < 2*c-1:
        move.append((r, move_left(c, d)))
    else:
        move.append((r, move_right(c, d)))

    ## UD
    d = d_i % (2*N-2)

    # D
    if d==0 or d==2*(N-r):
        move.append((r,c))
    elif d < 2*(N-r):
        move.append((move_down(r, d), c))
    else:
        move.append((move_up(r, d), c))
    
    # U
    if d==0 or d==(2*r-1):
        move.append((r,c))
    elif d < 2*r-1:
        move.append((move_up(r, d), c))
    else:
        move.append((move_down(r, d), c))

    # print(move)

    dest = move[0]
    for mo in move[1:]:
        if sum(dest) < sum(mo):     # 행 번호 + 열 번호가 큰 칸
            dest = mo
        elif sum(dest) == sum(mo):
            if dest[0] < mo[0]:     # 행 번호가 큰 칸
                dest = mo
            elif dest[0] == mo[0]:
                if dest[1] < mo[1]:     # 열 번호가 큰 칸
                    dest = mo
    
    return dest

Q = int(input())

command = list(map(int, input().split()))
assert command[0] == 100
### 경주 시작 준비
_, N, M, P, *info = command
pids, ds = info[::2], info[1::2]
pid_to_idx = dict(zip(pids, [*range(P)]))     # idx_to_pid is not necessary. use pids[idx].

scores = [0 for _ in range(P)]
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
            item = who_is_prior()
            count, _, (r, c), i = item

            ## 토끼 이동
            dest = move_to_where(r, c, i)
            
            # 가장 우선순위가 높은 칸을 골라 그 위치로 해당 토끼를 이동시킵니다
            heapq.heappush(rabbit_PQ, (count+1, sum(dest), dest, i))
            # 나머지 P−1마리의 토끼들은 전부 r+c 만큼의 점수를 동시에 얻게 됩니다.
            for idx in range(P):
                scores[idx] += sum(dest)
            scores[pid_to_idx[i]] -= sum(dest)
            
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
print(max(scores))