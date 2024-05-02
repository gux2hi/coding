S = input()
N = int(input())
li = list(map(int,input().split()))
T=""
for i in range(N):
    T+=li[i]*"a"
    T+=""
print(f"{S}"+" "+f"{T}")
print(li)