count_arr = [0]*10
a, b = tuple(map(int, input().split()))
ans = 0

while a>1:
    count_arr[a%b] += 1
    a//=b

for elem in count_arr:
    ans += elem ** 2

print(ans)