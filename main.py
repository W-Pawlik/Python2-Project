import time
import random
import os
from dotenv import load_dotenv, find_dotenv
import pprint
from pymongo import MongoClient

load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://wojtekpawlik17:{password}@pharmacyproducts.7r8kbft.mongodb.net/?retryWrites=true&w=majority&appName=PharmacyProducts"

client = MongoClient(connection_string)
products_db = client.PharmacyProducts
collections = products_db.list_collection_names()
print(collections)
collection = products_db.Products

def insert_product_doc():
    product_document = {
        "name": input("Wpisz nazwe leku: "),
        "price": input("Wpisz cene leku: ")
    }
    inserted_id = collection.insert_one(product_document).inserted_id
    print(inserted_id)

insert_product_doc()

printer = pprint.PrettyPrinter()

def print_products():
    products = collection.find()

    for product in products:
        printer.pprint(product)

print_products()

# Napisac logike dla id(generowanie id na podstawie wymyslonego algorytmu albo z biblioteki). Get i set. jezeli id nowego obiektu jest reowne innemu(iteracja przez list), to wygeneruj inne id
# Dane będą przetrzymywane w plikach tekstowych
# 3 opcja aplikacji- pomocnik sprzedaży. 1 odczyt danych z pliku tekstowego. 2 użytkownik dodaje produkt wpisując jego nazwe oraz ilość. 3 opcja usunięcia dodanego produktu. 4 Przleiczenie całkowietego kosztu zakupów. Do tegop użyję operatorów. osbługa błędów. 


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

class ProductsServices:
    def products_menu(self):
        while True:
            print("\n1- Dodaj produkt do bazy danych")
            print("2- Wyswietl liste produktow")
            print("3- Edytuj produkt")
            print("4- Usun produkt z bazy danych")
            print("5- Wroc do glwonego menu")
            
            choice = input("Twoj wybor: ")
            print("\n")

            match choice:
                case "1":
                    print("Dodaj")
                case "2":
                    print("Wyswietl")
                case "3":
                    print("Edytuj")
                case "4":
                    print("Usun")
                case "5":
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
                    print("\n-----Obsluga klientow-----")
                    product_service = ProductsServices()
                    product_service.products_menu()
                case "3":
                    print("Do zobaczenia!")
                    break
                case _:
                    print("Nieprawidlowa wartosc")

if __name__ == '__main__':
    app = app()
    app.start()
