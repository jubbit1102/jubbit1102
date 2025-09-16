"""
그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때,
가중치의 합이 최소가 되도록 만든 경우를 최소신장트리라고 한다.

0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때,
이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 만드시오.

[입력]
첫 줄에 테스트 케이스의 개수 T가 주어지고,
테스트 케이스 별로 첫 줄에 마지막 노드번호 V와 간선의 개수 E가 주어진다.

다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드 n1, n2, 가중치 w가 차례로 주어진다.

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
"""

# 크루스칼 / Prim 둘 다 사용해도 되지만 크루스칼 사용할 것임.
# 그게 더 익숙하니까
T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())

    # 크루스칼은 간선정보만 리스트로 저장
    edges = []

    for i in range(E):
        # s, e : 정점 번호
        # w : 가중치
        s, e, w = map(int, input().split())
        edges.append((s, e, w))

    # 가중치는 튜플의 2번 인덱스니까 2번 인덱스 원소를 기준으로 정렬
    edges.sort(key=lambda x: x[2])

    # 크루스칼은 상호배타적인 집합(유니온 파인드)를 통해 사이클의 유무 파악
    # make_set

    p = [i for i in range(V)]


# x번 정점의 대표를 찾는 연산
def find_set(x):
    if p[x] == x:
        return x

    # x의 부모한테서 다시 대표를 찾아 올라간다.
    p[x] = find_set(p[x])  # 경로 압축
    return p[x]


# x가 속한 집합과 y가 속한 집합을 합치는 연산
def union(x, y):
    king_x = find_set(x)
    king_y = find_set(y)

    # x와 y 이 두 정점이 속한 집합의 대표가 같으면
    # 하나의 MST 안에 속해 있는 거다
    # 이거를 또 추가해버리면 사이클이 생기게 된다.

    if king_x == king_y:
        return

    # 대표를 x 집합의 대표로 통일
    p[king_y] = king_x


# 내가 지금까지 선택한 간선의 개수
e_cnt = 0
# 가중치 합
min_w = 0

# 크루스칼 알고리즘은 인덱스 0번부터 차례대로 확인(이미 정렬되어 있음)
# 0번 인덱스에 있는 간선 => 가중치가 최소인 간선

for s, e, w in edges:
    # s, e 사이를 잇는 간선의 가중치가 w인데
    # s, e가 한 집합에 속해있다면. 이 간선을 추가하면 사이크링 생긴다. => MST X
    # s, e가 한 집합에 속해있지 않다면 이 간선을 추가해도 사이클이 안 생긴다. MST O
    if find_set(s) != find_set(e):
        # s랑 e가 속한 집합을 합친다.
        union(s, e)
        print(s, e, w)

        # 간선 개수 + 1
        e_cnt += 1

        # 가중치 합
        min_w += w

        # 이 간선을 추가하고 내가 지금까지 선택한 간선 개수 == V - 1이면 완성!

        if e_cnt == V - 1:
            break

print(f"#{tc} {min_w}")