# 음수 간선이 있는 그래프에서 특정 노드로부터 다른 모든 노드까지의 최단 거리 구하기
def bellman(start):
    dist[start] = 0
    for i in range(N): # 전체 n번의 라운드를 반복
        for j in range(M): # 매 반복바다 "모든 간선" 확인
            cur_n, adj_n, w = edges[j]
            if dist[cur_n] != 1e9 and dist[cur_n] + w < dist[adj_n]:
                dist[adj_n] = dist[cur_n] + w
                if i == N-1: # n번째 라운드에서도 값이 갱신된다면 음수 순환 존재
                    return True
    return False

# input : the number of nodes, edges
N, M = map(int, input().split())

edges = []
dist = [1e9] * (N+1) # shortest distance table
for _ in range(M):
    S, E, W = map(int, input().split())
    edges.append((S, E, W))

negative_cycle = bellman(1) # start node : 1
if negative_cycle:
    print('-1')
else:
    # 다른 노드까지 최단 거리 출력
    for i in range(2, N+1):
        if dist[i] == 1e9:
            print('-1')
        else:
            print(dist[i])

'''
Input
3 3
1 2 2
1 3 4
2 3 1

Output
2
3

Ref) https://www.youtube.com/watch?v=Ppimbaxm8d8
'''