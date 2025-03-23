k,n=map(int,input().split())
l=list(map(int,input().split()))
m=[]
for i in range(0,n-k+1):
    m.append(max(l[i:i+k]))
print(min(m))
