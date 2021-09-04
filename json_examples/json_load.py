import json
with open("dict_1.json",'r',encoding='UTF-8') as load_f:
    dict_1 = json.load(load_f)
print(dict_1)