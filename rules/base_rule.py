from utils.db_connector import get_db_connection
from utils.notification_sender import send_to_wechat
class base_rule:
    def __init__(self, db_name = 'iuap', sql = '', general_error = '', detail_error_prefix = '', wechat_bot = 'iuap', frequency = 60):
        self.db_name = db_name
        self.sql = sql
        self.general_error = general_error
        self.detail_error_prefix = detail_error_prefix
        self.wechat_bot = wechat_bot
        self.frequency = frequency
    def get_db_connection(self):
        # 假设这个方法使用 db_name 来获取数据库连接
        return get_db_connection(self.db_name)
    def validate(self):
        if self.sql == '':
            return '无检验内容', 0
        db_connection = self.get_db_connection()
        try:
            cursor = db_connection.cursor()
            cursor.execute(self.sql)
            results = cursor.fetchall()
            if len(results) > 0:
                message = self.general_error.format(len(results))
                details = []
                for result in results:
                    details.append(self.detail_error_prefix.format(*result))
                message += "\n".join(details)
            else:
                message = "所有数据检查均正常"
            return message, len(results)
        finally:
            db_connection.close()
    def execute(self, execution_times):
        if (execution_times % self.frequency == 0):
            result_message, items_found = self.validate()
            if items_found > 0:  # 如果找到不符合条件的项
                send_to_wechat(self.wechat_bot, result_message)