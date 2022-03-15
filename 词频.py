f = open('数据集处理_加强版.txt','r',encoding='utf8')
f1 = open('频数记录_加强版.txt','w',encoding='utf8')
records = {}
while True:
    list_data1 = f.readline()
    if len(list_data1) == 0:
        break
    list_data = list_data1.split(',')
    if '未知' in list_data[1]:
        continue
    word = list_data[0]
    records[word] = {'男':0,'女':0}
f.seek(0)
while True:
    list_data1 = f.readline()
    if len(list_data1) == 0:
        break
    list_data = list_data1.split(',')
    if '未知' in list_data[1]:
        continue
    word = list_data[0]
    target = list_data[1].replace('\n','')
    records[word][target] =records[word][target] + 1
f1.write(str(records))
print(records)