'''
json.dumps

dictData = {'a':1, 'b':2}
jsonData = json.dumps(dictData)  # dumps将数据对象转变为json格式
print jsonData
{"a": 1, "b": 2}
json.loads

print json.loads(jsonData)  # 与dumps相反，将json对象转变为字典对象返回
{u'a': 1, u'b': 2}
json.dump

with open('test.json', 'w') as f:
    json.dump(dictData, f)  # 将对象转变为json格式并存入文件中
json.load

with open('test.json') as f:
    print json.load(f)  # 将json文件转变为字典返回
{u'a': 1, u'b': 2}
'''