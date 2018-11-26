# 数据结构

## 列表
- 列表是可变的（添加、修改、删除列表元素），使用`[]`括起，使用`,`分隔。如`data=[1,2,3,4,5]`


|  函数  |   说明   |
| :--: | :-----: |
| s.append(x)  |   在列表s的末尾添加元素x|
|  s.pop(i)   | 删除并返回s中索引为i的元素 |
|  s.remove(x)   | 删除s中的第一个x元素  |

## 字典
- 用于存储键值对，效率极高,可以添加、删除、修改键值对。如`color={'red':1,'blue':2}`
- 字典中的键是独一无二的，即使在同一个字典里，也不允许任何两个键值对相同

```python
# 遍历字典的key&value
out = []
for key in data.keys():
    str1 = key + "=" + data[key]
    out.append(str1)
print('&'.join(out))
out1 = []
for key,value in data.items():
#for (key,value) in data.items():
    str2 = key + "=" + value
    out1.append(str2)
print('&'.join(out1))
# 遍历字典的value
for value in data.values():
    print(value)
```

### 在字典中嵌套列表
```python
import json
data = {'kvmlist':[{'name':'vm01','status':'0'}]}
print(data)
data1 = {'name':'vm02','status':'1'}
list1 = data['kvmlist']
list1.append(data1)
data['kvmlist']=list1
print(data)
json = json.dumps(data)
print(json)
```
```python
{'kvmlist': [{'name': 'vm01', 'status': '0'}]}
{'kvmlist': [{'name': 'vm01', 'status': '0'}, {'name': 'vm02', 'status': '1'}]}
{"kvmlist": [{"name": "vm01", "status": "0"}, {"name": "vm02", "status": "1"}]}
```