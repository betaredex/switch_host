import config
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

    print("server_up: " + str(server_up))

    if not server_up and current_server == "main":
        print("switching to backup")
        r1 = requests.patch(config.api_url_1, headers=config.headers, data=json.dumps({"content":config.backup_ip}))
        r2 = requests.patch(config.api_url_2, headers=config.headers, data=json.dumps({"content":config.backup_ip}))
        current_server = "backup"

    elif server_up and current_server == "backup":
        print("switching to main")
        r1 = requests.patch(config.api_url_1, headers=config.headers, data=json.dumps({"content":config.main_ip}))
        r2 = requests.patch(config.api_url_2, headers=config.headers, data=json.dumps({"content":config.main_ip}))
        current_server = "main"
    
    time.sleep(1)
