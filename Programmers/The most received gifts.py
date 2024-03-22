def solution(friends, gifts):
    n_friends = len(friends)
    matrix = [[0]*n_friends for _ in range(n_friends)]
    
    name_num = dict()
    for i in range(n_friends):
        name_num[friends[i]] = i
    
    for gift in gifts:
        A, B = gift.split()
        matrix[name_num[A]][name_num[B]] += 1
    
    gift_score = [0] * n_friends
    for i in range(n_friends):
        give = sum(matrix[i])
        receive = sum([matrix[j][i] for j in range(n_friends)])
        gift_score[i] = give - receive

    next_month = [0] * n_friends
    for i in range(n_friends):
        for j in range(i+1, n_friends):
            if matrix[i][j] == matrix[j][i]:
                if gift_score[i] > gift_score[j]:
                    next_month[i] += 1
                elif gift_score[i] < gift_score[j]:
                    next_month[j] += 1
            elif matrix[i][j] > matrix[j][i]:
                next_month[i] += 1
            else:
                next_month[j] += 1
    
    return max(next_month)