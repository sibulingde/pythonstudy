a=[[0,1,2,3,2,1],[1,0,1,2,3,2],[2,1,0,1,2,3],[3,2,1,0,1,2],[2,3,2,1,0,1],[1,2,3,2,1,0]]
r=len(a[1])
l=len(a)
sa=[]
cost=0
o=[]
for x in range(l):
    for y in range(r):
        if a[x][y]==0:
            a[x][y]=float('inf')
for j in range(r):
    o.append(min(a[j]))
tm=min(o)
sa.append(o.index(tm)+1)
sa.append(a[o.index(tm)].index(tm)+1)
def clear(s):
 for i in range(len(s)-1):
     for j in range(len(s)-i-1):
         a[s[i]-1][s[i+j+1]-1]=float('inf')
         a[s[i+j+1]-1][s[i]-1]=float('inf')
clear(sa)
for i in range(r-2):
    o.clear()
    for j in range(len(sa)):
        o.append(min(a[sa[j]-1]))
    tm1=min(o)
    sa.append(a[sa[o.index(tm1)]-1].index(tm1))
    sa[i+2]+=1
    clear(sa)
    tm+=tm1
print('way'+str(sa))
print('cost  '+str(tm))

