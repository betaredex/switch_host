import config
import requests
import time

current_server = "main"

while True:
    try:
        r = requests.get("http://" + config.main_ip, timeout=1)
        server_up = r.status_code == 200
    except Timeout:
        server_up = False

    if not server_up and current_server == main:
        r = requests.patch(config.api_url_1, headers=config.headers, data={"content":config.backup_ip})
        r = requests.patch(config.api_url_2, headers=config.headers, data={"content":config.backup_ip})
        current_server = backup
    elif server_up and current_server == backup:
        r = requests.patch(config.api_url_1, headers=config.headers, data={"content":config.main_ip})
        r = requests.patch(config.api_url_2, headers=config.headers, data={"content":config.main_ip})
    
    time.sleep(1)
