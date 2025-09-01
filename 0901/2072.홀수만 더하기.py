T = int(input())  # 테스트 케이스 개수
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for t in range(1, T + 1):
    nums = list(map(int, input().split()))  # 주어지는 10개의 수 받아와서 nums에 넣기
    sum = 0  # 문제에서 원하는 답을 위해 sum 변수 생성

    for num in nums:  # nums 안의 num을 전부 살펴보면서(반복)
        if num % 2 != 0:  # 이 num을 2로 나누었을 때의 나머지가 0이 아니라면 => 즉, 홀수라면
            sum += num  # 그 수를 sum에 합산

    print(f'#{t} {sum}')  # 문제에서 원하는 형식으로 답안을 출력