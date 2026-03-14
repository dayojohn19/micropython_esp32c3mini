

print('test1')
from funcf import *

SSID = "pldt fiber deco"  
PASSWORD = "Coconutgrove420!!"
DATAS = {
    'version_url':'https://raw.githubusercontent.com/dayojohn19/micropython_esp32c3mini/refs/heads/main/version.txt',
    'time_url':'http://worldtimeapi.org/api/timezone/Asia/Manila'
         }

FILES = {'version':'version.txt'}



if connect_wifi(SSID,PASSWORD):
    print(SSID,PASSWORD)
    update_text = url_request(DATAS['version_url'])
    print(update_text)
    update_file(FILES['version'],update_text)
else:
    print("Cannot make request without WiFi........")