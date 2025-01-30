n, m = tuple(map(int, input().split()))

arr = [
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]

for _ in range(m):
    r, c = tuple(map(int, input().split()))
    arr[r][c] = r*c

for i in range(1, n+1):
    for j in range(1, n+1):
        print(arr[i][j], end = " ")
    print()