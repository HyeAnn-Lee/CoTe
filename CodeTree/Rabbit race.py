def who_is_prior():
    '''
    우선순위가 높은 토끼
    '''

    i = pids[0]
    for pid in pids[1:]:
        if rabbit[pid][2] < rabbit[i][2]:   # 현재까지의 총 점프 횟수가 적은 토끼
            i = pid
        elif rabbit[pid][2] == rabbit[i][2]:
            if sum(rabbit[pid][1]) < sum(rabbit[i][1]):     # 현재 서있는 행 번호 + 열 번호가 작은 토끼
                i = pid
            elif sum(rabbit[pid][1]) == sum(rabbit[i][1]):
                if rabbit[pid][1][0] < rabbit[i][1][0]:     # 행 번호가 작은 토끼
                    i = pid
                elif rabbit[pid][1][0] == rabbit[i][1][0]:
                    if rabbit[pid][1][1] < rabbit[i][1][1]:     # 열 번호가 작은 토끼
                        i = pid
                    elif rabbit[pid][1][1] == rabbit[i][1][1]:
                        i = min(i, pid)         # 고유번호가 작은 토끼
    
    return i

def move_to_where():

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
    d_i, (r, c), *_ = rabbit[i]
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

def who_is_prior_to_get_S(history):
    '''
    S점을 받을 토끼
    '''
    i = history[0]
    for pid in history[1:]:
        if sum(rabbit[pid][1]) > sum(rabbit[i][1]):     # 현재 서있는 행 번호 + 열 번호가 큰 토끼
            i = pid
        elif sum(rabbit[pid][1]) == sum(rabbit[i][1]):
            if rabbit[pid][1][0] > rabbit[i][1][0]:     # 행 번호가 큰 토끼
                i = pid
            elif rabbit[pid][1][0] == rabbit[i][1][0]:
                if rabbit[pid][1][1] > rabbit[i][1][1]:     # 열 번호가 큰 토끼
                    i = pid
                elif rabbit[pid][1][1] == rabbit[i][1][1]:
                    i = max(i, pid)         # 고유번호가 큰 토끼

    return i

Q = int(input())

command = list(map(int, input().split()))
assert command[0] == 100
### 경주 시작 준비
_, N, M, P, *info = command
pids, ds = info[::2], info[1::2]
rabbit = {pids[p] : [ds[p], (1,1), 0, 0] for p in range(P)}     # pid: [d, (r,c), count, score]
# print(rabbit)

for _ in range(Q-2):
    command = list(map(int, input().split()))
    if command[0] == 200:
        ### 경주 진행
        _, K, S = command
        history = []
        for _ in range(K):
            ## 우선순위가 높은 토끼
            i = who_is_prior()
            history.append(i)

            ## 토끼 이동
            dest = move_to_where()
            for pid in pids:
                if pid==i:
                    # 가장 우선순위가 높은 칸을 골라 그 위치로 해당 토끼를 이동시킵니다
                    rabbit[pid][1] = dest
                    rabbit[pid][2] += 1
                else:
                    #  나머지 P−1마리의 토끼들은 전부 r+c 만큼의 점수를 동시에 얻게 됩니다.
                    rabbit[pid][3] += sum(dest)
            
        ## 점수 더하기
        i = who_is_prior_to_get_S(list(set(history)))
        rabbit[i][3] += S

    else:
        ### 이동거리 변경
        _, pid_t, L = command
        rabbit[pid_t][0] *= L

command = int(input())
assert command == 400
### 최고의 토끼 선정
score = 0
for pid in pids:
    score = max(score, rabbit[pid][3])
print(score)