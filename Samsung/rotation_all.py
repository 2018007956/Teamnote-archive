arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

## 1) zip() 활용
# 시계 방향 90 (= 반시계 방향 270)
arr_90 = list(map(list, zip(*arr[::-1])))
print(arr_90)

# 시계 방향 180 (= 반시계 방향 180)
arr_180 = [x[::-1] for x in arr[::-1]]
print(arr_180)

# 시계 방향 270 (= 반시계 방향 90)
arr_270 = [x for x in list(map(list, zip(*arr)))[::-1]]
print(arr_270)

# (+) 정사각형이 아닌 직사각형의 경우에도 배열의 인덱스 고민없이 빠르게 처리하기 좋다
# (-) 메모리나 시간 복잡도 면에서는 2번 방식보다 좋지 않다

## 2) 인덱스 규칙 활용
M = len(arr)
N = len(arr[0])

def rotated_90(arr):
    result = [[0] * M for _ in range(N)]
    for i in range(M):
        for j in range(N):
            result[j][M-i-1] = arr[i][j]
    return result

def rotated_180(arr):
    result = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            result[M-i-1][N-j-1] = arr[i][j]
    return result

def rotated_270(arr):
    result = [[0] * M for _ in range(N)]
    for i in range(M):
        for j in range(N):
            result[N-1-j][i] = arr[i][j]
    return result

print(rotated_90(arr))
print(rotated_180(arr))
print(rotated_270(arr))

# 정사각형의 경우
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
N = 3
result = [[0] * N for _ in range(N)]
def rotated_90(arr):
    for i in range(N):
        for j in range(N):
            result[j][N-i-1] = arr[i][j]
    return result

def rotated_180(arr):
    for i in range(N):
        for j in range(N):
            result[N-i-1][N-j-1] = arr[i][j]
    return result

def roated_270(arr):
    for i in range(N):
        for j in range(N):
            result[N-i-1][j] = arr[i][j]
    return result

print(rotated_90(arr))
print(rotated_180(arr))
print(rotated_270(arr))