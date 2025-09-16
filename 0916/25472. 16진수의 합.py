T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 16진수 문자열의 길이 N
    hex_num = input()  # 16진수 문자열

    sum = 0  # 문제에서 요구하는 16진수의 합

    # 16진수 => 10진수 변환
    hex_to_dec = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }

    for i in hex_num:  # 16진수 문자열에서
        sum += hex_to_dec[i]  # hex_to_dec를 참고, 변환하여 그 값들을 sum에 합산

    print(f'#{tc} {sum}')