A = int(input()) #4
B = [int(A) for A in input().split()]
if len(set(B)) == len(B):
    print('Yes')
else:
    print('No')
