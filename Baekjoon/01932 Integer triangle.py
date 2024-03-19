'''
각 층의 모든 칸마다 최댓값을 저장하면서 동적 계획법으로 푸는 문제
'''

n = int(input())

triangle = [list(map(int, input().split())) for _ in range(n)]

### Bottom-up

for i in range(n-1, 0, -1):
    
    subsum = [None] * i
    for j in range(i):
        subsum[j] = triangle[i-1][j] + max(triangle[i][j:j+2])

    triangle[i-1] = subsum

print(triangle[0][0])


### Top-down

for i in range(1, n):

    triangle[i][0] += triangle[i-1][0]
    for j in range(1, i):
        triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    triangle[i][i] += triangle[i-1][i-1]

print(max(triangle[-1]))