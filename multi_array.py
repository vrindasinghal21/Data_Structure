n,m = map(int,input().split())
arr = [[0 for i in range(n)]for j in range(m)]
print(arr)
for i in range(n):
    temp = list(map(int,input().split()))
    for j in range(m):
        arr[j][i] = temp[j]
for i in arr:
    for j in i:
        print(j,end=' ')
    print()