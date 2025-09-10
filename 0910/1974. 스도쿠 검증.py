T = int(input())
for test_case in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]  # 스도쿠 배열
    result = 1  # 겹치는 숫자 유무에 따라 각 테케마다 0 or 1로 갱신해서 출력(문제에서 요구하는 답)

    for i in range(9):  # 행 검사
        check_row = [0] * 10  # 1~9 숫자 체크용 빈 리스트 생성
        for j in range(9):
            num = sudoku[i][j]  # 지금 숫자 num에 저장

            if check_row[num] == 1:  # num이 이미 체크리스트에서 1이면 이거 중복임
                result = 0  # 중복이니까 result 값 0으로 갱신하고
                break  # 중복인 거 알았으니 더 검사할 필요 x
            check_row[num] = 1  # num이 중복이었다는 거 기록해두기

        if result == 0:  # 중복 발견으로 result 값 0일 시
            break  # 더 검사할 필요 x니 break

    if result == 1:  # 앞의  행 검사 결과가 1때만 열 검사
        for i in range(9):
            check_col = [0] * 10  # 행 검사 때랑 똑같이 빈 리스트 만들어주고
            for j in range(9):
                num = sudoku[j][i]  # 확인할 숫자
                if check_col[num] == 1:  # 체크리스트에서 있다고 나타나면
                    result = 0  # 중복 처리
                    break  # 탈출
                check_col[num] = 1  # 그 숫자 중복이었다ㅏ고 기록
            if result == 0:  # 중복이니까
                break  # 탈출

    if result == 1:  # 3x3 검사도 행, 열 검사 값에 중복 없었을 때만 시작
        for box_row in range(0, 9, 3):  # 이 부분 범위 설정에 gpt 도움 받았음 : 시작 숫자: 0, 끝 숫자(미포함): 9, 증가 간격(스텝): 3
            # 스도쿠 검사에서 3x3 격자 단위로 자르기 위해 행과 열의 시작 인덱스를 0, 3, 6으로 잡아 순회하기 위해 사용합니다.
            # 예를 들어 0행~2행, 3행~5행, 6행~8행씩 구분하기 위함
            for box_col in range(0, 9, 3):  # 열도 똑같이 만들어주기
                check_box = [0] * 10  # 3x3에서의 중복 체킹을 위한 리스트
                for i in range(3):
                    for j in range(3):  # 박스 안 i, j로 각각 순회
                        num = sudoku[box_row + i][box_col + j]  # 현재 칸의 숫자 num으로 저장

                        if check_box[num] == 1:  # 이 숫자가 이미 등장한 거면
                            result = 0  # 중복 처리
                            break  # 탈출
                        check_box[num] = 1  # 숫자 처음 발견 했을 시 체크해두기

                    if result == 0:  # gpt : 3x3 내부 반복문
                        break
                if result == 0:  # 3x3 격자 반복문
                    break
            if result == 0:  # 3x3 격자 순회 반복문  각 각 중복 다 확인하고 중복일 시 각각 탈출..
                break

    print(f"#{test_case} {result}")  # 문제에서 원하는 형식으로 출력