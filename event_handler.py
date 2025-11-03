import sys
import subprocess
from watchdog.events import FileSystemEventHandler

script = "tema-9/class.py"

class MyEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print(f"File modified: {event.src_path}. Running script...")
            # Replace 'your_script.py' with the actual script you want to run
            subprocess.run(['python', script]) 

    def on_created(self, event):
        if not event.is_directory:
            print(f"File created: {event.src_path}. Running script...")
            subprocess.run(['python', script])

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"File deleted: {event.src_path}. Running script...")
            subprocess.run(['python', script])

    def on_moved(self, event):
        if not event.is_directory:
            print(f"File moved: from {event.src_path} to {event.dest_path}. Running script...")
            subprocess.run(['python', script])