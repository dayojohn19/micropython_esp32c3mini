import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

print("Scanning...")
networks = wlan.scan()

for net in networks:
    ssid = net[0].decode()          # SSID as string
    bssid = ':'.join(['%02x' % b for b in net[1]])  # MAC
    channel = net[2]
    rssi = net[3]                   # Signal strength (higher = better, e.g. -50 > -90)
    security = net[4]               # 0=open, 1=WEP, 2=WPA, etc.
    print(f"SSID: {ssid}, RSSI: {rssi} dBm, Channel: {channel}")

import network
import time

# Replace these with your actual WiFi details
SSID = "Infinix HOT 30i"      # e.g. "HomeNetwork"
PASSWORD = "YourPassword123"

def connect_wifi(ssid_val,pass_val):
    wlan = network.WLAN(network.STA_IF)  # STA_IF = station/client mode
    
    if wlan.isconnected():
        print("Already connected!")
        print("IP address:", wlan.ifconfig()[0])  # or wlan.ipconfig('addr4')
        return
    
    print("Connecting to WiFi...")
    wlan.active(True)                    # Turn on the WiFi radio
    
    # Optional: set country for regulatory compliance (helps stability)
    # network.country("PH")             # Philippines, change to your country code
    
    # Optional tweaks for some ESP32-C3 boards (if you get "Wifi Internal Error")
    # wlan.config(txpower=5)           # Lower TX power can help on tiny boards
    # wlan.config(pm=wlan.PM_NONE)     # Disable power saving if unstable
    
    wlan.connect(ssid_val, pass_val)
    
    # Wait for connection (non-blocking connect, so loop needed)
    timeout = 3  # seconds
    start = time.time()
    while not wlan.isconnected():
        if time.time() - start > timeout:
            print("Connection failed! Check SSID/password or signal.")
            wlan.active(False)
            return
        print(".", end="")
        time.sleep(0.5)
    
    print("\nConnected!")
    print("IP address:", wlan.ifconfig()[0])   # Your device's local IP
    print("Subnet:", wlan.ifconfig()[1])
    print("Gateway:", wlan.ifconfig()[2])
    print("DNS:", wlan.ifconfig()[3])
    print("RSSI (signal strength):", wlan.status('rssi'), "dBm")
    return wlan.isconnected

# Run it
def create_wifi():
    ap = network.WLAN(network.AP_IF)     # AP_IF = access point mode
    ap.active(True)
    ap.config(ssid="MyESP32", password="12345678")  # Set your name & password

    print("Access Point started")
    print("Connect to SSID: MyESP32")

def brute_force_generator(target, charset=None, max_length=None):
    """
    Faster iterative brute-force in MicroPython.
    No recursion → better speed & no stack overflow.
    Prints every attempt.
    """
    if charset is None:
        # Keep charset small if possible — biggest speed factor!
        charset = "abcdefghijklmnopqrstuvwxyz0123456789!@#"

    charset_list = list(charset)          # faster access than string indexing
    n_chars = len(charset_list)

    if max_length is None:
        max_length = len(target) + 2

    print("Starting brute-force (iterative) for:", target)
    print("Charset size:", n_chars, "chars")
    print("Trying up to length:", max_length)

    import time
    start = time.ticks_ms()

    for length in range(1, max_length + 1):
        print("\nTrying length", length, "... ({:,} combos)".format(n_chars ** length))

        # Current combination (as list of indices into charset)
        indices = [0] * length
        is_connected = False
        while not is_connected:
            # Build current string
            attempt = ''.join(charset_list[i] for i in indices)

            print(attempt)                      # every attempt
            # is_connected = connect_wifi(SSID,attempt)

            if attempt == target:
                end = time.ticks_ms()
                print("\nFOUND after", time.ticks_diff(end, start), "ms")
                return attempt

            # Increment like an odometer (from right to left)
            pos = length - 1
            while pos >= 0:
                indices[pos] += 1
                if indices[pos] < n_chars:
                    break
                indices[pos] = 0
                pos -= 1

            if pos < 0:
                # All combinations for this length done
                break

    end = time.ticks_ms()
    print("\nNot found. Total time:", time.ticks_diff(end, start), "ms")
    return None



# ────────────────────────────────────────────────
# Usage example (use short target for testing!)
# if __name__ == "__main__":
#     # For real speed test — keep short!
#     result = brute_force_generator("lea@0606")

#     if result:
#         print("Success →", result)
#     else:
#         print("Not found")
# ────────────────────────────────────────────────
# # Example usage (run this on your board via Thonny REPL or main.py)

# if __name__ == "__main__":
#     target = "lea@606"   # your example (7 chars → will take extremely long!)

#     # For quick testing only – use very short target!
#     # result = brute_force_generator("ab1", max_length=4)

#     result = brute_force_generator(target, max_length=7)

#     if result:
#         print("Success! Password:", result)
#     else:
#         print("Not found.")