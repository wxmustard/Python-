# Q&A

## `ImportError: cannot import name 'Minio'`

`python`在导包过程中出现了以上错误，可以从三个方面分析解决问题：

- 检查导包的`py`文件是否与包的名字相同，如果相同的话会与默认的包发生冲突

- 检查是否已经下载第三方库

```bash
  sudo pip3 list
  sudo pip3 install ***
```

- 使用`virtualenv`环境

```bash
  virtualenv venv
  source venv/bin/activate
```

  

## 依赖文档

- Python项目中必须包含一个 requirements.txt 文件，用于记录所有依赖包及其精确的版本号。以便新环境部署。

```cmd
pip freeze > requirements.txt # 生成requirements.txt
pip install -r requirements.txt # 从requirements.txt安装依赖
```



