T = int(input())

# idx : 단계, 이 문제에서는 공장의 번호
# selected: 지금까지 생산한 제품 번호 모음
# now_cost: 현재 단계까지 선택한 공장들의 비용
# idx 번 공장에서 생산할 제품을 고르는 것
def perm(idx, selected, now_cost):
    global min_cost

    # 현재 단계까지 계산한 비용 now_cost가
    # 이전에 내가 계산한 최소 비용 min_cost 보다 큰 경우, 답이 될 가능성이 없다.
    if now_cost >= min_cost:
        return

    # 종료 조건
    if idx == N:
        # 모든 공장에서 어떤 제품을 생산할 건지 선택 완료
        # 최소 값을 비교해서 구하면 된다.
        min_cost = min(now_cost, min_cost)
        return

    # 재귀 호출(다음 단계)
    # idx번 공장에서 생산할 제품을 선택
    # 선택할 수 있는 가짓 수는 최대 N개
    #0 ~ idx -1 번 공장에서 생산했던 제품은 선택 불가
    # 제품 번호 j
    for j in range(N):
        # idx 번 공장에서 j번 제품 생산
        if j not in selected:
            # j번 제품을 이전에 생산한 적 없으면 해 보자
            selected.append(j)
            # j번 제품을 idx번 공장에서 생산했으니 비용 추가
            new_cost = now_cost + arr[j][idx]
            # idx + 1번 공장으로(다음 단계), 생산한 제품 목록, 지금까지의 생산 비용
            perm(idx + 1, selected, new_cost)
            # j번 제품 생산 기록 취소
            selected.pop()

for tc in range(1, T + 1):
    # 제품 / 공장 개수
    N = int(input())

    # 생산 비용 표(2차원 배열로 주어짐)
    # arr[i][j] => i번 제품을 j번 공장에서 생산하는 비용
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 문제에서 원하는 (최소) 값
    min_cost = 15 * 100

    # 공장 순서는 고정
    # 제품 순서만 바꿔서 순열을 만들고
    # 공장에서 생산하는 제품의 생산 비용을 전부 계산해서 합친 후
    # 그 중에 최소를 구하면 된다.
    perm(0, [], 0)

    print(f'#{tc} {min_cost}')
