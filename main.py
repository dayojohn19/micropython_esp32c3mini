

print('test1')
from funcf import *
# Replace these with dyour actual WiFi details333
SSID = "pldt fiber deco"      # e.g. "HomeNetwork"
PASSWORD = "Coconutgrove420!!"
DATAS = {'version_url':'https://raw.githubusercontent.com/dayojohn19/micropython_esp32c3mini/refs/heads/main/main.py',
         'time_url':'http://worldtimeapi.org/api/timezone/Asia/Manila'
         }

FILES = {'main':'version.txt'}



if connect_wifi(SSID,PASSWORD):
    print(SSID,PASSWORD)
    update_text = url_request(DATAS['version_url'])
    print(update_text)
    update_file_data = update_file(FILES['main'],update_text)

#

else:
    print("Cannot make request without WiFi........")