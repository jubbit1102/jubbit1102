T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # 각 배열들의 길이
    Ai = list(map(int, input().split()))  # 문제에서 주어지는 배열 1
    Bj = list(map(int, input().split()))  # 문제에서 주어지는 배열 2

    if N > M:  # 무조건 Bj가 더 긴 배열이 될 수 있도록 조작
        N, M = M, N
        Ai, Bj = Bj, Ai

    ans = -1e10  # 최대 값 담을 변수인데, 최대 값을 비교하며 갱신시키기 위해서는 초기 값이 굉~~장히 작은 수여야 함! => 그래서 -1의 10 제곱 할당시킴(헷갈려서 교안 찾아봄)
    for s in range(M - N + 1):  # s에서 시작해, Bj에서 Ai를 겹쳐보는 위치를 하나씩 옮겨가면서 탐색
        range_total = 0  # 현재 위치 s에서 배열 간 구간곱의 합을 여기에 저장
        for i in range(N):  # 마주보고 있는 구간 곱 계산을 위한 반복문
            range_total += Bj[s + i] * Ai[i]  # Bj의 s+i번째 원소와 Ai의 i번째 원소를 곱해 합산

        if range_total > ans:  # 이렇게 합친 구간 곱의 합이 최대값 ans보다 크면
            ans = range_total  # ans를 그 값으로 갱신
    print(f'#{test_case} {ans}')  # 문제에서 원하는 형식으로 답안 출력
