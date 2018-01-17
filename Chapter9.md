# 异常处理
- 在出现异常时，如果不捕获或以其他方式处理，`Python`会立即停止运行程序。

- 捕获所有异常
```python
try:
    # 可能会出现异常的语句
    conn.lookupByName(name)
except:
    # 如果出现异常的应对处理
    dominfo = {'message':'未找到该虚拟机，请确认虚拟机名称是否正确。'}
else:
    # 没有发生异常的情况下执行的语句
    domain = conn.lookupByName(name)
    state, maxmem, mem, cpus, cput = domain.info()
    if domain.isActive() == 0:
       status = '已关闭'
    if domain.isActive() == 1:
       status = '运行中'
       dominfo = {'name':domain.name(),'UUID':domain.UUIDString(),                               'status':status,'memory':str(mem),'max memory':str(maxmem),'cpus':str(cpus)}
```

