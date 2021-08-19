import D
oo=float('inf')
def chR(W):
    R = []
    for j in W:
        l = []
        for i in range(len(j)):
            if j[i] == 0 or j[i] == oo:
                l.append(0)
            else:
                l.append(i + 1)
        R.append(l)
    return R
def Floyd(W):
    R=chR(W)
    for i in range(6):
        tem=D.Dijkstra(W,i+1)
        for dat in tem:
            if dat[0]<W[dat[1]-1][dat[-1]-1]:
                W[dat[1] - 1][dat[-1] - 1]=dat[0]
                R[dat[1] - 1][dat[-1] - 1]=dat[-2]
    print('W:\n')
    for j in W:
        print(j)
    print('R\n')
    for j in R:
        print(j)
if __name__=="__main__":
    a= [[0.0, 9.2, 1.1, 3.5, oo, oo], [1.3, 0.0, 4.7, oo, 7.2, oo], [2.5, oo, 0.0, oo, 1.8, oo],[oo, oo, 5.3, 0.0, 2.4, 7.5], [oo, 6.5, 2.2, 8.9, 0.0, 5.1], [7.7, oo, 2.7, oo, 2.1, 0.0]]
    Floyd(a)
