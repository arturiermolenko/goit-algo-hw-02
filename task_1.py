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
    request_id = random.randint(100000, 999999)
    request = f"{random.choice(verbs)} {random.choice(nouns)} - {request_id}"
    queue.put(request)
    
    print(f"The request {request} was added to the queue!")

def process_request():
    if not queue.empty():
        request = queue.get()
        print(f"The request {request} was processed!")
    else:
        print("The queue is empty!")

def main():
    try:
        while True:
            for _ in range(random.randint(1, 3)):
                generate_request()
                time.sleep(1)
            
            for _ in range(random.randint(1, 3)):
                process_request()
                time.sleep(1)

            print(f"Current queue size: {queue.qsize()}\n")
    except KeyboardInterrupt:
        print("\nProgram terminated. Thank you!")

if __name__ == "__main__":
    main()

