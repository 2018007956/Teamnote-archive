import heapq

# 내림차순 정렬
def minheap(iterable):
    result = []
    heap = iterable.copy()
    heapq.heapify(heap)
    for i in range(len(heap)):
        result.append(heapq.heappop(heap))
    return result

# 오름차순 정렬
def maxheap(iterable):
    heap = []
    result = []
    for value in iterable:
        heapq.heappush(heap, -value)
    for i in range(len(heap)):
        result.append(-heapq.heappop(heap))
    return result

arr = [1,9,0,7,8,6,3,5]
print(minheap(arr))
print(maxheap(arr))
