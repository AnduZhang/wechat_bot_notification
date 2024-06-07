from importlib import import_module
from rules.base_rule import base_rule
import os

def main():
    rules_path = 'rules'
    messages = []
    execution_times = get_execution_times()
    # 及时更新执行次数，避免并发问题
    new_execution_times = execution_times + 1
    set_execution_times(new_execution_times)
    # 动态导入并执行每个规则的 validate 方法
    for rule_file in os.listdir(rules_path):
        if rule_file.endswith('.py') and not rule_file.startswith('__'):
            rule_module_name = rule_file[:-3]  # 移除 .py 后缀
            rule_module = f'rules.{rule_module_name}'
            module = import_module(rule_module)
            # 获取类定义，而非实例
            rule_class = getattr(module, rule_module_name, None) 
            # 确保 rule_class 不是 None 并且是 base_rule 的子类
            if rule_class and issubclass(rule_class, base_rule) and rule_class is not base_rule:  
                rule_instance = rule_class()  # 创建实例
                # 假设每个 validate 方法都可以独立执行
                rule_instance.execute(execution_times)


def get_execution_times():
    try:          
        with open('execution_history.txt', 'r') as file:
            content = file.read()
            execution_times = int(content)
    except FileNotFoundError:
        execution_times = 0   
    except ValueError:
        execution_times = 0 
    return execution_times

def set_execution_times(execution_times):
    with open('execution_history.txt', 'w') as file:
        file.write(str(execution_times))
if __name__ == "__main__":
    main()