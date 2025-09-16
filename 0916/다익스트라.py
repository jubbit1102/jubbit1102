"""
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
"""
# V : 정점 개수
# E : 간선 개수
V, E = map(int, input().split())

# 인접행렬 / 인접리스트
# g[i] = [(i번 정점과 연결되어있는 정점번호 , 가중치), ..]
g = [[] for _ in range(V)]

for i in range(E):
    # s에서 e로 가는 간선의 가중치 w
    s, e, w = map(int, input().split())
    g[s].append((e, w))

import heapq

INF = 1e9
D = [INF] * V
# start : 시작정점
# start정점에서 시작해서 다른 모든 정점까지 가는데 최단거리를 구한다.
def dijkstra(start):
    # 힙을 사용하는 이유
    # 가중치가 가장 작은 간선을 선택 => 최소힙
    heap = []

    # 초기상태에서 시작정점 처리
    # (0 , 시작정점)
    heapq.heappush(heap, (0, start))

    # D
    # D[i] = 시작정점에서 i번 정점까지의 최단 거리
    D[start] = 0

    # 힙에 간선 정보가 남아있지 않을때까지 반복
    while heap:
        # 다음에 도착가능한 정점중에 간선의 가중치가 최소가되는 정점을 선택
        # heap에서 하나 꺼내오기만 하면 (최소가중치, 정점번호) 꺼내오기 가능
        w, v = heapq.heappop(heap)

        # if v를 이전에 선택한적이 있다면:
        #     건너뛰어라
        # v까지 가는 경로는 여러개다. heap안에 여러개 있을수 있다.
        # v입장에서 가장먼저 꺼내게 되는 간선의 가중치 w면
        # 힙안에 남아있는 다른 v까지 가는 방법, 이때 가중치 x는 w보다 무조건크다.
        if w > D[v]:
            continue

        # v를 선택, v를 거쳐서 갈 수 있는 다른 새로운 길 계산
        # 이 새로운길의 가중치가 내가 이전에 계산한 가중치보다 작으면 갱신

        # v와 인접한 정점을 조사
        # nv : v와 인접한 정점번호, nw : 그때 가중치
        for nv, nw in g[v]:
            # v 를 거쳐서 nv로 가는 새로운 길을 발견!
            # 그때의 거리 = v까지의 최단거리 + v-nv까지의 거리
            new_distance = w + nw

            # 이 새로 계산한 거리가 이전에 계산한 거리보다 작나?
            # new_distance < D[nv]
            if new_distance < D[nv]:
                D[nv] = new_distance
                # D[nv] 까지의 최단 거리가 갱신되었으므로
                # NV 까지의 최단거리를 힙에 추가
                heapq.heappush(heap, (new_distance, nv))


dijkstra(0)

print(D)
