import D
data=[]
time=[3,2,3,2,2,3,2,3,4,2,3,2,5,3,2,3,2,2,2,3,3,2,3,2,2,2]
for i in range(26):
    data.append([])
    for j in range(26):
        data[i].append(float('inf'))
data[0][1]=data[1][0]=2
data[1][2]=data[2][1]=1
data[1][3]=data[3][1]=3
data[1][18]=data[18][1]=5
data[2][4]=data[4][2]=1
data[2][5]=data[5][2]=1
data[3][20]=data[20][3]=1
data[3][22]=data[22][3]=4
data[4][6]=data[6][4]=2
data[5][7]=data[7][5]=2
data[5][13]=data[13][5]=1
data[5][9]=data[9][5]=5
data[7][16]=data[16][7]=1
data[8][23]=data[23][8]=2
data[8][24]=data[24][8]=3
data[9][10]=data[10][9]=2
data[9][11]=data[11][9]=6
data[10][12]=data[12][10]=2
data[10][14]=data[14][10]=7
data[11][14]=data[14][11]=2
data[12][15]=data[15][12]=2
data[14][17]=data[17][14]=2
data[14][25]=data[25][14]=6
data[15][17]=data[17][15]=3
data[16][24]=data[24][16]=1
data[18][19]=data[19][18]=2
data[19][21]=data[21][19]=2
data[20][21]=data[21][20]=2
data[21][22]=data[22][21]=1
data[22][23]=data[23][22]=1
data[24][25]=data[25][24]=3
al_way=D.Dijkstra(data,22)
save_way=[]
flag=1
for i in al_way:
    flag=1
    for j in al_way:
        if(j[1:-1].count(i[-1])>0):
            flag=0
    if(flag==1):
        save_way.append(i)
tt=0
for k in time:
    tt+=k
for j in save_way:
    print(j)

