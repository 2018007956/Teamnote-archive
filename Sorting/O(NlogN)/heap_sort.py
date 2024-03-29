# heap (Priority Queue)
def heapify(arr, idx, heap_size):
    largest = idx
    left_idx = 2 * idx + 1 # left child index
    right_idx = 2 * idx + 2 # right child index

    if left_idx < heap_size and arr[left_idx] > arr[largest]:
        largest = left_idx

    if right_idx < heap_size and arr[right_idx] > arr[largest]:
        largest = right_idx

    if largest != idx:
        arr[largest], arr[idx] = arr[idx], arr[largest] 
        heapify(arr, largest, heap_size)


def heap_sort(arr: list) -> list:
    # max heap 구성
    for i in range(len(arr)//2-1, -1, -1): # n//2-1 : 힙 자료구조에서 마지막 원소의 부모 노드 index
        heapify(arr, i, len(arr))

    # 정렬 수행
    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] # root node (largest)와 leaf node 교환
        heapify(arr, 0, i)
    return arr


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a space: ").strip()
    unsorted = [int(item) for item in user_input.split(" ")]
    print(heap_sort(unsorted))

'''
오름차순 정렬 - max heap : 부모 노드의 key가 자식 노드의 key보다 크거나 같은 완전이진트리
내림차순 정렬 - min heap : 부모 노드의 key가 자식 노드의 key보다 작거나 같은 완전이진트리
- 코드 결과는 오름차순인데, 오름차순/내림차순을 반대로 설명하는 글도 많음. 뭐가 맞는거지? 로직 파악해서 이해하기

특징
- 제자리 정렬 알고리즘 : 정렬에 사용되는 추가적인 저장공간이 매우 작음
- 불안정적인 정렬 : 같은 값일 떄 순서가 변할 수 있음
'''