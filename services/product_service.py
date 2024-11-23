from models.product import Product
from repositories.product_repository import ProductRepository
from rich.console import Console

class ProductService:
    def __init__(self, repository: ProductRepository, console: Console):
        self.repository = repository
        self.console = console

    def add_product(self):
        name = input("Podaj nazwę produktu: ")
        price = input("Podaj cenę produktu: ")
        medicine_type = input("Podaj typ leku: ")

        try:
            price = float(price)
            if price < 0:
                raise ValueError("Cena nie może być ujemna.")

            product = Product(name, price, medicine_type)
            self.repository.insert_product(product)
            self.console.print("Produkt dodany pomyślnie!", style="success")
        except ValueError as e:
            self.console.print(f"Błąd: {e}", style="error")

    def list_products(self):
        products = self.repository.get_all_products()
        if not products:
            self.console.print("Brak produktów w bazie danych.", style="error")
            return

        self.console.print("--- Lista produktów ---")
        for product in products:
            self.console.print(
                f"Nazwa: {product['name']}, Cena: {product['price']}, Typ: {product['medicine_type']}"
            )

    def delete_product(self):
        name = input("Podaj nazwę produktu do usunięcia: ")
        self.repository.delete_by_name(name)
        self.console.print(f"Produkt {name} został usunięty.", style="error")

    def update_product(self):
        name = input("Podaj nazwę produktu do aktualizacji: ")
        product = self.repository.find_by_name(name)

        if not product:
            self.console.print("Nie znaleziono produktu.", style="error")
            return

        self.console.print("Znaleziono produkt:", style="main_theme")
        self.console.print(
            f"Nazwa: {product['name']}, Cena: {product['price']}, Typ: {product['medicine_type']}"
        )

        new_name = input("Nowa nazwa (pozostaw puste, aby nie zmieniać): ") or product['name']
        new_price = input("Nowa cena (pozostaw puste, aby nie zmieniać): ") or product['price']
        new_type = input("Nowy typ (pozostaw puste, aby nie zmieniać): ") or product['medicine_type']

        try:
            new_price = float(new_price)
            if new_price < 0:
                raise ValueError("Cena nie może być ujemna.")
        except ValueError as e:
            self.console.print(f"Błąd: {e}", style="error")
            return

        updated_data = {
            "name": new_name,
            "price": new_price,
            "medicine_type": new_type
        }
        self.repository.update_by_name(name, updated_data)
        self.console.print("Produkt zaktualizowany pomyślnie!", style="success")
