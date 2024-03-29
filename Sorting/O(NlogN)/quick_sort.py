# Devide and Conquer, Top down
# Devide and Conquer, Top down
def quick_sort(arr: list) -> list:

    if len(arr)<=1: return arr
    
    pivot = arr[-1] # last element but able to select randomly
    arr = arr[:-1] # remove the pivot from the arr
    lesser = [item for item in arr if item <= pivot]
    greater = [item for item in arr if item > pivot]

    return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a space: ").strip()
    unsorted = [int(item) for item in user_input.split(" ")]
    print(quick_sort(unsorted))

'''
특징
- 제자리 정렬 알고리즘 : 정렬에 사용되는 추가적인 저장공간이 매우 작음
- 불안정적인 정렬 : 같은 값일 때 순서가 변할 수 있음
'''

