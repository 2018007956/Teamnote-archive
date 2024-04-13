from functools import cmp_to_key
def cmp(a, b):
    a, b = map(str, (a, b))
    return int(b+a) - int(a+b)

arr = [("John", 25),
        ("Alice", 30),
        ("Bob", 25),
       ("John", 30)]
arr2 = [6, 10, 2]

# 1. sorted by lambda
print(sorted(arr, key=lambda x: (x[1], x[0]))) # 오름차순
print(sorted(arr, key=lambda x: (x[1], x[0]), reverse=True)) # 내림차순

# 2. sorted by cmp_to_key
print(sorted(arr2, key=cmp_to_key(cmp)))

# 3. sorted by custom function
def custom_sort(arr, cmp):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if cmp(arr[i], arr[j]) > 0:
                arr[i], arr[j] = arr[j], arr[i]
custom_sort(arr2, cmp)
print(arr2)

# 3. sorted by custom function (bubble sort)
def custom_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if (arr[j][1] > arr[j + 1][1]) or (arr[j][1] == arr[j + 1][1] and arr[j][0] > arr[j + 1][0]): # 나이가 같으면 이름으로 비교
                arr[j], arr[j+1] = arr[j+1], arr[j]
custom_sort(arr)
print(arr)