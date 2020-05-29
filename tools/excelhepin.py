# import xlrd  #读取Excel文件的包
# import xlsxwriter   #将文件写入Excel的包


# #打开一个excel文件
# def open_xls(file):
#     f = xlrd.open_workbook(file)
#     return f


# #获取excel中所有的sheet表
# def getsheet(f):
#     return f.sheets()


# #获取sheet表的行数
# def get_Allrows(f,sheet):
#     table=f.sheets()[sheet]
#     return table.nrows


# #读取文件内容并返回行内容
# def getFile(file,shnum):
#     f=open_xls(file)
#     table=f.sheets()[shnum]
#     num=table.nrows
#     for row in range(num):
#         rdata=table.row_values(row)
#         datavalue.append(rdata)
#     return datavalue


# #获取sheet表的个数
# def getshnum(f):
#     x=0
#     sh=getsheet(f)
#     for sheet in sh:
#         x+=1
#     return x



# #函数入口
# if __name__=='__main__':
#     #定义要合并的excel文件列表
#     allxls=['C:/Users/eastday/Desktop/yuyu.xlsx'] #列表中的为要读取文件的路径
#     #存储所有读取的结果
#     datavalue=[]
#     for fl in allxls:
#         f=open_xls(fl)
#         x=getshnum(f)
#         for shnum in range(x):
#             print("正在读取文件："+str(fl)+"的第"+str(shnum)+"个sheet表的内容...")
#             rvalue=getFile(fl,shnum)
#     #定义最终合并后生成的新文件
#     endfile='C:/Users/eastday/Desktop/yuyu1.xlsx'
#     wb=xlsxwriter.Workbook(endfile)
#     #创建一个sheet工作对象
#     ws=wb.add_worksheet()
#     for a in range(len(rvalue)):
#         for b in range(len(rvalue[a])):
#             c=rvalue[a][b]
#             ws.write(a,b,c)
#     wb.close()

#     print("文件合并完成")


import xlrd
import xlsxwriter
 
# todo 打开excle
xl = xlrd.open_workbook('C:/Users/eastday/Desktop/yuyu1.xlsx')
#print(xl.read())
 
# todo 通过索引获取工作表
table = xl.sheets()[0]
print(table)

col = table.col_values(2)
print(col)
 

import xlwt
# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding = 'utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('My Worksheet')

# 写入excel
# 参数对应 行, 列, 值
for i in range(0,len(col)-1):
    l = col[i+1].split(".")[0]
    print(l)
    worksheet.write(i,0, label = l)

    # 保存
workbook.save('Excel_test.xls')


# workbook = xlrd.open_workbook(u'有趣装逼每日数据及趋势.xls')

# workbooknew = copy(workbook)

# ws = workbooknew.get_sheet(0)

# ws.write(3, 0, 'changed!')

# workbooknew.save(u'有趣装逼每日数据及趋势copy.xls')