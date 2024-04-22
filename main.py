import time
import random
import os
from dotenv import load_dotenv, find_dotenv
import pprint
from pymongo import MongoClient
from rich.console import Console



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
            # Walidacja inputu
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


class ProductsInterface:
    def __init__(self, repository):
        self.repository = repository

    def products_menu(self):

        while True:
            print("\n1- Dodaj produkt do bazy danych")
            print("2- Wyswietl liste produktow")
            print("3- Edytuj produkt")
            print("4- Usun produkt z bazy danych")
            print("5- Znajdz konkretny lek")
            print("6- Wroc do glwonego menu")
            
            choice = input("Twoj wybor: ")
            print("\n")

            match choice:
                case "1":
                    print("Dodaj")
                    self.repository.insert_product_doc()
                case "2":
                    print("Wyswietl wszystkie produkty")
                    self.repository.print_products()
                case "3":
                    print("Edytuj")
                    name = input("Wpisz nazwe leku: ")
                    self.repository.update_product_by_name(name)
                case "4":
                    print("Usun")
                    name = input("Wpisz nazwe leku: ")
                    self.repository.delete_product_by_name(name)
                case "5":
                    print("Znajdz")
                    name = input("Wpisz nazwe leku: ")
                    self.repository.get_product_by_name(name)
                case "6":
                    print("Laduje")
                    time.sleep(1)
                    break
                case _:
                    print("Nieprawidlowa wartosc")



class ProductsRepository:
    def __init__(self, collection,printer):
        self.collection = collection
        self.printer = printer

    def insert_product_doc(self):
        product_name = input("Wpisz nazwe leku: ")
        while True:
            product_price = input("Wpisz cene leku: ")
            try:
                price = float(product_price)
                if price < 0:
                    raise ValueError("Cena nie może być ujemna!")
                
                product_document = {
                    "name": product_name,
                    "price": price
                }
                inserted_id = self.collection.insert_one(product_document).inserted_id
                print("Produkt zostal dodany do bazy danych")
                print(inserted_id)
                break
            except ValueError as e:
                print("Blad: Wprowadz poprawna cene. Blad: ", e)
            except Exception as e:
                print("Wystąpil blad podczas dodawania produktu: ",e)
            


    def print_products(self):
        try:
            products = self.collection.find()

            for product in products:
                self.printer.pprint(product['name'])
        except Exception as e:
            print("Wystapil blad podczas pobierania produktow", e)

    def get_product_by_name(self,name):
        serached_product = self.collection.find_one({"name": name})
        self.printer.pprint(serached_product)

    def delete_product_by_name(self, name):
        self.collection.delete_one({"name": name})

    def update_product_by_name(self,name):
        # all_updates = {
        #     "$set": {"on_sotck": True},
        # }
        # collection.update_one({"name": name}, all_updates)
        updated_product = {
            "name": input("Nowa nazwa: "),
            "price": input("Nowa cena: ")
        }
        self.collection.replace_one({"name": name}, updated_product)

class ProductServices:
    def __init__(self):
        load_dotenv(find_dotenv())
        password = os.environ.get("MONGODB_PWD")

        connection_string = f"mongodb+srv://wojtekpawlik17:{password}@pharmacyproducts.7r8kbft.mongodb.net/?retryWrites=true&w=majority&appName=PharmacyProducts"

        client = MongoClient(connection_string)
        products_db = client.PharmacyProducts
        collections = products_db.list_collection_names()
        self.collection = products_db.Products

        self.printer = pprint.PrettyPrinter()
    
    def products_menu(self):
        interface = ProductsInterface(ProductsRepository(self.collection,self.printer))
        interface.products_menu()

class App: 
    def __init__(self, console):
        self.console = Console

    def start(self):
        main_theme = "rgb(8,153,147)"
        section_title = "bold yellow on black"
        while True:
            os.system('cls')
            console.print('-------Witaj w aplikacji------', style="bold black on yellow")
            console.print('\nWybierz co chcesz zrobić:', style=section_title)
            console.print('1-Obsluga klientow 🧑', style=main_theme)
            console.print('2-Obsluga produktow :pill:',style=main_theme )
            console.print('3-exit',style="red")

            choice = input("Twój wybór: ")
            match choice:
                case "1":
                    console.print("\n👪👪👪 Obsluga klientow 👪👪👪", style=section_title)
                    customer_service = CustomerServices()
                    customer_service.customer_menu()
                case "2":
                    console.print("\n:pill::pill::pill: [bold yellow]Obsluga produktów[/] :pill::pill::pill:")
                    product_service = ProductServices()
                    product_service.products_menu()
                case "3":
                    console.print(":waving_hand: Do zobaczenia! :waving_hand:", style="bold")
                    break
                case _:
                    print("Nieprawidlowa wartosc")

if __name__ == '__main__':
    console = Console()
    app = App(console)
    app.start()
