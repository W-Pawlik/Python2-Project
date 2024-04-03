import time
import random
import os

# Napisac logike dla id(generowanie id na podstawie wymyslonego algorytmu albo z biblioteki). Get i set. jezeli id nowego obiektu jest reowne innemu(iteracja przez list), to wygeneruj inne id
# Dane będą przetrzymywane w plikach tekstowych
# 3 opcja aplikacji- pomocnik sprzedaży. 1 odczyt danych z pliku tekstowego. 2 użytkownik dodaje produkt wpisując jego nazwe oraz ilość. 3 opcja usunięcia dodanego produktu. 4 Przleiczenie całkowietego kosztu zakupów. Do tegop użyję operatorów. osbługa błędów. 
# produkty(albo kliencie, jeszcze zobaczę) przechowywane w mongodb lub innej bazie danych


class Customer:
    def __init__(self,first_name,second_name,age,id):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.id = id


    def show_customer_details(self):
        print(f"Client{self.id}: {self.first_name} {self.second_name}, {self.age} years old")

class CustomerServices:
    customer_list = []
    def create_customer(self):
        customer_first_name = input("Imie: ")
        customer_second_name = input("Nazwisko: ")
        customer_wiek = input("wiek: ")
        customer_id = random.randint(1,100)
        new_customer = Customer(customer_first_name, customer_second_name, customer_wiek, customer_id)
        self.customer_list.append(new_customer)
    
    def show_customer_list(self):
        for customer in self.customer_list:
            customer.show_customer_details()

    def delete_customer(self):
        print("Wybierz kleinta ktorego chcesz usunac")
        customer_name = input("Wpisz imie:")
        for customer in self.customer_list:
            if(customer.first_name == customer_name):
                self.customer_list.remove(customer)
                print("Klient zosatl usuniety")
            else:
                print("Nie odnaleziono klienta w bazie danych")


    def customer_menu(self):
        while True:
            print("\n1- Stworz nowy profil klienta")
            print("2- Usun profil klienta")
            print("3- Wyswietl liste klientow")
            print("4- Wroc do glownego menu")

            choice = input("Twoj wybor: ")
            print("\n")

            match choice:
                case "1":
                    self.create_customer()
                case "2":
                    self.delete_customer()
                case "3":
                    self.show_customer_list()
                case "4":
                        print("Laduje")
                        time.sleep(1)
                        break
                case _:
                    print("Nieprawidlowa wartosc")


class app: 
      
    def start(self):
        while True:
            os.system('cls')
            print('-------Witaj w aplikacji------')
            print('\nWybierz co chcesz zrobić:')
            print('1-Obsluga klientow')
            print('2-Obsluga produktow')
            print('3-exit')

            choice = input("Twój wybór: ")
            match choice:
                case "1":
                    print("\n-----Obsluga klientow-----")
                    customer_service = CustomerServices()
                    customer_service.customer_menu()
                case "2":
                    print("2")
                case "3":
                    print("Do zobaczenia!")
                    break
                case _:
                    print("Nieprawidlowa wartosc")

if __name__ == '__main__':
    app = app()
    app.start()
