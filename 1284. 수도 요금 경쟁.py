T = int(input())

for tc in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())

    # 한 달 수도 사용량이 W
    # A 회사 이용 시: 1리터 당 P => 즉 요금은 W * P
    # B 회사 이용 시: case 1. 사용량 R 이하라면 기본 요금 Q만 청구
    #                      case 2. 사용량 R 초과, 기본 요금 Q + (전체 사용량 중 R리터를 뺀 초과량 1 리터 당 * S) 추가요금 부과

    # 사용량 W에 대한 A / B 각 회사의 요금을 비교하여 낮은 회사 것을 출력

    a_fee = W * P  # A 회사 요금
    b_fee = 0  # B 회사 요금
    over_used = W - R  # 초과 수도 사용량

    ans = 0  # 답으로 제공할 변수

    # B 회사의 요금 계산을 위해(케이스 1 or 2 中 어느 경우에 속하는지 판별)
    if W <= R:  # 실 사용량 W가 기본 요금 보장량인 R과 같거나 작으면(이하)
        b_fee = Q  # B 회사의 요금은 기본 요금인 Q가 됨
    else:  # 그렇지 않으면( => W가 R보다 많으면)
        b_fee = Q + (over_used * S)  # 기본 요금 Q에 초과 요금 합산

    # A 회사 요금과 B 회사 요금 비교했을 때 더 작은 녀석을 고르기 위한 과정
    if a_fee < b_fee:
        ans = a_fee
    else:
        ans = b_fee

    print(f'#{tc} {ans}')  # 살림왕 진종민 완성