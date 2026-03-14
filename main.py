print('testgithubedits')
from funcf import *
SSID = "pldt fiber deco"  
PASSWORD = "Coconutgrove420!!"
FILES = {
    'version.txt':{
        'v':1,
        'last_update':'',
        'url':'https://raw.githubusercontent.com/dayojohn19/micropython_esp32c3mini/refs/heads/main/version.txt'
        },
    'main.py':{
        'v':1,
        'last_update':'',
        'url':'https://raw.githubusercontent.com/dayojohn19/micropython_esp32c3mini/refs/heads/main/main.py'
    },
    'boot.py':{
        'v':1,
        'last_update':'',
        'url':'https://raw.githubusercontent.com/dayojohn19/micropython_esp32c3mini/refs/heads/main/boot.py'
    },
    'funcf.py':{
        'v':1,
        'last_update':'',
        'url':'https://raw.githubusercontent.com/dayojohn19/micropython_esp32c3mini/refs/heads/main/funcf.py'
    }
    }


if connect_wifi(SSID,PASSWORD):
    print(SSID,PASSWORD)
    version_text = url_request(FILES['version.txt']['url'])
    if version_text is not False:
        print(version_text)
    update_files(FILES)
else:
    print("Cannot make request without WiFi........")
