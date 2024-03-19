
'''

666 1666 2666 3666 4666 5666 6660 6661 6662 6663 ...

- 5자리수: 약 300가지
    **666 약 100가지
    *666* 약 100가지
    666** 약 100가지
- 6자리수: 약 4000가지
- 7자리수: 약 5만가지. 7자리수까지 커버해야함.

Testcases:
    (20, 10666) (50, 26665) (100, 54666) (120, 65666) (121, 66600) (130, 66609) (140, 66619) (150, 66629)
    for N=10000, answer_div_1000_quotient runs until 2666. (10000th number: 2666799)

'''

N = int(input())

answer_div_1000_quotient = 0

while N > 0:
    answer_format = answer_div_1000_quotient*1000 + 666

    ## answer의 천의 자리가 6이 아닐 경우
    if answer_div_1000_quotient % 10 != 6:

        N -= 1
        if N == 0:
            print(answer_format)
            # This outputs answers like 666, 1666, ... 5666, 7666, 8666, ...

    ## answer의 천의 자리가 6일 경우
    else:

        ## 끝에서부터 6의 개수 세기
        how_many_6s = 0
        temp1 = answer_div_1000_quotient
        while temp1%10 == 6:
            how_many_6s += 1
            temp1 //= 10
        # Here, `how_many_6s` will have either 1, 2, or 3 for N <= 10000.
        cnt = 10**how_many_6s
        # Corresponding `cnt` will be 10, 100 and 1000 for N <= 10000.

        ## 적어도 3개의 연속된 6들을 가진 새로운 포맷 만들어서 1씩 증가시키며 print
        at_least_3_6s = (answer_format//cnt) * cnt
        # Here, `at_least_3_6s` is guaranteed to have at least 3 consecutive 6s.
        for i in range(cnt):
            N -= 1
            if N == 0:
                print(at_least_3_6s + i)
                # This outputs answers like 6660, 6661, 6662, ... 6666, ... 16669, ...
                break
    
    answer_div_1000_quotient += 1
