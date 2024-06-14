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
            frequency = 60, #每x次运行会执行一次本检查任务，假设主任务定时每分钟执行一次，那么这里代表每x分钟执行一次本检查
        )