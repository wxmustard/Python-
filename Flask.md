# 快速建站的微框架-Flask
## 安装Flask(Linux)

```bash
sudo pip3 install Flask
sudo pip3 install sqlalchemy
# sqlalchemy是一个实现了ORM数据库模型的Python库
sudo pip3 install flask-wtf 
# WTForm是一个简化HTML表单处理的Python库,flask-wtf提供了对WTForm的安装
```

## 实现

```python
# 引入包
from flask import Flask
# 建立一个Flask的实体app
app = Flask(__name__)

# 模板渲染
from flask import render_template
# 一个函数可以通过多个route()装饰器绑定到多个URL上
@app.route('/hello')
# 在路径中添加变量,分为两步,一是在装饰器中使用<variable_name>的方式声明,二是在所映射的函数的参数中声明,两次声明的变量名必须一致.
@app.route('/hello/<name>')
def hello(name=None):
    # render_template加载模板文件及参数,只需要指定模板(html)名称即可,Flask会自动在/templates文件夹下寻找
    return render_template('hello.html',name=name)

# 重定向与错误处理
from flask import abort,redirect,render_template
# 自定义错误处理器(Http定义了标准的返回错误代码表,大于等于400的代码都是错误)
@app.errorhandler(400)
def bad_request(error):
    return render_template('bad_request.html'),400
@app.route('/')
def index():
    # 重定向到check页面
    return redirect('/check')

@app.route('/check')
def f_check():
    #即刻返回400错误给客户端
    abort(400) # abort()用于中止一个请求并返回错误
    
# 当本模块被直接启动时才会运行其作用域中的代码
if __name__ == "__main__":
    app.run() #进入Flask消息循环,不要在本句后写任何代码,app.run()会一直执行
```

- 在路径中声明变量时还可以指定类型:

| 映射类型 | 说明                                             |
| -------- | ------------------------------------------------ |
| int      | 接受整数型变量 @app.route('/add/< int:number >') |
| float    | 接受浮点型变量                                   |
| path     | 默认方式,接受路径字符串                          |

- 路径中`/`的疑问?

  在URL中,`/`被认为是路径分隔符,当`/`在URL开头时表示这是一个绝对路径,在中间时表示这是一个隔离路径的层级,在后面时即可以访问到有`/`的路径,也可以访问到无`/`的路径.

| 声明                   | 举例                     | 是否可以访问 |
| ---------------------- | ------------------------ | ------------ |
| @app.route('/school/') | http://localhost/school  | 可以         |
|                        | http://localhost/school/ | 可以         |
| @app.route('/school')  | http://localhost/school  | 可以         |
|                        | http://localhost/school/ | 不可以       |

- HTTP方法绑定

```python
# 指定HTTP访问方式
from flask import request
# 如果不导入request会报错
@app.route('/SendMessage',methods=['GET','POST'])
def Message():
    if request.method == "POST":
        print("POST")
    else:
        print("GET")
    return render_template('hello.html')
```

如果出现`ValueError: View function did not return a response`错误,说明代码缩进有问题或者是返回值存在问题.

```python
# 根据访问方式的不同将同一个URL映射到不同的函数中
@app.route('/Message', methods=[ 'POST'])
def do_send():
    print("This is for POST methods")
	
@app.route('/Message', methods=['GET'])
def show_the_send_form():
    print("This is for GET methods")
```

- 路由地址反向生成

```python
from flask import url_for
with app.test_request_context():
    print(url_for('do_send'))
    print(url_for('hello'))
    print(url_for('hello',name='mustard'))
    
# 以下是输出
/Message
/hello
/hello/mustard
# flask中的test_request_context()方法是为了告诉解释器在其作用域中的代码模拟一个HTTP请求上下文
```

## Jinja2模板

```html
{{输出变量名或表达式}}
{%逻辑控制,如循环迭代等%}
{#注释#}
```

