# 针对重要业务的数据检查以及通知

## 开发
*  了解和安装python, pip。
*  安装依赖 pip install -r requirements.txt。
*  configs目录下配置数据库连接以及企业微信机器人的webhook地址。复制x_example.json, 编辑内容，重命名去掉example。
*  rules下添加数据检查业务。
*  业务拓展示例代码,mysql数据库中有用户表user, user表有id, name, phone字段，检索user表中phone为null的数据发出通知 
```python
from rules.base_rule import base_rule
class example_rule(base_rule):
    def __init__(self):
        sql = """
select id, name, phone from user where phone is null
"""
        super().__init__(
            db_name='test', #使用db_config中的数据库连接名  
            sql=sql, #异常业务数据查询语句
            general_error="没有手机号的异常数据{}组，详细情况如下：\n", #异常数据总提示
            detail_error_prefix="用户ID{}，姓名{}", #异常数据明细
            wechat_bot = 'test', #指定发送的机器人，使用wechat_bot中的机器人名
            frequency = , #每x次运行会执行一次本检查任务，假设主任务定时每分钟执行一次，那么这里代表每x分钟执行一次本检查
        )
```
*  调试运行: python main.py
## 部署
Python环境镜像，定时运行main.py