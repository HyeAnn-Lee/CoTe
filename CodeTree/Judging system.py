import heapq
from collections import defaultdict


def url_to_domain_qid(url):
    return url.split('/')

def qid_to_hashlevel(qid):
    qid = int(qid)
    quot, level1 = qid // 1000, qid % 1000
    level3, level2 = quot // 1000, quot % 1000
    return level1, level2, level3

def add_to_wait(p, t, u):
    heapq.heappush(waiting_PQ, (p, t, u))
    domain, qid = url_to_domain_qid(u)

    l1, l2, l3 = qid_to_hashlevel(qid)
    waiting_hash[domain][l1][l2].append(l3)
    return


waiting_PQ = []     # (p, t, url)
heapq.heapify(waiting_PQ)

waiting_hash = defaultdict(lambda: [defaultdict(lambda: [[] for _ in range(1000)]) for _ in range(1000)])
judging_domain = set()
domain_latest = defaultdict(lambda: (0,0))  # domain : (start, gap)


Q = int(input())
for _ in range(Q):
    command = input().split()
    # print(command)

    ### 코드트리 채점기 준비
    if command[0] == '100':
        N, u0 = int(command[1]), command[2]

        idle_judger = [*range(1, N+1)]
        heapq.heapify(idle_judger)

        judging_what = [None for _ in range(N)]

        add_to_wait(1, 0, u0)

    ### 채점 요청
    elif command[0] == '200':
        t, p, u = int(command[1]), int(command[2]), command[3]

        domain, qid = url_to_domain_qid(u)

        l1, l2, l3 = qid_to_hashlevel(qid)
        if l3 in waiting_hash[domain][l1][l2]:
            continue
        
        add_to_wait(p, t, u)
    
    ### 채점 시도
    elif command[0] == '300':
        t = int(command[1])

        if len(idle_judger) == 0:
            continue

        temp = []
        while len(waiting_PQ) != 0:
            item = heapq.heappop(waiting_PQ)
            _, _, u_i = item
            domain_i, qid_i = url_to_domain_qid(u_i)
            start, gap = domain_latest[domain_i]

            if domain_i in judging_domain or t < start + 3 * gap:
                temp.append(item)

            else:
                J_id = heapq.heappop(idle_judger)
                judging_what[J_id-1] = (t, u_i)
                judging_domain.add(domain_i)

                l1, l2, l3 = qid_to_hashlevel(qid_i)
                waiting_hash[domain_i][l1][l2].remove(l3)
                break
                
        for item in temp:
            heapq.heappush(waiting_PQ, item)
                
    
    ### 채점 종료
    elif command[0] == '400':
        t, J_id = int(command[1]), int(command[2])

        if judging_what[J_id-1] is None:
            continue
        
        t_i, u_i = judging_what[J_id-1]
        domain_i, _ = url_to_domain_qid(u_i)

        judging_what[J_id-1] = None
        heapq.heappush(idle_judger, J_id)
        judging_domain.remove(domain_i)
        domain_latest[domain_i] = (t_i, t-t_i)
    
    ### 채점 대기 큐 조회
    else:
        assert command[0] == '500'
        t = int(command[1])

        print(len(waiting_PQ))
    
    # print(command, idle_judger, waiting_PQ, judging_what)