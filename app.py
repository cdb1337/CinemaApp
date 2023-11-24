from database import CinemaDatabase

class CinemaAPI:
    def __init__(self):
        self.database = CinemaDatabase()

    def display_menu(self):
        print("\n===== Cinema Ticketing App Menu =====")
        print("1. Buy Ticket")
        print("2. Change Seat")
        print("3. View Ticket")
        print("4. Delete Ticket")
        print("5. Display All Tickets")
        print("6. Quit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter the number of your choice: ")

            if choice == "1":
                name = input("Enter your name: ")
                age = int(input("Enter your age: "))
                seat = input("Enter the seat: ")
                print(self.buy_ticket(name, age, seat))

            elif choice == "2":
                old_seat = input("Enter the current seat: ")
                new_seat = input("Enter the new seat: ")
                print(self.change_seat(old_seat, new_seat))

            elif choice == "3":
                name = input("Enter your name: ")
                seat = input("Enter the seat: ")
                print(self.view_ticket(name, seat))

            elif choice == "4":
                name = input("Enter your name: ")
                seat = input("Enter the seat: ")
                print(self.delete_ticket(name, seat))

            elif choice == "5":
                print(self.display_all_tickets())

            elif choice == "6":
                print("Quitting the application. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a valid number.")

    def buy_ticket(self, name, age, seat):
        self.database.add_ticket(seat, name, age)
        return f"Ticket purchased successfully. Name: {name}, Age: {age}, Seat: {seat}"

    def change_seat(self, old_seat, new_seat):
        return self.database.change_seat(old_seat, new_seat)

    def view_ticket(self, name, seat):
        return self.database.view_ticket(name, seat)

    def delete_ticket(self, name, seat):
        return self.database.delete_ticket(name, seat)

    def display_all_tickets(self):
        all_tickets = self.database.get_all_tickets()
        if all_tickets:
            return "All Tickets: " + ", ".join([f"Seat: {seat} ({info[0]}, {info[1]})" for seat, info in all_tickets.items()])
        else:
            return "No tickets available."

# Example usage
if __name__ == "__main__":
    cinema_app = CinemaAPI()
    cinema_app.run()