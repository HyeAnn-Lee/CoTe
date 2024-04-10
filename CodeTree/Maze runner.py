# Be aware of the index mismatch between [maze] and [people or exit].
def empty_south(r,c):
    return maze[r][c-1] == 0
def empty_north(r,c):
    return maze[r-2][c-1] == 0
def empty_east(r,c):
    return maze[r-1][c] == 0
def empty_west(r,c):
    return maze[r-1][c-2] == 0

def move_to(r, c):
    global sum_move

    sum_move += 1
    if (r,c) == exit:
        people.pop(m)
    else:
        people[m] = (r,c)
    
    return

N, M, K = list(map(int, input().split()))
maze = [list(map(int, input().split())) for _ in range(N)]
people = [tuple(map(int, input().split())) for _ in range(M)]
exit = tuple(map(int, input().split()))

sum_move = 0

for k in range(K):
    ## 1. 참가자 이동
    for m in range(len(people)-1, -1, -1):
        r,c = people[m]

        if c==exit[1]:      # 위아래 직선이동
            if r < exit[0] and empty_south(r,c):
                move_to(r+1, c)
            elif r > exit[0] and empty_north(r,c):
                move_to(r-1, c)
        elif r==exit[0]:    # 좌우 직선이동
            if c < exit[1] and empty_east(r,c):
                move_to(r, c+1)
            elif c > exit[1] and empty_west(r,c):
                move_to(r, c-1)
        
        elif r < exit[0] and empty_south(r,c):
            move_to(r+1, c)
        elif r > exit[0] and empty_north(r,c):
            move_to(r-1, c)
        elif c < exit[1] and empty_east(r,c):
            move_to(r, c+1)
        elif c > exit[1] and empty_west(r,c):
            move_to(r, c-1)
    
    ## 게임 종료
    if len(people) == 0:
        break

    ## 2. 회전

    # Find square
    rotate = (N, (N,N))
    for r,c in people:
        side = max(abs(r-exit[0]), abs(c-exit[1]))      # 예시: 2
        bottomright = (max(r, exit[0]), max(c, exit[1]))    # 예시: (3,3)
        topleft = (max(1, bottomright[0]-side), max(1, bottomright[1]-side))    # 예시: (1,1)
        rotate = min(rotate, (side, topleft))
    side, (x,y) = rotate

    # 미로 내구도 감소
    section = maze[x-1:x+side]
    temp = [row[y-1:y+side] for row in section]
    for i in range(side+1):
        for j in range(side+1):
            temp[i][j] = max(0, temp[i][j]-1)

    # 미로 회전
    temp2 = []
    for i in range(side+1):
        row = [temp[j][i] for j in range(side, -1, -1)]
        temp2.append(row)

    # 미로 업데이트
    for i in range(side+1):
        for j in range(side+1):
            maze[x-1+i][y-1+j] = temp2[i][j]

    # people, exit 회전
    for i in range(len(people)):
        r,c = people[i]
        if x <= r <= x+side and y <= c <= y+side:
            people[i] = (x+(c-y), y+(x+side-r))
    if x <= exit[0] <= x+side and y <= exit[1] <= y+side:
        exit = (x+(exit[1]-y), y+(x+side-exit[0]))

print(sum_move)
print(exit[0], exit[1])