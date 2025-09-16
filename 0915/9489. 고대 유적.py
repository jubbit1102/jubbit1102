T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]

    m_count = 0   # 가로 & 세로에서 연속되는 1의 개수 중 최대값

    for i in range(N):     # data 배열의 가로 순회(행마다)
        cnt = 0            # 구조물 카운트
        for j in range(M): # 각 열마다
            if data[i][j] == 1:   # 구조물이 있으면
                cnt += 1          # 카운트 +1

                if cnt > m_count:   # 이 때 센 구조물 개수가 기존 최대값보다 크면
                    m_count = cnt   # 그 값을 최대값으로 갱신

            else:   # data[i][j]가 1이 아니면(즉, 0이면 = 구조물이 없으면)
                cnt = 0  # 연속 끊긴 거니까 count 초기화


    for j in range(M):      # data 배열의 세로 순회(행마다)
        cnt = 0
        for i in range(N):
            if data[i][j] == 1:
                cnt += 1

                if cnt > m_count:
                    m_count = cnt

            else:
                cnt = 0


    print(f'#{tc} {m_count}')