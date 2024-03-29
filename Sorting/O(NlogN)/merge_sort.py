# Devide and Conquer, Bottom up
from collections import deque

def merge_sort(arr):

    if len(arr) <= 1:   return arr
    
    mid = len(arr)//2
    left = deque(merge_sort(arr[:mid]))
    right = deque(merge_sort(arr[mid:]))

    merged = []
    while left and right:
        merged.append(left.popleft() if left[0]<right[0] else right.popleft()) # pop(0)은 시간복잡도가 O(n)이기 때문에 deque의 popleft 사용
    merged.extend(left)
    merged.extend(right)
    return merged

'''
특징
- 안정적인 정렬 : 같은 값이어도 정렬 후 순서가 변하지 않음
- 메모리 사용 : 원래의 리스트를 반으로 나누며 재귀호출되며 생성되는 리스트들이 함수 종료 전까지 소멸되지 않고 저장 공간 차지함
  - 임시배열 사용하지 않는 merge sort 코드 (return값 없음) : https://bblackscene21.tistory.com/8
'''

# Nested Function ver : https://github.com/TheAlgorithms/Python/blob/master/sorts/merge_sort.py 시간 조금 더 단축됨
def nested_merge_sort(collection: list) -> list:

    def merge(left: list, right: list) -> list:
        result = []
        while left and right:
            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        result.extend(left)
        result.extend(right)
        return result

    if len(collection) <= 1:
        return collection
    mid_index = len(collection) // 2
    return merge(nested_merge_sort(collection[:mid_index]), nested_merge_sort(collection[mid_index:]))


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a space: ").strip()
    unsorted = [int(item) for item in user_input.split(" ")]
    print(nested_merge_sort(unsorted))
