# 2차원 배열의 특정 부분만 회전시키기
sy, sx = 2, 2 # 회전시킬 부분의 왼쪽 위 모서리 위치
length = 3

def rotated_90(sy, sx, length):
    arr = [[7*j+i for i in range(1, 8)] for j in range(7)] # 7x7
    new_arr = [[0] * 7 for _ in range(7)]

    for y in range(sy, sy+length): # [2, 3, 4]
        for x in range(sx, sx+length): # [2, 3, 4]
            # 1단계 : (0, 0)으로 옮겨주는 변환
            oy, ox = y-sy, x-sx
            # 2단계 : 90도 회전했을때의 좌표 구하기
            ry, rx = ox, length-oy-1
            # 3단계 : 다시 (sy,sx) 더하기
            new_arr[sy+ry][sx+rx] = arr[y][x]

    # new-arr 값을 현재 board에 옮기기
    for y in range(sy, sy+length):
        for x in range(sx, sx+length):
            arr[y][x] = new_arr[y][x]

    return arr

def rotated_180(sy, sx, length):
    arr = [[7*j+i for i in range(1, 8)] for j in range(7)] # 7x7
    new_arr = [[0] * 7 for _ in range(7)]

    for y in range(sy, sy+length):
        for x in range(sx, sx+length):
            oy, ox = y-sy, x-sx
            ry, rx = length-oy-1, length-ox-1
            new_arr[sy+ry][sx+rx] = arr[y][x]
    
    for y in range(sy, sy+length):
        for x in range(sx, sx+length):
            arr[y][x] = new_arr[y][x]

    return arr

def rotated_270(sy, sx, length):
    arr = [[7*j+i for i in range(1, 8)] for j in range(7)]
    new_arr = [[0] * 7 for _ in range(7)]

    for y in range(sy, sy+length):
        for x in range(sx, sx+length):
            oy, ox = y-sy, x-sx
            ry, rx = length-ox-1, oy
            new_arr[sy+ry][sx+rx] = arr[y][x]

    for y in range(sy, sy+length):
        for x in range(sx, sx+length):
            arr[y][x] = new_arr[y][x]

    return arr

arr_90 = rotated_90(sy, sx, length)
arr_180 = rotated_180(sy, sx, length)
arr_270 = rotated_270(sy, sx, length)

print('Rotate 90')
for i in range(len(arr_90)):
    print(arr_90[i])

print('Rotate 180')
for i in range(len(arr_180)):
    print(arr_180[i])

print('Rotate 270')
for i in range(len(arr_270)):
    print(arr_270[i])