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

