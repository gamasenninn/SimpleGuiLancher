import time
import random

messages = ["Hello", "World", "Python", "Coding", "Subprocess", "Random"]

for _ in range(10):
    try:
        print(random.choice(messages), flush=True)
        time.sleep(1)
    except Exception as e:
        print(f"Error: {e}", flush=True)
