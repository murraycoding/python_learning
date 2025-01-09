import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from POs_Reader import *

# Function to run when a new file is added
def on_created(event):
    if event.is_directory:
        return
    print(f"New file created: {event.src_path}")
    POs_Reader()

class Watcher:
    def __init__(self, folder_to_watch):
        self.folder_to_watch = folder_to_watch
        self.event_handler = FileSystemEventHandler()
        self.event_handler.on_created = on_created

    def start(self):
        observer = Observer()
        observer.schedule(self.event_handler, self.folder_to_watch, recursive=False)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

# Specify the folder you want to monitor
folder_to_watch = "/Users/jmutcap/OneDrive - CUEBITZ LLC/Walmart 2025/Walmart POs"
watcher = Watcher(folder_to_watch)
watcher.start()

