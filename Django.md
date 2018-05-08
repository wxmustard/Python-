# 企业级开发框架-Django

## 数据库操作

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



