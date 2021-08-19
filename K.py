a=[[0,1,2,3,2,1],[1,0,1,2,3,2],[2,1,0,1,2,3],[3,2,1,0,1,2],[2,3,2,1,0,1],[1,2,3,2,1,0]]
dat=[]
pot=[]
way=[]
r=len(a[0])
for i in range(r):
    a[i][i]=-1
for i in range(r**2-r):
    compare = float('inf')
    dat.append([])
    for x in range(r):
        for y in range(r):
            if a[x][y]<compare and a[x][y]>0:
                compare=a[x][y]
                dat[i]=[x,y,compare]
    a[dat[i][0]][dat[i][1]]=float('inf')
pot.append(dat[0][0])
pot.append(dat[0][1])
cost=dat[0][2]
way.append(dat[0])
dat.remove(dat[0])
for i in range(r-2):
    for u in dat:
        if (pot.count(u[0])==1 and pot.count(u[1])==0):
            pot.append(u[1])
            cost+=u[2]
            dat.remove(u)
            way.append(u)
            break
        if (pot.count(u[1]) == 1 and pot.count(u[0]) == 0):
            pot.append(u[0])
            cost += u[2]
            dat.remove(u)
            way.append(u)
            break
print('pot   :'+str(pot))
print('cost  :'+str(cost))
print('way   :'+str(way))