from models.customer import Customer
from repositories.customer_repository import CustomerRepository
from rich.console import Console

from utility import loading

class CustomerService:
    def __init__(self, console: Console):
        self.console = console
        self.repository = CustomerRepository()

    def create_customer(self):
        first_name = input("Imię: ")
        second_name = input("Nazwisko: ")
        age = input("Wiek: ")
        customer = Customer(first_name, second_name, age)
        customers = self.repository.read_all()
        customers.append(customer.to_dict())
        self.repository.save_all(customers)
        self.console.print("Dodano nowego klienta!", style="success")

    def show_all_customers(self):
        customers = self.repository.read_all()
        if not customers:
            self.console.print("Brak klientów w bazie danych.", style="error")
            return

        self.console.print("--- Lista klientów ---")
        for customer_data in customers:
            customer = Customer.from_dict(customer_data)
            self.console.print(f"{customer.first_name} {customer.second_name}, Wiek: {customer.age}")
    
    def delete_customer(self):
        first_name = input("Imię klienta do usunięcia: ")
        second_name = input("Nazwisko klienta do usunięcia: ")
        customers = self.repository.read_all()
        updated_customers = [
            c for c in customers if c['first_name'] != first_name or c['second_name'] != second_name
        ]

        if len(updated_customers) < len(customers):
            self.repository.save_all(updated_customers)
            self.console.print(f"Klient {first_name} {second_name} został usunięty.", style="success")
        else:
            self.console.print(f"Nie znaleziono klienta: {first_name} {second_name}", style="error")

    def update_customer(self):
        first_name = input("Imię klienta do edycji: ")
        second_name = input("Nazwisko klienta do edycji: ")
        customers = self.repository.read_all()

        for customer in customers:
            if customer['first_name'] == first_name and customer['second_name'] == second_name:
                self.console.print(f"Znaleziono klienta: {first_name} {second_name}")
                print("Wybierz, które dane chcesz zmienić:")
                print("1 - Imię")
                print("2 - Nazwisko")
                print("3 - Wiek")

                choice = input("Twój wybór: ")
                if choice == "1":
                    customer['first_name'] = input("Nowe imię: ")
                elif choice == "2":
                    customer['second_name'] = input("Nowe nazwisko: ")
                elif choice == "3":
                    customer['age'] = input("Nowy wiek: ")
                else:
                    self.console.print("Nieprawidłowy wybór!", style="error")
                    return

                self.repository.save_all(customers)
                self.console.print("Dane klienta zostały zaktualizowane.", style="success")
                return

        self.console.print(f"Nie znaleziono klienta: {first_name} {second_name}", style="error")

    def customer_menu(self):
        while True:
            print("\n➕ 1 - Stwórz nowego klienta ➕")
            print("2 - ➖ Usuń klienta ➖")
            print("3 - 📜 Wyświetl listę klientów 📜")
            print("4 - 📝 Edytuj dane klienta 📝")
            print("5 - 🔙 Wróć do głównego menu 🔙")

            choice = input("Twój wybór: ")

            match choice:
                case "1":
                    self.create_customer()
                case "2":
                    self.delete_customer()
                case "3":
                    self.show_all_customers()
                case "4":
                    self.update_customer()
                case "5":
                    loading()
                    break
                case _:
                    print("Nieprawidłowa wartość! Wybierz liczbę z zakresu 1-5.")
