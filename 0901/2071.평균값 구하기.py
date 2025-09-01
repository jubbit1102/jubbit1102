T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in range(1, T + 1):
    nums = list(map(int, input().split()))  # 10개의 수 받아오기
    total = 0  # 평균 값 구하기 이전에 알아야 할 10개의 수의 합계를 담은 변수

    for num in nums:  # nums리스트 안의 숫자들 전부 한번씩
        total += num  # total로 합산

    average = round(total / 10)  # total을 10으로 나누고 반올림한 게 평균 / 반올림 어떻게 하는 건지 기억 안 나서 한번 찾아봄..

    print(f'#{t} {average}')  # 문제에서 원하는 형식으로 출력