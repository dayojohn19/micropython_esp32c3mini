Shortcut	Function
Ctrl + C	stop running program
Ctrl + D	soft reboot (restart MicroPython)
Ctrl + A	enter raw REPL
Ctrl + B	exit raw REPL
Ctrl + E	paste mode
Ctrl + ]	exit mpremote


# mpremote commands (quick reference)

This file collects common `mpremote` commands for working with MicroPython devices (ESP32, RP2040, etc.).

> Tip: run `mpremote --help` to see the latest command list for your installed version.

---

## 1) Connect to a device

### List available serial ports

```sh
mpremote devs
```

### Connect to a specific port

```sh
mpremote connect /dev/ttyUSB0
# or using a shortcut:
mpremote u0   # (also: u1, u2, u3)
```

### Disconnect

```sh
mpremote disconnect
```

---

## Shortcut command aliases (quick keys)

These are shorthand commands that map to the full `mpremote` commands. They are especially handy when working with a single device.

```sh
# Connect to typical serial ports:
mpremote u0        # /dev/ttyUSB0 (mac/linux)
mpremote u1        # /dev/ttyUSB1 (mac/linux)
mpremote a0        # /dev/ttyACM0 (mac/linux)
mpremote c0        # COM0 (Windows)

# Common operations:
mpremote reset     # hard reset (same as "mpremote reset")
mpremote soft-reset
mpremote bootloader
mpremote devs      # list serial ports
```

---

## 2) Enter the REPL (interactive prompt)

```sh
mpremote repl
```

If you have already connected to a device in the same session, just:

```sh
mpremote repl
```

---

## 3) Soft reset (restart MicroPython without re-enumerating USB)

```sh
mpremote soft-reset
```

> Shortcut: `mpremote soft-reset` (same as the full command)

In the REPL, the same effect can be triggered by sending Ctrl‑D.

---

## 4) Hard reset (full hardware reset)

```sh
mpremote reset
```

> Shortcut: `mpremote reset` (same as the full command; also available via the `reset` shortcut key alias)

This is useful when the device becomes unresponsive or you need a full power-cycle reset.

---

## 5) Upload / run scripts on the device

### Run a local script without saving it

```sh
mpremote run main.py
```

### Copy/upload a file to the device

```sh
mpremote cp local.py :/main.py
```

### Copy a file from device to host

```sh
mpremote cp :/main.py ./main_copy.py
```

---

## 6) Filesystem commands

### List files on the device

```sh
mpremote ls
```

### Remove a file

```sh
mpremote rm /boot.py
```

### Create a directory

```sh
mpremote mkdir /mydir
```

### Mount a local directory as the device filesystem (useful for live editing)

```sh
mpremote mount . /
# then in another terminal:
mpremote repl
```

### Unmount

```sh
mpremote umount
```

---

## 7) Execute one-liners (quick snippets)

```sh
mpremote eval "print('hello')"
mpremote exec "import os; print(os.listdir())"
```

---

## 8) Other helpful shortcuts

- `mpremote devs` — list serial ports
- `mpremote version` — show mpremote version
- `mpremote bootloader` — reboot device into bootloader mode

---

## Notes

- If you have multiple devices plugged in, use `mpremote -p /dev/ttyUSB0` (or `-p COM3` on Windows) to target a specific one.
- On macOS, serial ports are usually `/dev/tty.usbserial-*` or `/dev/cu.*`.
