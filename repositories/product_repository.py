from pymongo.collection import Collection

class ProductRepository:
    def __init__(self, collection: Collection):
        self.collection = collection

    def insert_product(self, product):
        self.collection.insert_one(product.to_dict())

    def get_all_products(self):
        return list(self.collection.find())

    def find_by_name(self, name):
        return self.collection.find_one({"name": name})

    def delete_by_name(self, name):
        self.collection.delete_one({"name": name})

    def update_by_name(self, name, updated_data):
        self.collection.update_one({"name": name}, {"$set": updated_data})
