s=input().strip()
n=int(input())
l=[]
for _ in range(n):
    a,b=map(int,input().split())
    l.append(s[a-1:b].count('T'))
print(*(i for i in l),sep='\n')
