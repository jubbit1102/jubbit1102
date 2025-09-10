# 이것저것 수정 해 보고는 있지만 테케 10개 중 절반 정도만 맞고 자꾸 Fail뜸....
# 뭐가 문제ㅇㄴ 거지...
# 수정 필요


def binary_search(arr, target):
    left = 0  # 탐색할 리스트의 시작 위치 0
    right = len(arr) - 1  # 끝 위치는 마지막 인덱스
    pre = 0  # 0: 처음, 1: 왼쪽, 2: 오른쪽 방향 선택     # 이거 빠트려서 계속 틀림(GPT 도움)
    # 탐색 시 이전 방향(pre)을 인자로 전달하여 양쪽 구간을 번갈아 선택했는지를 추적

    while left <= right:
        mid = (left + right) // 2  # 중간값 mid

        if arr[mid] == target:  # 중간 값이 차즌ㄴ 숫자 타켓이랑 같으면
            return True  # true

        # 왼쪽 구간 선택
        if pre == 2:
            # 이전에 오른쪽을 선택했다면 번갈아 선택한 것
            return True
        right = mid - 1
        pre = 1
    else:
        # 오른쪽 구간 선택
        if pre == 1:
            # 이전에 왼쪽을 선택했다면 번갈아 선택한 것
            return True
        left = mid + 1
        pre = 2

    return False  # 못 찾으면 false 반환


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # A와 B에 속한 정수의 개수 N, M
    A = list(map(int, input().split()))  # 두 줄에 걸쳐 N개와 M개의 백만 이하의 양의 정수
    B = list(map(int, input().split()))

    A.sort()  # 이진 탐색 전에 반드시 정렬해야 함

    cnt = 0  # 찾은 숫자의 개수 초기화

    for num in B:  # B리스트의 숫자 하나씩 꺼내
        if binary_search(A, num):  # A에서 num을 이진 탐색으로 찾아서
            cnt += 1  # # 찾았으면 count +1

    print(f"#{tc} {cnt}")
