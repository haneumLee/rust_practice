# 미로 생성
import random

# 전체 미로의 크기 지정
MAP_N = 25

# 미로 초기화
maze = [] #리스트 변수 선언
for y in range(0, MAP_N):
    maze.append([0 for x in range(0, MAP_N)]) # MAP_N 크기의 2차원 리스트 생성

# 둘레를 벽을 감싸기
for n in range(0, MAP_N):
    maze[n][0] = maze[n][MAP_N-1] = 1 #왼쪽 벽과 아래쪽 벽을 만든다
    maze[0][n] = maze[MAP_N-1][n] = 1 #왼쪽 벽과 아래쪽 벽을 만든다

# 2칸마다 1개의 벽을 배치
for y in range(2, MAP_N-2):
    for x in range(2, MAP_N-2):
        if x % 2 == 1 or y % 2 == 1: continue
        maze[y][x] = 1
        # 상하좌우 중 어느 하나를 벽으로 만들기
        r = random.randint(0, 3)
        if r == 0: maze[y-1][x] = 1 # 상
        if r == 1: maze[y+1][x] = 1 # 상
        if r == 2: maze[y][x-1] = 1 # 상
        if r == 3: maze[y][x+1] = 1 # 상

# 미로를 출력
# 0과 1을 각각 흰색 타일(U+2B1C)과 검은색 타일(U+2B1B)로 치환한다
tiles = ["◼︎", "◻"]

for y in range(0, MAP_N):
    for  x in range(0, MAP_N):
        print(tiles[maze[y][x]], end="")
    print("")  