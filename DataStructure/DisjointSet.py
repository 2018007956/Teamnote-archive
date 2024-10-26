import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])    
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    # 작은 트리를 큰 트리에 연결 (union by rank)
    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[b] = a
        rank[a] += 1


N, M = map(int, input().split())
parent = [i for i in range(N+1)]
rank = [0] * (N+1)
for _ in range(M):
    command, a, b = map(int, input().split())
    if command==0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
'''
분리집합(서로소집합) : 각 집합이 공통 원소를 가지지 않는 집합 A ∩ B = Ø 
분리집합의 구현과 연산 : Union-Find
    union : rank가 작은 트리를 큰 트리에 연결
    find : 루트 노드 찾기

Ref) BOJ 1717    
'''