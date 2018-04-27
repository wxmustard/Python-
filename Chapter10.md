# OOP

## 类 `class`

```python
class Person:
    # 构造函数，方法的第一hj个参数必须是self
    def __init__(self, name ='', age = 0):
        # 通常 _name表示变量 __age表示私有变量 name表示方法 
        self._name = name
        self._age = age
    def __str__(self):
        return "Person(%s ,%d)" % (self._name, self._age)
    def __repr__(self):
        return str(self)
    def display(self):
        print(str(self))
    
```

- 使用装饰器来完成设置和获取函数

```python
@property  # 获取函数
def age(self):
    return self._age
@age.setter # 设置函数
def age(self, age):
    self._age = age 
# 直接使用p.age = 18 即可完成变量的赋值
```

- 继承

```python
class teacher(Person):
    # pass表示什么都不做
    pass
class student(Person):
    # 重写函数
    def __repr__(self):
        return "student(%s ,%d)" % (self._name, self._age)
```



