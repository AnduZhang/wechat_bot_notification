import json
import mysql.connector
# 可根据需要导入其他数据库连接库

def get_db_connection(db_identifier):
    config_path = 'configs/db_config.json'
    with open(config_path) as config_file:
        all_configs = json.load(config_file)
    
    if db_identifier not in all_configs:
        raise ValueError(f"Database identifier '{db_identifier}' is not defined in db_config.json")

    config = all_configs[db_identifier]
    
    if config['database_type'] == 'mysql':
        return mysql.connector.connect(
            host=config['hostname'],
            user=config['username'],
            password=config['password'],
            database=config['database'],
            port=config['port']
        )
    else:
        raise ValueError("Unsupported database type")
