T = int(input())

for t in range(1, T+1):   # 근데 input 보니까 테케 하나 뿐인데 굳이 이 코드 써야하나?
    D, A, B, F = map(int, input().split())
    # D: 두 기차 A, B의 전면부 사이 거리
    # A: 기차 A의 속력
    # B: 기차 B의 속력
    # F: 파리의 속력

    d = 0    # 파리가 이동한 거리

    tmp = D / (A+B)   # 임시변수 tmp는 기차 A, B의 충돌까지 남은 시간
    # 처음에 습관처럼 // 연산자(몫, 정수 나눗셈) 쓰는 바람에 fail.
    d = tmp * F    # tmp * 파리의 속력 => 파리가 이동한 거리가 된다.

    print(f'#{t} {d}')