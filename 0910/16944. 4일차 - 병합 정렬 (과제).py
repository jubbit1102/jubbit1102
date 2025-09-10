
def merge_sort(left, right):

    # 재귀 호출로 쪼개기
    # 이를 위해서는
    # 1. 종료 조건과 (더이상 분할이 불가능 할 때까지)
    if left == right -1:
        # 길이가 1이면 분할 불가능(왜냐면 요소가 하나뿐이란 뜻이니까)
        return left, right


    # 2. 재귀 호출 필요
    # 두 부분으로 나누고 합칠 때 정렬
    # 두 부분으로 나누는 기준 : 가운데 위치(mid)
    mid = (left + right) // 2

    # 왼쪽 범위 정렬해
    left_s, left_e = merge_sort(left, mid)
    # 오른쪽 범위 정렬해
    right_s, right_e = merge_sort(mid, right)

    # 합치면 된다.
    merge(left_s, left_e, right_s, right_e)

    # 합치고 나면 정렬 완료
    return left, right

# 주어진 범위(왼쪽, 오른쪽)의 리스트를 합치는 함수
def merge(left_s, left_e, right_s, right_e):
    global cnt  # wjsdur qustn tjsdj

    # 왼쪽 범위의 제일 작은 원소의 인덱스
    l = left_s
    # 오른쪽 점위의 제일 작은 원소의 인덱스
    r = right_s

    # 결과로 만들어 낼 배열의 길이
    gil2 = right_e - left_s

    result = [0] * gil2

    # result의 위치를 가리키는 인덱스
    idx = 0

    # 정렬(합치기) 시작
    # 왼쪽에서 가장 작은 것, 오른쪽에서 가장 작은 것
    # 둘 중 더 작은 것 선택해서 result의 idx 위치에 놓으면 된다. idx += 1


    # 1. 비교할 왼쪽, 오른쪽이 둘 다 남아있는 경우
    while l < left_e and r < right_e:
        if ai[l] < ai[r]:
            # 왼쪽과 오른쪽 중에 작은 거 놓기
            result[idx] = ai[l]
            l += 1
            idx += 1
        else:
            result[idx] = ai[r]
            r += 1
            idx += 1

    # 2. 왼쪽 부분이나 오른쪽 부분에만 남아있는 경우

    # 2-1. 오른쪽만 남아있는 경우
    while r < right_e:
        result[idx] = ai[r]
        r += 1
        idx += 1

    # 2-2. 왼쪽만 남아있는 경우
    while l < left_e:
        result[idx] = ai[l]
        l += 1
        idx += 1
    # left_e가 right_e보다 큰 거 확인하고 경우의 수 출력해야 함.
    if ai[left_e -1] > ai[right_e -1]:
        cnt += 1

    # 정렬이 완료된 범위 (left_s ~ right_e)를 원본에 반영
    for i in range(gil2):
        ai[left_s + i] = result[i]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))
    cnt = 0   # 여기서 cnt 변수 선언 하는 거 까먹음...
    merge_sort(0, N)
    print(f'#{tc} {ai[N //2]} {cnt}')    # 처음에 # 붙이는 거 까먹음