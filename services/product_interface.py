from services.product_service import ProductService
from rich.console import Console

from utility import loading

class ProductInterface:
    def __init__(self, service: ProductService, console: Console):
        self.service = service
        self.console = console

    def product_menu(self):
        while True:
            self.console.print("\n1- Dodaj produkt", style="main_theme")
            self.console.print("2- Wyświetl produkty", style="main_theme")
            self.console.print("3- Usuń produkt", style="main_theme")
            self.console.print("4- Zaktualizuj produkt", style="main_theme")
            self.console.print("5- Wróć do głównego menu", style="main_theme")

            choice = input("Twój wybór: ")
            match choice:
                case "1":
                    self.service.add_product()
                case "2":
                    self.service.list_products()
                case "3":
                    self.service.delete_product()
                case "4":
                    self.service.update_product()
                case "5":
                    loading()
                    break
                case _:
                    self.console.print("Nieprawidłowa opcja, spróbuj ponownie.", style="error")
