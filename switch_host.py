import config # User provided config.py file
import requests
import time
import json

current_server = "main"

while True:
    try:
        r = requests.get("http://" + config.main_ip, timeout=1)
        server_up = r.status_code == 200
    except:
        server_up = False

    if not server_up and current_server == "main":
        print("Switching to backup")
        for url in config.api_urls:
            r = requests.patch(url, headers=config.headers, data=json.dumps({"content":config.backup_ip}))
        current_server = "backup"

    elif server_up and current_server == "backup":
        print("Switching to main")
        for url in config.api_urls:
            r = requests.patch(url, headers=config.headers, data=json.dumps({"content":config.main_ip}))
        current_server = "main"
    
    time.sleep(1)
