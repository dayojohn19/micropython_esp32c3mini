
import subprocess
import sys
import os
import time
# from pathlib import Path
# print('00')
PORT = "auto"
IGNORE_FILE = ".uploadignore"

# file = Path(sys.argv[1])
# print("FILE: ",file)
# # print(Path(sys.argv)[1])

# # Debounce - prevent multiple uploads of same file within 2 seconds
# lock_file = "/tmp/esp_upload.lock"
# print('000')
# if os.path.exists(lock_file):
#     try:
#         with open(lock_file, 'r') as f:
#             last_file, last_time = f.read().split('|')
#         if last_file == str(file) and time.time() - float(last_time) < 2:
#             print("Skipping duplicate upload (debounced)")
#             sys.exit(0)
#     except:
#         pass
# print('111')
# # Update lock file
# with open(lock_file, 'w') as f:
#     f.write(f"{str(file)}|{time.time()}")
# print('111')
# # Read ignore patterns
# ignore = set()
# if os.path.exists(IGNORE_FILE):
#     ignore = set(open(IGNORE_FILE).read().split())
# print('111')
# # Check if file should be ignored
# if any(i in str(file) for i in ignore):
#     print("Skipping", file.name, "- file is in .uploadignore")
#     sys.exit(0)
# print('111')
# print("Uploading", file.name, str(file))
# print('111')
# # Upload the file using the working method
# subprocess.run(
#     ["mpremote", "connect", PORT, "fs", "cp", str(file), ":" + str(file)]
# )
# import os
# import subprocess
# from pathlib import Path

# PORT = "auto"
# IGNORE_FILE = ".uploadignore"
# ##
# ignore = set()
# if os.path.exists(IGNORE_FILE):
#     ignore = set(open(IGNORE_FILE).read().split())

# for root, dirs, files in os.walk("."):
#     for f in files:
#         path = Path(root) / f

#         if any(i in str(path) for i in ignore):
#             continue

#         if path.suffix == ".py":
#             print("Uploading", path)
#             subprocess.run(
#                 ["mpremote", "connect", PORT, "fs", "cp", str(path), ":" + str(path)]
#             )

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
class UploadHandler(FileSystemEventHandler):
    def __init__(self, observer):
        print('Watcher initialized', flush=True)
        self.observer = observer
        self.last_uploaded = {}  # Track last upload time per file
        

    def on_modified(self, event):
        # Skip .vscode, .git, __pycache__ directories
        if any(skip in event.src_path for skip in ['.vscode', '.git', '__pycache__', '.pytest']):
            return
            
        # Only process Python files
        if not event.src_path.endswith(".py"):
            return
        
        # Debounce: check if file was uploaded within last 2 seconds
        current_time = time.time()
        if event.src_path in self.last_uploaded:
            if current_time - self.last_uploaded[event.src_path] < 2:
                return
        
        print(f"Uploading {event.src_path}...", flush=True)
        
        IGNORE_FILE = ".uploadignore"
        ignore = set()
        if os.path.exists(IGNORE_FILE):
            ignore = set(open(IGNORE_FILE).read().split())
        if any(i in str(event.src_path) for i in ignore):
            print("Skipped (in .uploadignore)", flush=True)
            return
        
        # Mark this file as uploaded now
        self.last_uploaded[event.src_path] = current_time
        
        try:
            result = subprocess.run(
                ["mpremote", "connect", PORT, "fs", "cp", str(event.src_path), ":" + os.path.basename(event.src_path)]
            )
            if result.returncode == 0:
                print("Upload successful", flush=True)
            else:
                print(f"Upload failed (code {result.returncode})", flush=True)
        except Exception as e:
            print(f"Error: {str(e)}", flush=True)
        self.observer.stop()

        # try:
        #     subprocess.run(
        #         ["mpremote", "cp", PORT, "fs", "cp", str(event.src_path), ":" + os.path.basename(event.src_path)]
        #     )            
        #       :/main.py ./main_copy.py
observer = Observer()
handler = UploadHandler(observer)
observer.schedule(handler, ".", recursive=True)
observer.start()

print("Watching for changes...", flush=True)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopping...", flush=True)
    observer.stop()

observer.join()
