class User:
    def __init__(self, username, initial_balance=0):
        self.username = username
        self.wallet = initial_balance
        self.tickets = []

    def buy_ticket(self, event_name, ticket_price):
        if self.wallet >= ticket_price:
            self.wallet -= ticket_price
            self.tickets.append(event_name)
            return f"{self.username} has purchased a ticket for {event_name}"
        else:
            return f"Insufficient funds to buy a ticket for {event_name}"

    def view_wallet_balance(self):
        return f"{self.username}'s wallet balance: ${self.wallet:.2f}"

    def view_tickets(self):
        if not self.tickets:
            return f"{self.username} has no tickets."
        else:
            return f"{self.username}'s tickets: {', '.join(self.tickets)}"

    def perform_action(self, event_name, action):
        if event_name in self.tickets:
            return f"{self.username} is {action} at the {event_name}"
        else:
            return f"{self.username} does not have a ticket for {event_name}"

# Example usage:
user1 = User("Alice", 100)
user2 = User("Bob", 50)

print(user1.buy_ticket("Concert A", 30))
print(user1.buy_ticket("Sports Event B", 40))
print(user1.view_wallet_balance())
print(user1.view_tickets())
print(user1.perform_action("Concert A", "dancing"))
print(user1.perform_action("Sports Event B", "cheering"))

print(user2.buy_ticket("Concert X", 20))
print(user2.view_wallet_balance())
print(user2.view_tickets())
print(user2.perform_action("Concert X", "singing"))
