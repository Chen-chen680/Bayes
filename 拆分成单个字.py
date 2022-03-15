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
f1 = open('数据集处理_加强版.txt','w',encoding='utf8')

name_genders = data_read('dict_源数据1.txt')
for name_gender in name_genders:
    target = name_gender[1]
    names = name_gender[0][1:]
    for name in names:
        f1.write(name+','+target+'\n')
f1.close()