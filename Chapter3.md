# 编写程序

## 安装编译环境以及编写第一个`Python`程序

* **ubuntu**环境下安装`Python`编辑器`IDLE`

  ```bash
  # 查看本机python版本
  python --version
  # 安装IDLE编辑器
  sudo apt install idle-python2.7
  ```

* 使用`IDLE`编写第一个`Python`程序

  * 打开`IDLE`

  * File -->  NEW File

  * 在新弹出的窗口输入`Python`语句

    ```python
    print('Welcome to Python')
    ```

  * File --> Save  保存成 **.py**文件

* *运行方法一*

  * Run --> Run Moudle

  * 会出现一个新的窗口返回结果

    ![](https://vgy.me/K7qFeQ.png)

* *运行方法二*

  * ```python
    python welcome.py
    ```

    ![](https://vgy.me/QQp0m9.png)

## 编译源代码

> 在运行`.py`文件时会自动创建相应的`.pyc`文件，`.pyc`文件中包含目标代码，这个目标代码是一种`Python`专用的语言，计算机可以高效运行，并且`Python`程序是在虚拟机上运行的。

* 输入字符串

  ```python
  name = input('')
  # 函数input返回用户输入的字符串，name最终指向用户输入的字符串
  # 如果想获得数字，需要自行将接受的字符串转换为数字类型，使用int()，float()都可以
  ```

  ​

![](https://vgy.me/fmLgmU.png)

* 在屏幕上打印字符串

  ```python
  print('hello',end='')
  print('world')
  # print打印完自动在指定内容后添加一个换行符\n
  # 如果想在同一行输出，需要使用上述语句
  ```

* 在`python`中使用#注释

* 快捷键

|      快捷键       |     动作     |
| :------------: | :--------: |
|     Ctrl+O     | open file  |
| Ctrl+(Shift)+Z |     撤销     |
|       F5       | run moudle |
|     Ctrl+N     |  new file  |

