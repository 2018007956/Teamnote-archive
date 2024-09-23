# 순서 상관 X, 중복 O
arr = [1, 2, 3, 4]

def combinations_with_replacement(n, new_arr, c):
    if len(new_arr) == n:
        print(new_arr)
        return
    
    for i in range(c, len(arr)):
        combinations_with_replacement(n, new_arr+[arr[i]], i)


combinations_with_replacement(2, [], 0)