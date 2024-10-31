# 모든 정점을 포함하고 사이클이 없는 트리의 최소 가중치 합 (MST) 구하기
import sys
input = sys.stdin.readline
def kruskal():
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return
        
        if rank[a] == rank[b]:
            parent[b] = a
            rank[a] += 1
        elif rank[a] > rank[b]:
            parent[b] = a
        else:
            parent[a] = b

    parent = [i for i in range(N+1)]
    rank = [0] * (N+1)
    res = 0
    for a, b, w in graph:
        if find(a) != find(b):
            union(a, b)
            res += w

    print(res)
    

N = int(input())
M = int(input())
graph = []
for _ in range(M):
    a, b, w = map(int, input().split())
    graph.append((a, b, w))

graph.sort(key=lambda x: x[2])
kruskal()
'''
Input
6
9
1 2 5
1 3 4
2 3 2
2 4 7
3 4 6
3 5 11
4 5 3
4 6 8
5 6 8

Output
23

Ref) boj 1922 - https://www.acmicpc.net/problem/1922
'''