# 企业级开发框架-Django

## 开发环境

>在开发Python应用程序的时候，系统安装的Python3只有一个版本：3.4。所有第三方的包都会被`pip`安装到Python3的`site-packages`目录下。
>
>如果我们要同时开发多个应用程序，那这些应用程序都会共用一个Python，就是安装在系统的Python 3。如果应用A需要jinja 2.7，而应用B需要jinja 2.6怎么办？
>
>这种情况下，每个应用可能需要各自拥有一套“独立”的Python运行环境。virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境.

- 安装`virtualenv`

  ```bash
  sudo pip install virtualenv virtualenvwrapper
  ```

- 更改`.zshrc`

  ```bash
  export WORKON_HOME=/home/mustard/.virtualenvs
  export PROJECT_HOME=/home/mustard/workspace
  export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python
  source /usr/local/bin/virtualenvwrapper.sh
  # 使更改生效
  source .zshrc
  ```

- 创建一个新的项目

  ```bash
  # 创建项目目录
  mkdir myproject
  cd myproject/
  # 创建一个独立的Python运行环境，命名为venv
  virtualenv --no-site-packages venv
  # virtualenv命令是创建一个独立的Python运行环境
  # --no-site-packages参数是创建一个干净的不包含第三方包的Python运行环境
  
  #进入venv环境
  source venv/bin/activate
  # 此时可以使用pip install等命令了
  ```

## Django

- 安装`bpython`，添加自动补全功能

  ```python
  # 进入venv环境后
  # 1.升级pip
  pip install --upgrade pip
  # 2.安装Django
  pip install Django
  # 3.安装bpython
  pip install bpython
  # 进入bpython，查询django版本
  >>> import django
  >>> django.VERSION
  (1, 11, 7, 'final', 0)
  ```


### `Django`基本命令

- ```bash
  # 创建新项目 mysite
  django-admin startproject mysite
  # 创建新应用（app），learn
  python manage.py startapp learn
  # 将新定义的app加到settings.py中的INSTALL_APPS中
  # 修改mysite/mysite/settings.py
  INSTALLED_APPS = (
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
   
      'learn',
  )
  # 新建的 app 如果不加到 INSTALL_APPS 中的话, django 就不能自动找到app中的模板文件(app-name/templates/下的文件)和静态文件(app-name/static/中的文件)
  ```

- `requirements.txt`

  > python项目中必须包含一个 requirements.txt 文件，用于记录所有依赖包及其精确的版本号。以便新环境部署。

  ```bash
  # 生成requirements.txt
  pip3 freeze >requirements.txt
  # 部署环境
  pip3 install -r requirements.txt
  ```



##  使用Django Rest framework框架

### 基础设置

- 下载框架

```bash
pip3 install djangorestframework
pip3 install pygments
```

- 基础配置

  - 将app添加至项目中

  ```python
  # 将'vm.apps.VmConfig'添加到kvm/settings.py中
  INSTALLED_APPS = [
      'vm.apps.VmConfig',
  ]
  ```

  - 修改项目的url

  ```python
  # 打开kvm/urls.py,将以下语句添加进去
  # 提示：vm/urls.py需要自行创建
  from django.conf.urls import url , include
  urlpatterns = [
      path('admin/', admin.site.urls),
      url(r'^',include('vm.urls'))
  ]
  ```

  - 创建`vm/urls.py`

  ```python
  # url是预先设计好的
  from django.conf.urls import url
  from vm import views
  from rest_framework.urlpatterns import format_suffix_patterns
  urlpatterns = [
      url(r'^v1/vps/$',views.kvm_list),
      url(r'^v1/vps/kvmname/(?P<name>[a-zA-Z0-9]+)/$',views.kvm),
  ]
  urlpatterns = format_suffix_patterns(urlpatterns)
  ```

### 数据库操作

- 配置数据库文件

```python
# 修改django项目的setting.py文件
DATABASES = {
        'default': {
       # 'ENGINE': 'django.db.backends.sqlite3',
       # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 's3test',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'127.0.0.1',
        'PORT':'3306',
    }
}
```

- 编写模型类

```python
# 编写项目app的models.py 文件,如
from django.db import models

# Create your models here.
class buckets(models.Model):
    id = models.AutoField(primary_key = True)
    bucket_name = models.CharField(max_length = 32)
    create_id = models.CharField(max_length =8)
    create_at = models.DateTimeField(auto_now_add= True)
    objects = models.Manager() 
class users(models.Model):
    # 参数中包含max_length为可变长度（varchar类型），没有参数的为定长（char类型）
    id = models.AutoField(primary_key = True)
    access_key = models.CharField(max_length = 64)
    access_secret = models.CharField(max_length = 64)
    create_id = models.CharField(max_length =8)
    # 如果在数据中已有数据的基础上需要更改数据库设计，需要先清空表中数据，并为新增字段添加默认值
    server_address = models.CharField(max_length = 64,default='')
    # auto_now 自动创建---无论添加或修改，都是当前操作的时间 ,auto_now_add 自动创建---永远是创建时的时间
    create_at = models.DateTimeField(auto_now_add= True)
    # null=True数据库中的字段允许为空，但是django会自动检测数据不允许为空值，需要添加blank=True才可以
    update_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    objects = models.Manager() 
```

- 将新建的`models`同步至数据库

```cmd
# 查询当前数据库与本地的models之间的差异,生成合并代码
python manage.py makemigrations
# 将何必代码导入数据库
python manage.py migrate
```

### 数据库的基本操作(`views.py`)

- 增

```python
from s3.models import buckets,users,shares
bucket = buckets(bucket_name ='mytest',create_id='17721803')
bucket.save()
```

- 查

```python
from s3.models import buckets,users,shares
# 获取表中所有数据
bucket = buckets.objects.all()
# 获得表中所有数据的values
bucket = buckets.objects.all().values('id','bucket_name')
bucket1 = buckets.objects.filter().values('id','bucket_name')
# 使用values进行查询数据时将返回一个QuerySet对象，如<QuerySet [{'bucket_name': 'wxmust', 'id': 3}, {'bucket_name': 'mytest', 'id': 9}]>
# 形式为[{}]，列表中包含字典的形式
bucket1[0]['id']
# 获得单条数据
bucket = buckets.objects.get(id = 1)
bucket = buckets.objects.filter(id = 1)
```

- 删

```python
from s3.models import buckets,users,shares
# 删除单条数据
buckets.objects.get(id=1).delete()
# 删除多条符合条件的数据
buckets.objects.filter(id=1).delete()
# 删除所有数据
buckets.objects.all().delete()
```

- 改

```python
from s3.models import buckets,users,shares
# 1: 获得单条数据信息
# 2: 修改数据信息
# 3: save()
user = users.objects.get(create_id='17721803')
user.access_key = 'wxmust'
user.access_secret = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
user.save()
```

### 响应头Response

#### 返回状态码

- 使用方法：

```python
 return Response(status=status.HTTP_204_NO_CONTENT)
```

- 状态码列表：

```python
HTTP_100_CONTINUE = 100
HTTP_101_SWITCHING_PROTOCOLS = 101
HTTP_200_OK = 200
HTTP_201_CREATED = 201
HTTP_202_ACCEPTED = 202
HTTP_203_NON_AUTHORITATIVE_INFORMATION = 203
HTTP_204_NO_CONTENT = 204
HTTP_205_RESET_CONTENT = 205
HTTP_206_PARTIAL_CONTENT = 206
HTTP_207_MULTI_STATUS = 207
HTTP_300_MULTIPLE_CHOICES = 300
HTTP_301_MOVED_PERMANENTLY = 301
HTTP_302_FOUND = 302
HTTP_303_SEE_OTHER = 303
HTTP_304_NOT_MODIFIED = 304
HTTP_305_USE_PROXY = 305
HTTP_306_RESERVED = 306
HTTP_307_TEMPORARY_REDIRECT = 307
HTTP_400_BAD_REQUEST = 400
HTTP_401_UNAUTHORIZED = 401
HTTP_402_PAYMENT_REQUIRED = 402
HTTP_403_FORBIDDEN = 403
HTTP_404_NOT_FOUND = 404
HTTP_405_METHOD_NOT_ALLOWED = 405
HTTP_406_NOT_ACCEPTABLE = 406
HTTP_407_PROXY_AUTHENTICATION_REQUIRED = 407
HTTP_408_REQUEST_TIMEOUT = 408
HTTP_409_CONFLICT = 409
HTTP_410_GONE = 410
HTTP_411_LENGTH_REQUIRED = 411
HTTP_412_PRECONDITION_FAILED = 412
HTTP_413_REQUEST_ENTITY_TOO_LARGE = 413
HTTP_414_REQUEST_URI_TOO_LONG = 414
HTTP_415_UNSUPPORTED_MEDIA_TYPE = 415
HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE = 416
HTTP_417_EXPECTATION_FAILED = 417
HTTP_422_UNPROCESSABLE_ENTITY = 422
HTTP_423_LOCKED = 423
HTTP_424_FAILED_DEPENDENCY = 424
HTTP_428_PRECONDITION_REQUIRED = 428
HTTP_429_TOO_MANY_REQUESTS = 429
HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE = 431
HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS = 451
HTTP_500_INTERNAL_SERVER_ERROR = 500
HTTP_501_NOT_IMPLEMENTED = 501
HTTP_502_BAD_GATEWAY = 502
HTTP_503_SERVICE_UNAVAILABLE = 503
HTTP_504_GATEWAY_TIMEOUT = 504
HTTP_505_HTTP_VERSION_NOT_SUPPORTED = 505
HTTP_507_INSUFFICIENT_STORAGE = 507
HTTP_511_NETWORK_AUTHENTICATION_REQUIRED = 511
```

#### 自定义Response响应头

> 参考资料： http://www.django-rest-framework.org/api-guide/responses/#creating-responses

```python
# views.py 文件中进行自定义Response
    response = Response()
    # response = Response(status = status.HTTP_200_OK)
    response['server'] = 'SHU'
    response1['content_type'] = 'application/octet-stream'
return response
```



## Q&A

### 字典排序

- 按照字典中的`Key`排序

```python
sorted(dict.keys()) # key升序排列
sorted(dict.keys(),reverse=True) # key降序排列
```

