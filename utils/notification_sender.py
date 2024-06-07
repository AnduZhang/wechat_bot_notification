import json
import requests

def send_to_wechat(wechat_bot, message):
    config_path = 'configs/wechat_bot_config.json'
    with open(config_path) as config_file:
        all_configs = json.load(config_file)
    if wechat_bot not in all_configs:
        raise ValueError(f"Wechat bot '{wechat_bot}' is not defined in wechat_bot_config.json")
    config = all_configs[wechat_bot]
    webhook_url = config['webhook_url']
    data = {"msgtype": "text", "text": {"content": message}}
    requests.post(webhook_url, json=data)