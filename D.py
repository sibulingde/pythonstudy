oo = float('inf')
def Dijkstra(a,b):
    G=[]
    for i in range(len(a[b-1])):
        G.append(i+1)
    G.remove(b)
    Gp=[b]
    way=[]
    w=a[b-1]
    w[b-1]=oo
    cost=0
    tem={}
    for i in range(len(a)-1):
        mi=min(w)
        p=w.index(mi)+1
        cost+=mi
        w[p-1]=oo
        way.append([mi]+tem.get(p,[b,p]))
        G.remove(p)
        for j in way:
            for k in G:
                if (j[0]+a[j[-1]-1][k-1])<w[k-1]:
                    w[k-1]=j[0]+a[j[-1]-1][k-1]
                    tem[k]=j[1:]+[k]
    return way
if __name__=='__main__':
 a=[[0.0,9.2,1.1,3.5,oo,oo],[1.3,0.0,4.7,oo,7.2,oo],[2.5,oo,0.0,oo,1.8,oo],[oo,oo,5.3,0.0,2.4,7.5],[oo,6.5,2.2,8.9,0.0,5.1],[7.7,oo,2.7,oo,2.1,0.0]]
 print(Dijkstra(a,6))