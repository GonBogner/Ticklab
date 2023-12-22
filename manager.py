import hashlib
import random
import threading
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
        sha256_hash = hashlib.sha256()
        sha256_hash.update(str(seed).encode('utf-8'))
        return sha256_hash.hexdigest()

class User:
    def __init__(self, username, initial_balance=0):
        self.username = username
        self.wallet = initial_balance
        self.tickets = []

    def buy_ticket(self, event, ticket_price):
        if self.wallet >= ticket_price:
            self.wallet -= ticket_price
            ticket = Ticket(event, self)
            self.tickets.append(ticket)
            return f"{self.username} has purchased a ticket for {event.name}"
        else:
            return f"Insufficient funds to buy a ticket for {event.name}"

    def view_wallet_balance(self):
        return f"{self.username}'s wallet balance: ${self.wallet:.2f}"

    def view_tickets(self):
        if not self.tickets:
            return f"{self.username} has no tickets."
        else:
            ticket_names = [ticket.event.name for ticket in self.tickets]
            return f"{self.username}'s tickets: {', '.join(ticket_names)}"

class Ticket:
    def __init__(self, event, user):
        self.event = event
        self.user = user
        self.qr_code = None

    def generate_qr_code(self):
        while True:
            self.qr_code = QRCodeGenerator.generate_qr_code(random.randint(1, 1000000))
            time.sleep(60)

    def scan_ticket(self, scanned_qr_code):
        if scanned_qr_code == self.qr_code:
            return f"Welcome to {self.event.name}, {self.user.username}!"
        else:
            return f"Invalid ticket for {self.event.name}"

class TicketManager:
    def __init__(self):
        self.events = []
        self.users = []

    def create_event(self, event_type, name, date, time):
        event = Event(event_type, name, date, time)
        self.events.append(event)
        return event

    def create_user(self, username, initial_balance=0):
        user = User(username, initial_balance)
        self.users.append(user)
        return user

    def buy_ticket(self, user, event, ticket_price):
        return user.buy_ticket(event, ticket_price)

    def scan_ticket(self, user, event, scanned_qr_code):
        for ticket in user.tickets:
            if ticket.event == event:
                return ticket.scan_ticket(scanned_qr_code)
        return f"{user.username} does not have a ticket for {event.name}"

# Example usage:
ticket_manager = TicketManager()
event1 = ticket_manager.create_event("Concert", "Concert A", "2023-09-15", "19:00")
user1 = ticket_manager.create_user("Alice", 100)

# Start QR code generation in a separate thread for user1's ticket
qr_code_thread = threading.Thread(target=user1.tickets[0].generate_qr_code)
qr_code_thread.start()

# Simulate scanning the ticket after a delay
time.sleep(90)  # Wait for 1.5 minutes
scanned_qr_code = user1.tickets[0].qr_code  # Simulate scanning the QR code
result = ticket_manager.scan_ticket(user1, event1, scanned_qr_code)
print(result)
