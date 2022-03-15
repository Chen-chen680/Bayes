f = open('频数记录_加强版.txt','r',encoding='utf8')
f1 = open('频率记录_加强版.txt','w',encoding='utf8')
data = f.read()
data = eval(data)
outdata = {}

total_datas = data.items()
for total_data in total_datas:
    outdata[total_data[0]] = {'男':0,'女':0}
print(outdata)
for total_data in total_datas:
    #print(type(total_data))
    if total_data[1]['男'] + total_data[1]['女'] <20:
        continue
    outdata[total_data[0]]['男'] = total_data[1]['男']/(total_data[1]['男'] + total_data[1]['女'])
    outdata[total_data[0]]['女'] = total_data[1]['女'] / (total_data[1]['男'] + total_data[1]['女'])
print(outdata)
f1.write(str(outdata))