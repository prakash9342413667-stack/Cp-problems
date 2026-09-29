l=[]
t=int(input())
for i in range(t):
    l.append(int(input()))
for i in l:
    f=1
    for j in range(i):
        f*=(j+1)
    print(f)