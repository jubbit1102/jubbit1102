# 그래프 연결 요소 개수를 구하는 문제
# 학생 번호 => 그래프의 정점 N개
# 신청서 => 간선 M개
# 같은 조 = 연결 요소 개수를 구하시오


def find_set(x):  # 집합에서 대표자 찾는 함수 정의
    if parent[x] == x:  # parent[x]가 x와 동일하면(=x 본인이 대표자면)
        return x  # 대표자인 x 반환
    return find_set(parent[x])  # x가 대표자가 아니면 부모를 따라 올라가면서 대표자 찾기


def union(a, b):  # 두 집합 a, b를 하나로 합치는 함수
    root_a = find_set(a)  # a의 대표
    root_b = find_set(b)  # b의 대표

    if root_a != root_b:  # a, b의 대표가 서로 다르면 각각 다른 집합
        parent[root_b] = root_a  # b 대표를 a로 연결해 두 집합을 합침


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 학생 수 N과 신청서 수 M을 입력받음
    applies = list(map(int, input().split()))  # 지원서 내용 입략받음
    parent = [i for i in range(N + 1)]  # 처음에는 스스로를 대표자로 두게끔 배열을 초기화 하는 코드

    for i in range(M):  # 입력받은 신청서 M개 차례대로 처리
        a, b = applies[2 * i], applies[2 * i + 1]  # applies 리스트에서 i번째 신청서 각각 1장씩 총 2장 뽑기
        union(a, b)  # a, b를 합집합 시킴

    # 각 노드의 대표를 모두 찾아 고유한 대표의 개수를 센다
    groups = set(find_set(i) for i in range(1, N + 1))  # 1번부터 N번까지 각 노드의 대표를 찾아 집합으로 만듦(set 자료구조의 특성을 이용하여 중복 제거)

    print(f'#{tc} {len(groups)}')  # 결과 출력