# 배열에서 두 숫자의 합이 특정 숫자가 되는 쌍의 개수 구하기
def Solution(arr, target):
    arr.sort()
    cnt = 0
    start, end = 0, len(arr)-1
    while start < end:
        Sum = arr[start]+arr[end]
        if Sum > target:
            end -= 1
        elif Sum < target:
            start += 1
        else:
            print(arr[start], arr[end])
            cnt += 1
            start += 1
            end -= 1
    return cnt

arr = [1,2,3,4,5,4,6,8,2]
target = 10
print('result: ', Solution(arr, target))