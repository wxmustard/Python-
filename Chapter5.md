# 函数

- 函数结构

  ```python
  def sayhi(name):
  ```

  `def` 函数头  

  `sayhi`函数名  

  `name`参数 

  `:`函数头必须以`:`为结尾

- `def`后面所有缩进的代码都是函数体

- `Python`函数的参数是按引用的方式进行传递的，而C++等是按值传递的

- 参数默认值问题：

  ```python
  def Sayhi(name,greet='hello'):
  ```

  含默认值的参数必须放在无默认值的参数后面

- 关键字参数

  ```python
  def shop(where='shop',what='patsa'):
  	print(where,what)
      
  # 使用函数
  shop(where='store')
  ```

  使用关键字函数的优点：

  - 清晰指出了参数值，提高程序的可读性
  - 关键字的参数顺序无关紧要