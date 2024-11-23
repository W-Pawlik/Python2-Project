import os
from services.customer_service import CustomerService
from services.product_interface import ProductInterface
from config.database import get_database
from repositories.product_repository import ProductRepository
from services.product_service import ProductService
from utils.console_utils import console

class App: 
    def __init__(self, console):
        self.console = console

    def start(self):
        db = get_database()
        product_repo = ProductRepository(db.Products)
        product_service = ProductInterface(ProductService(product_repo, console), console)

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
                    customer_service = CustomerService(console)
                    customer_service.customer_menu()
                case "2":
                    console.print("\n:pill::pill::pill: [bold yellow]Obsluga produktów[/] :pill::pill::pill:")
                    product_service.product_menu()
                case "3":
                    console.print(":waving_hand: Do zobaczenia! :waving_hand:", style="bold")
                    break
                case _:
                    console.print("Nieprawidlowa wartosc! Wpisz liczbe z zakresu od 1 do 6", style="error")


if __name__ == '__main__':
    os.system('cls')
    
    app = App(console)
    app.start()
