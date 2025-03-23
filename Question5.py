k=list(map(int,input().split()))
if any(i<10 or i>200 for i in k):
    print("INVALID INPUT")
    exit()
s=[k[i::5]for i in range(5)]
p=[sum(i)/4 for i in s]
m=round(max(p))
if m<50:
    print("Energy consumption is optimal")
else:
    print("Sensor Number:",p.index(max(p))+1)
