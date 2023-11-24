class CinemaDatabase:
    def __init__(self):
        self.tickets = {}  # Using a dictionary to store tickets {seat: (name, age)}

    def add_ticket(self, seat, name, age):
        self.tickets[seat] = (name, age)

    def change_seat(self, old_seat, new_seat):
        if old_seat in self.tickets:
            self.tickets[new_seat] = self.tickets.pop(old_seat)

    def view_ticket(self, name, seat):
        if seat in self.tickets and self.tickets[seat][0] == name:
            return f"Ticket Info: Name: {name}, Age: {self.tickets[seat][1]}, Seat: {seat}"
        else:
            return "Ticket not found."

    def delete_ticket(self, name, seat):
        if seat in self.tickets and self.tickets[seat][0] == name:
            del self.tickets[seat]
            return "Ticket deleted successfully."
        else:
            return "Ticket not found."

    def get_all_tickets(self):
        return self.tickets
