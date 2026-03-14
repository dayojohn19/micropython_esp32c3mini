installing packages 
mip.install("micropython-urequests")
# micropython_esp32c3mini

## to Lower the memory
mpy-cross [filename]

Erasing Flash 
`esptool  --chip esp32c3 --port /dev/tty.usbmodem101 erase_flash`

Flashing

`esptool.py \
--chip esp32c3 \
--port /dev/tty.usbmodem101 \
--baud 460800 \
write_flash -z 0x0 '/Users/nhoj/Documents/ESP 32 C3 Mini Module/firmwares/ESP32_GENERIC_C3-20251209-v1.27.0.bin'


install mpremote
pip3 install mpremote