import random
import os
from dotenv import load_dotenv, find_dotenv
import pprint
from pymongo import MongoClient
from rich.console import Console
from rich.theme import Theme
from utility import loading
import uuid
import json

# Napisac logike dla id(generowanie id na podstawie wymyslonego algorytmu albo z biblioteki). Get i set. jezeli id nowego obiektu jest reowne innemu(iteracja przez list), to wygeneruj inne id
# Dane będą przetrzymywane w plikach tekstowych
# 3 opcja aplikacji- pomocnik sprzedaży. 1 odczyt danych z pliku tekstowego. 2 użytkownik dodaje produkt wpisując jego nazwe oraz ilość. 3 opcja usunięcia dodanego produktu. 4 Przleiczenie całkowietego kosztu zakupów. Do tegop użyję operatorów. osbługa błędów. 


class Customer:
    def __init__(self,first_name,second_name,age,id):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.id = id

    def data_to_dict(self):
        return {
            "first_name" : self.first_name,
            "second_name" : self.second_name,
            "age" : self.age,
            "id" : self.id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['first_name'], data['second_name'], data['age'], data['id'])

class CustomerServices:
    
    # Methods for file service
    def save_customer_to_file(self,cus_database_file,customer):
        customers = self.read_customers_from_file(cus_database_file)
        customers.append(customer.data_to_dict())
        file = open(cus_database_file, "w")
        with open(cus_database_file, 'w') as file:
            json.dump(customers, file, indent=4)
    
    def read_customers_from_file(self, cus_database_file):
        if not os.path.exists(cus_database_file):
            return []
        try:
            with open(cus_database_file, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
            

    def create_customer(self):
        cus_database_file = 'customers_database.json'
        
        customer_first_name = input("Imie: ")
        customer_second_name = input("Nazwisko: ")
        customer_age = input("wiek: ")
        customer_id = str(uuid.uuid4())[0:15]
        new_customer = Customer(customer_first_name, customer_second_name, customer_age, customer_id)
        self.save_customer_to_file(cus_database_file,new_customer)
        console.print("Dodano nowego klienta", style="success")
        
    
    def show_customer_list(self):
        cus_database_file = 'customers_database.json'
        customers_list = self.read_customers_from_file(cus_database_file)
        if customers_list:
            console.print("---LISTA KLIENTOW---")
            for customer_data in customers_list:
                customer = Customer.from_dict(customer_data)
                print(f"Imię: {customer.first_name}, Nazwisko: {customer.second_name}, Wiek: {customer.age}")
        else:
            console.print("W bazie danych nie ma żadnych klientów", style="error")

        
        

    def delete_customer(self):
        cus_database_file = 'customers_database.json'
        customers_list = self.read_customers_from_file(cus_database_file)
        print("Wybierz klienta, którego chcesz usunąć")
        customer_first_name = input("Wpisz imię: ")
        customer_second_name = input("Wpisz nazwisko: ")

        updated_customers_list = [
            customer for customer in customers_list
            if not (customer['first_name'] == customer_first_name and customer['second_name'] == customer_second_name)
        ]

        with open(cus_database_file, 'w') as file:
            json.dump(updated_customers_list, file, indent=4)
        console.print(f"Usunięto klienta: {customer_first_name} {customer_second_name}", style="error")

    def update_customer(self):
        cus_database_file = 'customers_database.json'
        customers_list = self.read_customers_from_file(cus_database_file)
        print("Wybierz klienta, którego chcesz edytować")
        customer_first_name = input("Wpisz imię: ")
        customer_second_name = input("Wpisz nazwisko: ")

        for customer in customers_list:
            if customer['first_name'] == customer_first_name and customer['second_name'] == customer_second_name:
                print(f"Znaleziono klienta: {customer_first_name} {customer_second_name}")
                while True:
                    print("Które dane chcesz zmienić?")
                    print("1 - Imię")
                    print("2 - Nazwisko")
                    print("3 - Wiek")
                    
                    choice = input("Twój wybór: ")

                    if choice == "1":
                        customer['first_name'] = input("Wpisz nowe imię: ")
                        break
                    elif choice == "2":
                        customer['second_name'] = input("Wpisz nowe nazwisko: ")
                        break
                    elif choice == "3":
                        customer['age'] = input("Wpisz nowy wiek: ")
                        break
                    else:
                        print("Nieprawidłowa wartość! Wpisz liczbę z zakresu od 1 do 3")

                with open(cus_database_file, 'w') as file:
                    json.dump(customers_list, file, indent=4)
                console.print("Zaktualizowano dane klienta: ", customer['first_name'], customer['second_name'], style="success")
                return

        print(f"Nie znaleziono klienta: {customer_first_name} {customer_second_name}")



    def customer_menu(self):
        while True:
            console.print("\n➕1- Stworz nowy profil klienta ➕", style="main_theme")
            console.print("2- ➖ Usun profil klienta ➖",  style="main_theme")
            console.print("3- 📜 Wyswietl liste klientow 📜",  style="main_theme")
            console.print("4- 📝  Edytuj dane klienta 📝",  style="main_theme")
            console.print("5- 🔙 Wroc do glownego menu 🔙",  style="main_theme")

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
                    self.update_customer()
                case "5":
                        loading()
                        break
                case _:
                    console.print("Nieprawidlowa wartosc! Wpisz liczbe z zakresu od 1 do 4", style="error")


class ProductsInterface:
    def __init__(self, repository):
        self.repository = repository

    def products_menu(self):
        
        while True:
            console.print("\n1- ➕ Dodaj produkt do bazy danych ➕", style="main_theme")
            console.print("2- 📜 Wyswietl liste produktow 📜", style="main_theme")
            console.print("3- ✍  Edytuj produkt ✍", style="main_theme")
            console.print("4- ➖ Usun produkt z bazy danych ➖", style="main_theme")
            console.print("5- 🔎 Znajdz konkretny lek 🔎", style="main_theme")
            console.print("6-  📜 Wyswietl produkty danego typu 📜", style="main_theme")
            console.print("7- 🔙 Wroc do glwonego menu 🔙", style="main_theme")
            
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
                    print("Wyswietl produkty danego typu")
                    medicine_type = input("Wpisz jakiego typu lekow szukasz: ")
                    self.repository.print_product_of_specific_type(medicine_type)
                case "7":
                    loading()
                    break
                case _:
                    console.print("Nieprawidlowa wartosc! Wpisz liczbe z zakresu od 1 do 6", style="error")



class ProductsRepository:
    def __init__(self, collection,printer):
        self.collection = collection
        self.printer = printer

    def insert_product_doc(self):
        product_name = input("Wpisz nazwe leku: ")
        medicine_type = input("Wpisz typ leku: ")
        while True:
            product_price = input("Wpisz cene leku: ")
            try:
                price = float(product_price)
                if price < 0:
                    raise ValueError("Cena nie może być ujemna!")
                
                product_document = {
                    "name": product_name,
                    "price": price,
                    "medicine_type": medicine_type
                }
                inserted_id = self.collection.insert_one(product_document).inserted_id
                print("Produkt zostal dodany do bazy danych")
                print(inserted_id)
                break
            except ValueError as e:
                print("Blad: Wprowadz poprawna cene. Blad: ", e)
            except Exception as e:
                print("Wystąpil blad podczas dodawania produktu: ",e)
            

    def print_product_of_specific_type(self,medicine_type):
        print(f"Wyszukiwany typ leku: {medicine_type}")
        searched_products = self.collection.find({"medicine_type": medicine_type}).sort({ "price": 1})
        for i, searched_product in enumerate(searched_products, start=1):
            index = i
            product_name = searched_product['name']
            product_price = searched_product['price']
            print(f"Produkt {index}: {product_name} {product_price}")
            
    
    def print_products(self):
        
        def pprint_to_str(product, index):
            return f"Product number {index+1}: {product['name']} cena: {product['price']}"
        try:
            products = self.collection.find()
            
            product_strings = map(lambda item: pprint_to_str(item[1], item[0]), enumerate(products))

            for product_str in product_strings:
                self.printer.pprint(product_str)

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
        username = os.environ.get("MONGODB_USERNAME")

        connection_string = f"mongodb+srv://{username}:{password}@pharmacyproducts.7r8kbft.mongodb.net/?retryWrites=true&w=majority&appName=PharmacyProducts"

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
        self.console = console

    def start(self):
        while True:
            
            console.print('-------Witaj w aplikacji------', style="bold black on yellow")
            console.print('\nWybierz co chcesz zrobić:', style="section_title")
            console.print('1-Obsluga klientow 🧑', style="main_theme")
            console.print('2-Obsluga produktow :pill:',style="main_theme" )
            console.print('3-exit 🔚',style="red")

            choice = input("Twój wybór: ")
            match choice:
                case "1":
                    console.print("\n👪👪👪 Obsluga klientow 👪👪👪", style="section_title")
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
                    console.print("Nieprawidlowa wartosc! Wpisz liczbe z zakresu od 1 do 6", style="error")


if __name__ == '__main__':
    os.system('cls')
    custom_theme = Theme({"main_theme": "rgb(8,153,147)", "section_title" : "bold yellow on black", "error": "bold red underline", "success": "bold green"})
    console = Console(theme=custom_theme)
    app = App(console)
    app.start()
