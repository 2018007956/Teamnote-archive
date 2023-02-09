import heapq as hq

n, m = map(int, input().split())
start = int(input())
INF = 1e8

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    # u: start node, v: end node, w: weight
    u, v, w = map(int, input().split()) 
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    hq.heappush(q, (0, start)) # (우선순위, 값)
    distance[start] = 0
    
    while q:
        dist, now = hq.heappop(q) # 우선순위가 가장 낮은 값(가장 작은 거리) 나옴

        if distance[now] < dist: # 이미 입력된 값이 현재 노드까지의 거리보다 작으면 이미 방문한 노드
            continue

        for adj in graph[now]:
            if dist+adj[1] < distance[adj[0]]:
                distance[adj[0]] = dist + adj[1]
                hq.heappush(q, (dist+adj[1], adj[0]))


dijkstra(start)
print(distance)

'''
input:
5 6
1
5 1 1
1 2 1
1 3 3
2 3 1
2 4 5
3 4 2

output:
[100000000.0, 0, 1, 2, 4, 100000000.0]

ref) https://techblog-history-younghunjo1.tistory.com/247
https://velog.io/@tks7205/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-with-python
'''