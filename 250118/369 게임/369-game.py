n = int(input())

for i in range(1, n+1):
    s = str(i)
    count = 0
    for x in s:
        if x=='3' or x=='6' or x=='9':
            count += 1
    if count>0 or i%3==0:
        print(0, end = " ")
    else:
        print(i, end = " ")