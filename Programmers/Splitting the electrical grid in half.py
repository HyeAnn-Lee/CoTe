from collections import deque


def solution(n, wires):
    # 각 edge에 가상의 node를 추가하고 그 node를 root로 만들었을 때, 두 subtree의 크기를 비교
    
    answer = n
    
    for i in range(n-1):
        
        subroot1, _ = wires[i]
        wires_test = wires[:i] + wires[i+1:]
        
        """Conventional BFS approach""" 

        E = [[] for _ in range(n+1)]
        for v1, v2 in wires_test:
            E[v1].append(v2)
            E[v2].append(v1)

        subsize1 = 1
        
        visited = [False] * (n+1)
        Q = deque([subroot1])
        while len(Q) != 0:
            u = Q.popleft()
            visited[u] = True
            for neigh in E[u]:
                if visited[neigh] == False:
                    Q.append(neigh)
                    subsize1 += 1
            
        ############

        """Brand-new set approach"""

        # s = set([subroot1])
        # for _ in range(n-1):
        #     for e in wires_test:
        #         if set(e) & s:
        #             s.update(e)
        # subsize1 = len(s)

        ############
    
        diff = abs(subsize1 - (n-subsize1))
        answer = min(diff, answer)

    return answer