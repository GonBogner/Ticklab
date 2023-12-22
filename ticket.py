import hashlib
import random
import time

class Event:
    def __init__(self, event_type, name, date, time):
        self.event_type = event_type
        self.name = name
        self.date = date
        self.time = time

class QRCodeGenerator:
    @staticmethod
    def generate_qr_code(seed):
        # Simulate QR code generation using a hash function
        sha256_hash = hashlib.sha256()
        sha256_hash.update(str(seed).encode('utf-8'))
        return sha256_hash.hexdigest()

class Ticket:
    def __init__(self, event, user):
        self.event = event
        self.user = user
        self.qr_code = None

    def generate_qr_code(self):
        # Generate a new QR code every 1 minute
        while True:
            self.qr_code = QRCodeGenerator.generate_qr_code(random.randint(1, 1000000))
            time.sleep(60)  # Sleep for 1 minute before generating a new QR code

    def scan_ticket(self, scanned_qr_code):
        if scanned_qr_code == self.qr_code:
            return f"Welcome to {self.event.name}, {self.user.username}!"
        else:
            return f"Invalid ticket for {self.event.name}."

# Example usage:
event1 = Event("Concert", "Concert A", "2023-09-15", "19:00")
user1 = User("Alice", 100)
ticket1 = Ticket(event1, user1)

# Start QR code generation in a separate thread
import threading
qr_code_thread = threading.Thread(target=ticket1.generate_qr_code)
qr_code_thread.start()

# Simulate scanning the ticket after a delay
time.sleep(90)  # Wait for 1.5 minutes
scanned_qr_code = ticket1.qr_code  # Simulate scanning the QR code
result = ticket1.scan_ticket(scanned_qr_code)
print(result)
