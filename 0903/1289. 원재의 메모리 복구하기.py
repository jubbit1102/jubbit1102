T = int(input())

for x in range(1, T + 1):
    bit = list(input())

    # 현재 상태(모든 bit가 0인 상태)에서 원래 bit 값으로 돌아가야 해!
    # 원래 bit 값으로 돌아가기 위해 몇 번의 수정이 필요한지, 수정 횟수를 요구하는 문제
    # k번째 bit 값을 0(or 1)으로 수정할 시 그 뒷자리의 bit 값들도 0(or 1)로 똑같이 덮어씌워져 버린다.


    # 아무 생각 없이 처음에 string으로 받아오려고 했는데
    # str로 받으면 수정이 안 됨
    # 리스트로 받아와야 하는 거였다!

    count = 0  # 수정 횟수 카운트(문제서 요구하는 답)
    first = ['0'] * len(bit)  # 초기 상태는 모두 0으로 시작하되, 현재 메모리와 같은 길이


    for i in range(len(bit)):
        new_b = bit[i]   # <= 이거 왜 있는 코드지??? : 다시 공부하세요
        if new_b != first[i]:   # 원래 메모리의 i번째 글자와 현재 내가 바꾸고 있는 메모리의 i번째 글자가 다르면 바꾼다.
            count += 1   # bit 바꿨으니 횟수도 +1
            for j in range(i, len(bit)):
                # 반복문을 하나 더 사용 i <= j < len(bit) 일 때 j 번째 글자도 모두 변경한다.
                # j번째 비트 (i부터 len(bit)-1 까지 다 바꾸는 게 끝났으면 원래 비트와 비교)
                first[j] = new_b

        if first == bit:
            # 비교했는데 비트가 같다??? (문자열의 모양이) 뒤에는 볼 필요가 없다.
            # 반복문을 중단하고 지금까지 계산한 count를 정답으로 출력
            break

            # 파이썬은 리스트 비교도 가능
            # ["1" , "1" , "1" ] == ["1" , "1" , "1" ] 의 결과는 True
            # ["1" , "0" , "1" ] == ["1" , "1" , "1" ] 의 결과는 False

    print(f"#{x} {count}")




    # 처음에 짠 코드(다시 검토 필요)

    # for b in bit:
    #     # 이전 비트 값과 다르면 작업 한 번 필요
    #     if b != prev:
    #         count += 1
    #         prev = b  # 바뀐 비트 값으로 prev 갱신
    #
    # print(f'#{tc} {count}')