class Product:
    def __init__(self, name, price, medicine_type):
        self.name = name
        self.price = price
        self.medicine_type = medicine_type

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "medicine_type": self.medicine_type
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['price'], data['medicine_type'])
