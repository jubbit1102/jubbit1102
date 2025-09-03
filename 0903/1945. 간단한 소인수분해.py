T = int(input())

for tc in range(T):   # 습관처럼 (1, T + 1) 범위 설정해버림(실수)
    N = int(input())  # 문제로부터 숫자 N 입력받기
    dict = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}   # 구해야 하는 각각의 지수들을 딕셔너리의 값으로 할당

    for num in dict.keys():   # 딕셔너리의 키를 num이라고 하자
        while N % num == 0:   # N을 num으로 나눈 나머지가 0이 될 때까지(더이상 안 나눠질 때 까지)
            dict[num] += 1    # 그 때마다 해당 num의 값, 즉 지수는 1씩 더해준다.
            N = N // num      # N을 num으로 나누어 지수를 세면서 N의 값을 줄여 나가, 결국 나누기 종료 조건을 확인하는 역할

    print(f'#{tc+1} {dict[2]} {dict[3]} {dict[5]} {dict[7]} {dict[11]}')  # 각각의 지수들 출력