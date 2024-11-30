from openpyxl.writer.excel import ExcelWriter 
from openpyxl.workbook import Workbook
from types import MappingProxyType
from openpyxl.utils import get_column_letter
import xlwt
import pandas as pd 
import numpy as np
import xlrd
import xlsxwriter
import matplotlib.pyplot as plt
def v_z_chazhi(x0,a,n):#Reservoir Capacity-Water Level Interpolation
    for j in range(1,n):
        if x0<=y2[j][a] and x0>y2[j-1][a]:
            return y1[j-1][a]+(x0-y2[j-1][a])*(y1[j][a]-y1[j-1][a])/(y2[j][a]-y2[j-1][a])
        if x0<=y2[0][a]:
            return y1[0][a]
        if x0>y2[n-1][a]:
            return y1[n-1][a]
def z_v_chazhi(x0,a,n):#Water Level-Reservoir Capacity Interpolation
    for j in range(1,n):
        if x0<=y1[j][a] and x0>y1[j-1][a]:
            return y2[j-1][a]+(x0-y1[j-1][a])*(y2[j][a]-y2[j-1][a])/(y1[j][a]-y1[j-1][a]) 
        if x0<=y1[0][a]:
            return y2[0][a]
        if x0>y1[n-1][a]:
            return y2[n-1][a] 
y1=np.zeros((200,40))
y2=np.zeros((200,40))
y3=np.zeros((200,40))
y4=np.zeros((200,40))
 
vmin=np.zeros(10)
vmax=np.zeros(10)
num=np.zeros((20),dtype=int)
num1=np.zeros((20),dtype=int)
H1=np.zeros(10)
stll=np.zeros(3)
stll[0]=100
stll[1]=100
Nzh=np.zeros(10)# ensured output capacity
yr=np.zeros((200,40))# output capacity
yqx=np.zeros((200,100))
t=np.zeros(100)
V=np.zeros((200,40))
V[0][0]=5.43
zss=np.zeros((200,40))
V[1][0]=14.9
    
       
wb=xlrd.open_workbook('特征曲线.xlsx')
table=wb.sheets()[0]
 
for i in range(0,22):
    y1[i][0]=float(table.cell_value(i,0))
    y2[i][0]=float(table.cell_value(i,1))
for i in range(0,25):
    y1[i][1]=float(table.cell_value(i,2))
    y2[i][1]=float(table.cell_value(i,3))
table1=wb.sheets()[1]
for i in range(0,10):
    y3[i][0]=float(table1.cell_value(i,0))
    y4[i][0]=float(table1.cell_value(i,1))
for i in range(0,9): 
    y3[i][1]=float(table1.cell_value(i,2))
    y4[i][1]=float(table1.cell_value(i,3))
# Load normal water level, dead water level, and output capacity.

zss[0][0]=2855

zss[0][6]=2889
zss[0][11]=2855
zss[1][0]=2672
zss[1][6]=2702
zss[1][11]=2672

H1[2]=55
H1[3]=84
H1[4]=78
H1[5]=144
H1[6]=144.5
num[0]=22
num[1]=25
vmin[1]=14.9
vmax[1]=23.14
vmax[0]=10.8
vmin[0]=5.43
Nzh[0]=2240000
Nzh[1]=2000000
Nzh[2]=750000
Nzh[3]=1200000
Nzh[4]=826000
Nzh[5]=2400000
Nzh[6]=2400000
def z_q_chazhi(x1,b,n1):#Downstream water level - Power generation flow interpolation
    for i in range(1,n1):
        if x1<y4[i][b] and x1>y4[i-1][b]:
            return y3[i-1][b]+(x1-y4[i-1][b])*(y3[i][b]-y3[i-1][b])/(y4[i][b]-y4[i-1][b]) 
        if x1<=y4[0][b]:
             return y3[0][b]
        if x1>y4[n1-1][b]:
            return y3[n1-1][b]
def q_z_chazhi(x1,b,n1):# Power generation flow—— water level interpolation
    for i in range(1,n1):
        if x1<y3[i][b] and x1>y3[i-1][b]:
            return y4[i-1][b]+(x1-y3[i-1][b])*(y4[i][b]-y4[i-1][b])/(y3[i][b]-y3[i-1][b]) 
        if x1<=y3[0][b]:
             return y4[0][b]
        if x1>y3[n1-1][b]:
            return y4[n1-1][b] 

E1=np.zeros((200,100))
zzz=np.zeros((20,30))
t1=np.zeros(20)
t1[8]=744.0
t1[9]=672.0
t1[10]=744.0
t1[11]=720.0
t1[12]=744.0
t1[1]=720.0
t1[2]=744.0
t1[3]=744.0
t1[4]=720.0
t1[5]=744.0
t1[6]=720.0
t1[7]=744.0
E3=0
qs=np.zeros((200,30))
zdq=np.zeros(10)#允许流量
yv=np.zeros((100,40)) #离散库容
V2=np.zeros((61000,30))
qxs=np.zeros((200,40))#过水发电流量
yqx=np.zeros((200,100))
qx1=np.zeros((200,30))
hs=np.zeros((200,13))
zx=np.zeros((200,40))#下游水位
N=7
 
ls=np.zeros((200,30))#来水量
M=12
qss=np.zeros((200,40))
N1=np.zeros((200,40))
qxs1=np.zeros((200,40)) 
vd=np.zeros(20)
q2=np.zeros((100,20)) 
max_income=np.zeros(100)
y_v=np.zeros((200,40))
y_v[0][6]=10.7995
y_v[1][6]=23.14
y_v[0][12]=5.43
y_v[1][12]=14.9
E=np.zeros((200,40))
E1=np.zeros(61000)
E2=np.zeros(61000)
E4=np.zeros((200,30))
N5=np.zeros(20)
E5=np.zeros(20)#优化后各时段发电量
zdq[0]=1483
zdq[1]=1541
zdq[2]=1603.2
zdq[3]=1622.4
zdq[4]=1631
zdq[5]=1866.4
zdq[6]=2000

q1=np.zeros((50,13))#入库流量
q3=np.zeros(200)#区间流量
N3=np.zeros(200)
qx=np.zeros((200,40))#出库流量
qss1=np.zeros((200,30))
num1[1]=9
num1[0]=10
ruku=[]
chuku=[]
init_plot=[]  
winner_plot=[]
V1=np.zeros((61000,50))
def tjsk(x,j,r):
    zss[j][r-1]=v_z_chazhi(V[j][r-1],j,num[j])
    bvs=V[j][r-1]/2.0+(V[j][r]+x*0.00005)/2.0#第一段库容
    bvx=(V[j][r]+x*0.00005)/2.0+V[j][r+1]/2.0#第二段库容
    zss[j][r]=v_z_chazhi(bvs,j,num[j])#第一段水库水位，插值得到
    zss[j][r+1]=v_z_chazhi(bvx,j,num[j])#第二段水库水位，插值得到
    qxs1[j][r]=q1[j][r]+(V[j][r-1]-V[j][r]-x*0.00005)*100000000/t[r]#前一段过水发电流量
    qxs1[j][r+1]=q1[j][r+1]+(V[j][r]+x*0.00005-V[j][r+1])*100000000/t[r+1]
    if qxs1[j][r]>stll[j] and qxs1[j][r+1]>stll[j]:#大于最小下泄流量(即生态流量)
        if qxs1[j][r]<=zdq[j]:#小于最大允许流量
            zx[j][r]=q_z_chazhi(qxs1[j][r],j,num1[j])#根据发电流量插补出下游水位
            hs[j][r]=(zss[j][r]+zss[j][r-1])/2.0-zx[j][r]#前一时段的平均水头=前一时段的水库水位-下游水位
            N4[j][r]=8.7*qxs1[j][r]*hs[j][r]#出力
            qx[j][r]=qxs1[j][r]
            if N4[j][r]>Nzh[j]:
                
                N4[j][r]=Nzh[j]
                qxs1[j][r]=N4[j][r]/8.7/hs[j][r]
            qs[j][r]=qx[j][r]-qxs1[j][r]
        if qxs1[j][r]>zdq[j]:#大于最大允许流量
            qxs1[j][r]=zdq[j]
            zx[j][r]=q_z_chazhi(qxs1[j][r],j,num1[j])
            hs[j][r]=(zss[j][r]+zss[j][r-1])/2.0-zx[j][r]
            N4[j][r]=8.7*qxs1[j][r]*hs[j][r]
            qx[j][r]=qxs1[j][r]
            if N4[j][r]>Nzh[j]:
                
                N4[j][r]=Nzh[j]
                qxs1[j][r]=N4[j][r]/8.7/hs[j][r]
            qs[j][r]=qx[j][r]-qxs1[j][r]
        if qxs1[j][r+1]<=zdq[j]:
            zx[j][r+1]=q_z_chazhi(qxs1[j][r+1],j,num1[j])
            hs[j][r+1]=(zss[j][r+1]+zss[j][r])/2.0-zx[j][r+1]
            N4[j][r+1]=8.7*qxs1[j][r+1]*hs[j][r+1]
            qx[j][r+1]=qxs1[j][r+1]
            if N4[j][r+1]>Nzh[j]:
                
                N4[j][r+1]=Nzh[j]
                qxs1[j][r+1]=N4[j][r+1]/8.7/hs[j][r+1]
            qs[j][r+1]=qx[j][r+1]-qxs1[j][r+1]
        if qxs1[j][r+1]>zdq[j]:
            qxs1[j][r+1]=zdq[j]
            zx[j][r+1]=q_z_chazhi(qxs1[j][r+1],j,num1[j])
            hs[j][r+1]=(zss[j][r+1]+zss[j][r])/2.0-zx[j][r+1]
            qx[j][r+1]=qxs1[j][r+1]
            N4[j][r+1]=8.7*qxs1[j][r+1]*hs[j][r+1]
            if N4[j][r+1]>Nzh[j]:
                N4[j][r+1]=Nzh[j]
                qxs1[j][r+1]=N4[j][r+1]/8.7/hs[j][r+1]
            qs[j][r+1]=qx[j][r+1]-qxs1[j][r+1]                            
    return N4[j][r],N4[j][r+1],qxs1[j][r],qxs1[j][r+1],qs[j][r],qs[j][r+1]
q4=np.zeros((20,20))
N2=np.zeros(20)
YeBaTan_N=[]
LaWa_N=[]
BaTang_N=[]
SuWaLong_N=[]
ChangBo_N=[]
XuLong_N=[]
BenZiLan_N=[] 
ZN=np.zeros(20)
N_N=0   
if __name__=="__main__":
    xlsx=xlrd.open_workbook('枯水年.xlsx')
    sheet1=xlsx.sheets()[0]
# print(type(sheet1))
# print(sheet1.cell_value(1,3))
#加载初始轨迹
    N4=np.zeros((200,40))
    for i in range(1,13):
        V[0][i]=float(sheet1.cell_value(4,i))
        zzz[0][i]=float(sheet1.cell_value(2,i))
        yr[0][i]=float(sheet1.cell_value(8,i))
        N4[0][i]=yr[0][i]
        yqx[0][i]=float(sheet1.cell_value(11,i))
        t[i]=float(sheet1.cell_value(7,i))
        zss[0][i]=float(sheet1.cell_value(2,i))
        qss1[0][i]=float(sheet1.cell_value(12,i))
        qx1[0][i]=qss1[0][i]+yqx[0][i]
    sheet2=xlsx.sheets()[1]
    for i in range(1,13):
        V[1][i]=float(sheet2.cell_value(4,i))
        zzz[1][i]=float(sheet2.cell_value(2,i))
        yr[1][i]=float(sheet2.cell_value(8,i))
        N4[1][i]=yr[1][i]
        yqx[1][i]=float(sheet2.cell_value(11,i))
        zss[1][i]=float(sheet2.cell_value(2,i))
        qss1[1][i]=float(sheet2.cell_value(12,i))
        qx1[1][i]=qss1[1][i]+yqx[1][i]
    xlsx3=xlrd.open_workbook('枯水年.xlsx')
    for j in range(2,7):
        sheet1=xlsx3.sheets()[j]
        for i in range(1,sheet1.ncols):
            yr[j][i]=sheet1.cell_value(6,i)
            N4[j][i]=yr[j][i]
            ls[j][i]=sheet1.cell_value(3,i)
            yqx[j][i]=sheet1.cell_value(7,i)
            qss1[j][i]=float(sheet1.cell_value(8,i))
    wb=xlrd.open_workbook('特征曲线.xlsx')
    table=wb.sheets()[0]
 
    for i in range(0,22):
        y1[i][0]=float(table.cell_value(i,0))
        y2[i][0]=float(table.cell_value(i,1))
    for i in range(0,25):
        y1[i][1]=float(table.cell_value(i,2))
        y2[i][1]=float(table.cell_value(i,3))
    table1=wb.sheets()[1]
    for i in range(0,10):
        y3[i][0]=float(table1.cell_value(i,0))
        y4[i][0]=float(table1.cell_value(i,1))
    for i in range(0,9): 
        y3[i][1]=float(table1.cell_value(i,2))
        y4[i][1]=float(table1.cell_value(i,3))
    xlsx_1=xlrd.open_workbook('流量.xlsx')
    sheet1=xlsx_1.sheets()[2]
# print(type(sheet1))
# print(sheet1.cell_value(1,3))
# print(type(sheet1.cell_value(1,3)))
    for j in range(0,7):
        for i in range(1,sheet1.ncols):
            q1[j][i]=float(sheet1.cell_value(j+1,i))
            q3[i]=(q1[1][i]-q1[0][i])
    for i in range(1,13):
        for j in range(0,7):
            N3[i]+=yr[j][i]
        N_N+=N3[i]
        init_plot.append(N3[i]/10000)
        E1[i]=N3[i]*t1[i]
  
        E3+=N3[i]*t1[i]
    for j in range(0,7):
        N2[j]=0
        for i in range(1,13):
            N2[j]+=yr[j][i]
        print(N2[j])
    for i in range(1,12):
        max_income[i]=E1[i]+E1[i+1]
    #N3[8]=2271000
    #N3[9]=1990000
    N3[7]=2000000
    N3[12]=2000000
    for i in range(1,13):
        q4[1][i]=yqx[0][i]+q3[i]
       
    E2[0]=E3
    for k in range(1,60000):
        E2[k]=E2[k-1]
        for r in range(1,12):
            
            for m in range(-1,2):
                
                y_v[0][r]=V[0][r]+m*0.00005
                if y_v[0][r]>5.43 and y_v[0][r]<10.8:
                   # ZN=0
                   # ZN1=0
                    N1[0][r],N1[0][r+1],qxs[0][r],qxs[0][r+1],qss[0][r],qss[0][r+1]=tjsk(m,0,r)
                    
                   # ZN1+=N1[0][r+1]
                   # ZN+=N1[0][r]
                 
                    q1[1][r]=qxs[0][r]+q3[r]+qss[0][r]
                    q1[1][r+1]=qxs[0][r+1]+q3[r+1]+qss[0][r+1]
                    for n in range(-1,2):
                         
                        y_v[1][r]=V[1][r]+n*0.00005
                        if y_v[1][r]>=14.9 and y_v[1][r]<=23.14:  
                            V1[k][r]=y_v[0][r]
                            V2[k][r]=y_v[1][r]
                            g=0
                            g1=0
                            sum1=0
                            N1[1][r],N1[1][r+1],qxs[1][r],qxs[1][r+1],qss[1][r],qss[1][r+1]=tjsk(n,1,r)
                          #  sum+=N1[1][r]
                           # sum1+=N1[1][r+1]
                            
                            for j in range(2,7):
                    #无调节水电站
                                qxs[j][r]=qxs[j-1][r]+(q1[j][r]-q1[j-1][r])+qss[j-1][r]
                   
                                N1[j][r]=8.7*qxs[j][r]*H1[j]
                                qxs[j][r+1]=qxs[j-1][r+1]+(q1[j][r+1]-q1[j-1][r+1])+qss[j-1][r+1]
                                N1[j][r+1]=8.7*qxs[j][r+1]*H1[j]
                                qx[j][r]=qxs[j][r]
                                qx[j][r+1]=qxs[j][r+1]
                                if N1[j][r]>Nzh[j]:
                                    N1[j][r]=Nzh[j]
                                    qxs[j][r]=N1[j][r]/8.7/H1[j]
                                qss[j][r]=qx[j][r]-qxs[j][r]
                                if N1[j][r+1]>Nzh[j]:
                                    N1[j][r+1]=Nzh[j]
                                    qxs[j][r+1]=N1[j][r+1]/8.7/H1[j]
                                qss[j][r+1]=qx[j][r+1]-qxs[j][r+1]
                              #  sum+=N1[j][r]
                             #   sum1+=N1[j][r+1]
                            N_N=N_N-ZN[r]-ZN[r+1]
                            ZN[r]=0
                            ZN[r+1]=0
                 
                            for q in range(0,7):
                                ZN[r]+=N1[q][r]

                                ZN[r+1]+=N1[q][r+1]
                        #计算前后两时段发电量
                            N_N=N_N+ZN[r]+ZN[r+1]
                            total=ZN[r]*t1[r]+ZN[r+1]*t1[r+1]  
                           # print(total)
                          #  print(ZN)
                           # print(N3[r])
                         #   print(ZN1)
                         #   print(N3[r+1])
                            if ZN[r]<2000000:
                                total=total+10000000000*(ZN[r]-2000000)
                        
                            if ZN[r+1]<2000000:
                                total=total+10000000000*(ZN[r+1]-2000000) 
                          #  print(total) 
                          #  print(max_income[r])
                            if total>max_income[r]:
                                q4[1][r]=q1[1][r]
                                E2[k]=E2[k]-max_income[r]
                                max_income[r]=total
                                E2[k]=E2[k]+max_income[r]
                            
                                for z in range(0,7):
                                    yr[z][r]=N1[z][r]
                                    yr[z][r+1]=N1[z][r+1]
                                    yqx[z][r]=qxs[z][r]
                                    yqx[z][r+1]=qxs[z][r+1]
                                    qss1[z][r]=qss[z][r]
                                    qss1[z][r+1]=qss[z][r+1] 
                                    qx1[z][r]=qss1[z][r]+yqx[z][r]  
                                    qx1[z][r+1]=qss1[z][r+1]+yqx[z][r+1] 
                                for x in range(2,7):
                                    ls[x][r]=qxs[x-1][r]+(q1[x][r]-q1[x-1][r])+qss[x-1][r]
                                    ls[x][r+1]=qxs[x-1][r+1]+(q1[x][r+1]-q1[x-1][r+1])+qss[x-1][r+1]
                                V[0][r]=y_v[0][r]
                                V[1][r]=y_v[1][r]
                                zzz[0][r]=v_z_chazhi(V[0][r],0,22)
                                zzz[1][r]=v_z_chazhi(V[1][r],1,25)
                                print(r)
                                print(V[0][r])
                                print(V[1][r])
                            
                        else:
                            continue
                else:
                    continue
       
           
             
               
       
        if abs((E2[k]-E2[k-1])/E2[k])<0.00000006: 
            workbook=xlsxwriter.Workbook('结果1.xlsx')
            worksheet=workbook.add_worksheet()
        
            col=0
            for i in range(1,200):
                row=0
                for r in range(1,13):
                    worksheet.write(row,col,V1[i][r])
                    row+=1
                col+=1
            worksheet=workbook.add_worksheet()
        
            col1=0
            for i in range(1,200):
                row1=0
                for r in range(1,13):
                    worksheet.write(row1,col1,V2[i][r])
                    row1+=1
                col1+=1
            workbook.close()
            """for r in range(1,13):
                zzz[0][r]=v_z_chazhi(V[0][r],0,22)
                zzz[1][r]=v_z_chazhi(V[1][r],1,25)
            for r in range(1,12):
                for z in range(0,7):
                    yr[z][r]=N1[z][r]
                    yr[z][r+1]=N1[z][r+1]
                    yqx[z][r]=qxs[z][r]
                    yqx[z][r+1]=qxs[z][r+1]
                    qss1[z][r]=qss[z][r]
                    qss1[z][r+1]=qss[z][r+1] 
                    qx1[z][r]=qss1[z][r]+yqx[z][r]  
                    qx1[z][r+1]=qss1[z][r+1]+yqx[z][r+1] 
                for x in range(2,7):
                    ls[x][r]=qxs[x-1][r]+(q1[x][r]-q1[x-1][r])+qss[x-1][r]
                    ls[x][r+1]=qxs[x-1][r+1]+(q1[x][r+1]-q1[x-1][r+1])+qss[x-1][r+1]"""
            for y in range(1,13):
                N5[y]=0
                E5[y]=0
                E1[y]=E1[y]/100000000
                for x in range(0,7):
                    E4[x][y]=yr[x][y]*t1[y]/100000000
                    yr[x][y]=yr[x][y]/10000
                    N5[y]+=yr[x][y]
                    E5[y]+=E4[x][y]
            
            df1_dic={'叶巴滩水位':zzz[0][1:13],'入库流量':q1[0][1:13],'叶巴滩发电流量':yqx[0][1:13],'叶巴滩弃水':qss1[0][1:13],'叶巴滩出力':yr[0][1:13],'叶巴滩发电量':E4[0][1:13],
            '拉哇水位':zzz[1][1:13],'入库流量1':q4[1][1:13],'拉哇发电流量':yqx[1][1:13],'拉哇弃水':qss1[1][1:13],'拉哇出力':yr[1][1:13],'拉哇发电量':E4[1][1:13],
            '来水流量2':ls[2][1:13],'发电流量2':yqx[2][1:13],'巴塘弃水':qss1[2][1:13],'巴塘出力':yr[2][1:13],'巴塘发电量':E4[2][1:13],
            '来水流量3':ls[3][1:13],'发电流量3':yqx[3][1:13],'苏洼龙弃水':qss1[3][1:13],'苏洼龙出力':yr[3][1:13],'苏洼龙发电量':E4[3][1:13],
            '来水流量4':ls[4][1:13],'发电流量4':yqx[4][1:13],'昌波弃水':qss1[4][1:13],'昌波出力':yr[4][1:13],'昌波发电量':E4[4][1:13],
            '来水流量5':ls[5][1:13],'发电流量5':yqx[5][1:13],'旭龙弃水':qss1[5][1:13],'旭龙出力':yr[5][1:13],'旭龙发电量':E4[5][1:13],
            '来水流量6':ls[6][1:13],'发电流量6':yqx[6][1:13],'奔子栏弃水':qss1[6][1:13],'奔子栏出力':yr[6][1:13],'奔子栏发电量':E4[6][1:13],'总出力':N5[1:13],'优化前各时段发电量':E1[1:13],'优化后各时段发电量':E5[1:13]}
            df1=pd.DataFrame.from_dict(df1_dic)
            # for i in range(13):
            #     df1.append({V[0][i:i],yr[0][i:i]})
                
            df1.to_excel('枯水年结果.xlsx',sheet_name='Sheet3')
            for y in range(1,13):
                print(N3[y])
            print(k)
            print(E2[k])  
            print(E2[k-1])
            for i in range(1,13):
                YeBaTan_N.append(yr[0][i])
                LaWa_N.append(yr[1][i])
                BaTang_N.append(yr[2][i])
                SuWaLong_N.append(yr[3][i])
                ChangBo_N.append(yr[4][i])
                XuLong_N.append(yr[5][i])
                BenZiLan_N.append(yr[6][i])
                
            plt.rcParams['font.sans-serif']=['SimHei']
            plt.rcParams['axes.unicode_minus']=False
            plt.figure(1)
            #ind=np.arange(M)
            bar_width=0.1
            index_N1=np.arange(12)
            index_N2=index_N1+bar_width
            index_N3=index_N2+bar_width
            index_N4=index_N3+bar_width
            index_N5=index_N4+bar_width
            index_N6=index_N5+bar_width
            index_N7=index_N6+bar_width
            plt.bar(index_N1,height=YeBaTan_N,width=bar_width,color='#FFA500',label='叶巴滩各月出力')
            plt.bar(index_N2,height=LaWa_N,width=bar_width,color='r',label='拉哇各月出力')
            plt.bar(index_N3,height=BaTang_N,width=bar_width,color='#87CEEB',label='巴塘出力')
            plt.bar(index_N4,height=SuWaLong_N,width=bar_width,color='#2E8B57',label='苏洼龙出力')
            plt.bar(index_N5,height=ChangBo_N,width=bar_width,color='#00FF7F',label='昌波各月出力')
            plt.bar(index_N6,height=XuLong_N,width=bar_width,color='#4169E1',label='旭龙各月出力')
            plt.bar(index_N7,height=BenZiLan_N,width=bar_width,color='#FA8072',label='奔子栏各月出力')
            months=('6月','7月','8月','9月','10月','11月','12月','1月','2月','3月','4月','5月')
            plt.legend()
            plt.xticks(index_N1+bar_width*2,months)
            plt.xlabel("月份")
            plt.ylabel("出力/万KW")
            plt.title('枯水年优化后梯级水电站各月出力图')
            #fig,ax=plt.subplots()
           # inits=ax.bar(ind,init_plot,width,color='##ffad00')   
            #winners=ax.bar(ind+width,winner_plot,width,color='#9b3c38')
           # ax.set_xticks(ind+width)
            #ax.set_xticklabels(('6月','7月','8月','9月','10月','11月','12月','1月','2月','3月','4月','5月'))
            #ax.legend((inits[0],winners[0]),('优化前','优化后'))
            plt.show()    
            plt.figure(2)
            for i in range(1,13):
                ruku.append(q1[0][i]) 
                chuku.append(qx1[0][i])
            X=range(1,13)
            plt.plot(X,ruku,color='red',label='入库流量',linewidth=0.5)
            plt.legend(loc='upper right')
            X1=range(1,13)
            plt.plot(X1,chuku,color='black',label='出库流量',linewidth=0.5)
            plt.legend(loc='upper right')
            plt.title('枯水年叶巴滩流量变化图')
            plt.xlim(xmin=1,xmax=12)
            plt.xlabel("月份")
            plt.ylabel("流量(m3/s)")
            plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12],['6月','7月','8月','9月','10月','11月','12月','1月','2月','3月','4月','5月'])
            plt.show()
            plt.figure(3)
            for i in range(1,13):
                winner_plot.append(N5[i])
            X2=range(1,13)
            plt.plot(X2,init_plot,color='red',label='初始各时段出力',linewidth=0.6)
            plt.legend(loc='upper right')
            plt.plot(X2,winner_plot,color='black',label='优化后各时段出力',linewidth=0.6)
            plt.legend(loc='upper right')
            plt.title('枯水年优化前后各时段梯级总出力对比图')
            plt.xlim(xmin=1,xmax=12)
            plt.xlabel("月份")
            plt.ylabel("出力/万KW")
            plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12],['6月','7月','8月','9月','10月','11月','12月','1月','2月','3月','4月','5月'])
            plt.show()
            break
        else:
            continue
    
       



