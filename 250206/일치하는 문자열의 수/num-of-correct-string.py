n, A = input().split()
n = int(n)
cnt = 0

for _ in range(n):
    B = input()
    if B == A:
        cnt+=1
print(cnt)