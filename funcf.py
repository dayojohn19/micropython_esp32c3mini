import network
import urequests
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

print("Scanning...")
for net in wlan.scan():
    print("SSID:", net[0].decode(), "RSSI:", net[3], "CH:", net[2])


def connect_wifi(ssid_val, pass_val):
    w = network.WLAN(network.STA_IF)
    if w.isconnected():
        return True
    w.active(True)
    w.connect(ssid_val, pass_val)
    t0 = time.time()
    while not w.isconnected() and time.time() - t0 < 3:
        print(".", end="")
        time.sleep(0.5)
    if w.isconnected():
        cfg = w.ifconfig()
        print("\nOK", cfg[0], cfg[1], cfg[2], cfg[3], w.status("rssi"))
        return True
    w.active(False)
    print("\nFail")
    return False


def url_request(url=None, method="GET", params=None, data=None, headers=None, retries=5, timeout=5):
    if not url:
        url = "https://httpbin.org/ip"
    if params:
        sep = "&" if "?" in url else "?"
        for k, v in params.items():
            url += sep + k + "=" + str(v)
            sep = "&"
    for a in range(retries):
        try:
            print(f"Try {a+1}: {method} {url}")
            r = urequests.post(url, data=data, headers=headers, timeout=timeout) if method.upper() == "POST" else urequests.get(url, headers=headers, timeout=timeout)
            if r.status_code == 200:
                text = r.text
                r.close()
                return text
            print("Status", r.status_code)
            r.close()
        except Exception as e:
            print("Err", e)
        time.sleep(2)
    return False

def update_file(p, c, m="w"):
    try:
        d = str(c)
        with open(p, m, encoding="utf-8") as f:
            for i in range(0, len(d), 64 * 1024):
                f.write(d[i:i + 64 * 1024])
        return True
    except Exception as e:
        print("upddd err", e)
        return False