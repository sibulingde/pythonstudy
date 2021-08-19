import os
import xlrd
import xlwt
def add(url,coun,saveurl):
    wb=xlwt.Workbook()
    wb.encoding="UTF-8"
    b=[]
    for i in range(coun):
        b.append(wb.add_sheet("table"+str(i)))
    temp=[[],[]]
    for root,dirs,files in os.walk(url):
        for file in files:
            data=xlrd.open_workbook(url+"/"+file)
            data.encoding="UTF-8"
            for i in range(len(data.sheet_names())):
                table=data.sheet_by_index(i)
                for j in range(table.nrows):
                    d=table.row_values(j)
                    if d.count("")!=len(d) and temp[i].count(d)==0:
                        temp[i].append(d)
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            for h in range(len(temp[i][j])):
                b[i].write(j,h,temp[i][j][h])
    wb.save(saveurl+"/save.xls")
    input("save successfully!")

if __name__=="__main__":
    a=input("文件路径")
    b=input("每一个Exel文件里表数量：")
    c=input("存储路径：")
    add(a,int(b),c)