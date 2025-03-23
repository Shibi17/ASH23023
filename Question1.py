n=int(input())
l=list(map(int,input().split()))
m=0
for i in range(n):
    c=l[i]  
    k=None
    for j in range(i+1,n):
        if c<l[j]:
            k=l[j]-c
            if k>m:
                m=k
print(m)
