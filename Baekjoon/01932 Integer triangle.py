'''
각 층의 모든 칸마다 최댓값을 저장하면서 동적 계획법으로 푸는 문제
'''

n = int(input())

triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

for i in range(n-1, 0, -1):
    subsum = [None] * i
    for j in range(i):
        subsum[j] = triangle[i-1][j] + max(triangle[i][j:j+2])

    triangle[i-1] = subsum

print(triangle[0][0])