S = list(input())

Key = {
    'd':0,
    'r':1,
    'm':2,
    'f':3,
    's':4,
    'l':5,
    'c':6,
    }

M = 'm'
t=0

for i in range(len(S)):
    t += 1
    t += abs(Key[S[i]]-Key[M])
    M = S[i]
print(t)