# Hierholzer 알고리즘 : 오일러 회로(Euler circuit) 찾기
def find_euler_circuit(graph):
    # 시작점 임의 선택
    start = list(graph.keys())[0]
    stack =[start]
    result = []
    while stack:
        node = stack[-1]
        if node in graph and graph[node]:
            # 이동 가능한 노드가 있으면 이동
            next_node = graph[node].pop()
            stack.append(next_node)
        else:
            # 이동할 수 있는 노드가 없으면 결과 리스트에 추가
            result.append(stack.pop())
    
    # 결과 리스트를 역순으로 정렬하여 오일러 회로 리턴
    return result[::-1]

## 프로그래머스 43164번 여행경로 문제
# graph = {'ICN': ['JFK'], 'HND': ['IAD'], 'JFK': ['HND']}
graph = {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['SFO', 'ICN']}
print(find_euler_circuit(graph))
'''
Hierholzer 알고리즘은 오일러 회로(Euler circuit)를 찾는 알고리즘
오일러 회로란 그래프의 모든 간선을 한 번씩만 통과하는 연속된 경로
한붓그리기와 유사한데, 시작점과 도착점이 같으면 오일러 회로가 됨

Hierholzer's Algorithm :
1. 임의의 시작점을 선택하여 stack에 넣는다
2. stack에서 노드 하나를 꺼내 이 노드에 연결된 간선들 중 아직 방문하지 않은 간선을 찾는다.
   해당 간선을 따라 다음 노드로 이동한다.
3. 이동한 노드를 stack에 넣는다. 이동한 간선은 삭제한다
4. 2~3번 과정을 반복
   만약 더 이동할 간선이 없다면 해당 노드를 result 리스트에 추가
5. stack이 비어있지 않은 동안 2~4번 과정을 반복
6. result 리스트의 역순으로 정렬한 후 반환

ref) https://risingcurve.tistory.com/33
'''