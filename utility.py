from rich.progress import track
import time

def loading():
    for i in track(range(2), description="Loading..."):
        time.sleep(0.5)

