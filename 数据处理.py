#import

#读取数据
def data_read(path):
    i = 0
    f = open(path,'r',encoding='utf8')
    jishu = 0
    name_gende = []
    while True:
        content = f.readline()
        if len(content) == 0:
            i += 1
            if i >=10:
                break
        else:
            i = 0
            name_gende.append([content.split(',')[0],content.split(',')[1].replace('\n','')])
    return name_gende
f1 = open('数据集处理.txt','w',encoding='utf8')
for i in range(1,9):
    name_genders = data_read('.\\数据\\源数据 ('+str(i)+')csv.csv')
    for name_gender in name_genders:
        target = name_gender[1]
        names = name_gender[0][1:]
        for name in names:
            f1.write(name+','+target+'\n')
f1.close()
