n=int(input())
a,b=list(input().strip()),input().strip()
if sorted(a)!=sorted(b):
    print(-1)
    exit()
s=0
for i in range(n):
    if a[i]!=b[i]:
        k=a.index(b[i],i)
        while k>i:
            a[k],a[k-1]=a[k-1],a[k]
            s+=1
            k-=1
print(s)
