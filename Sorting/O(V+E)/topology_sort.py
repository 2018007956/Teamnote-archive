from collections import deque

N, M = map(int, input().split())

indegree = [0] * (N+1) # 진입 차수 
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
def topology_sort():
    result = []
    queue = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        cur = queue.popleft()
        result.append(cur)

        # 인접 노드 간선 제거
        for i in graph[cur]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()

'''
위상 정렬, Topology Sort
위상 정렬은 진입 차수를 이용한 알고리즘으로,
DAG(Direct Acyclic Graph, 순환하지 않는 방향 그래프) 일 떄 가능
큐와 스택으로 구현할 수 있으며, 시간복잡도는 O(V+E)
'''