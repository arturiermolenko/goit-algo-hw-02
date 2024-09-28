import random
import time
from queue import Queue


queue = Queue()


def generate_request():
    verbs = [
        "Check", "Update", "Repair", "Install", "Replace",
        "Clean", "Configure", "Troubleshoot", "Test", "Upgrade"
]
    nouns = [
        "Computer", "Printer", "Network", "Software", "Hardware",
        "Server", "Device", "Monitor", "Cable", "System"
]
    request = f"{random.choice(verbs)} {random.choice(nouns)} - {random.randint(100000, 999999)}"
    queue.put(request)
    print(f"The request {request} wass added to queue!")


def process_request():
    if queue:
        request = queue.get()
        print(f"The request {request} was processed!")
    else:
        print("The queue is empty!")


while True:
    for _ in range(random.randint(1, 3)):
        generate_request()
        time.sleep(1)
    for _ in range(random.randint(1, 3)):
        process_request()
        time.sleep(1) 
