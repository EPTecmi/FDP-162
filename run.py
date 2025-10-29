import time
from watchdog.observers import Observer
from event_handler import MyEventHandler # Import your custom event handler

path_to_watch = '.'  # Monitor the current directory, or specify a different path

if __name__ == "__main__":
    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path_to_watch, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join() 