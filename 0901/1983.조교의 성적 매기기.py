T = int(input())
for test_case in range(1, T + 1):  # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    N, K = map(int, input().split())  # 문제에서 학생 수(N)와 학생 번호(K) 불러오기
    scores = []  # 점수 담을 변수
    for _ in range(N):  # !!! : 처음에 리스트 컴프리헨션을 사용해서 불러오는 코드를 생각해봤는데 생각만큼 잘 안 됐고
        # GPT에서 옳게 된 사용 예를 보니까 스스로 생각하기에 잘 이해가 안 돼서 그냥 반복문을 따로 사용하기로 함

        M, F, A = map(int, input().split())  # 중간, 기말, 과제 점수 불러오기
        total_score = (M * 0.35) + (F * 0.4) + (A * 0.2)  # 점수는 문제에서 제시한 비율대로 계산(중간 35%, 기말 40%, 과제 20%)
        scores.append(total_score)  # 계산한 점수를 scores 변수에 담아주기
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']  # 학점 리스트
    # 이 부분부터 좀 헤맸음(GPT 도움도 간간히 받음)
    score_list = []  # 학생 총점과 인덱스를 새로운 리스트로 저장
    for i in range(N):  # 학생 수만큼 반복해서
        score_list.append([scores[i], i])  # 각 학생의 점수랑 인덱스 추가

    score_list.sort(reverse=True)  # 점수 정렬

    student_grade = [None] * N  # 각 학생의 학점을 담을 리스트 초기화
    per_grade = N // 10

    for i in range(N):  # 학생에게 학점 부여하는 반복문 실행
        grade_idx = i // per_grade  # i번 학생이 어느 학점 구간에 속하는지
        idx = score_list[i][1]  # 원래 학생 번호 (인덱스는 1)
        student_grade[idx] = grades[grade_idx]  # 학점이 각 학생 번호에 맞게 저장됨

    print(f"#{test_case} {student_grade[K - 1]}")  # 문제에서 요구하는 K번째 학생 학점 출력
