import json
import os

class CustomerRepository:
    def __init__(self, database_file='customers_database.json'):
        self.database_file = database_file

    def read_all(self):
        if not os.path.exists(self.database_file):
            return []
        try:
            with open(self.database_file, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_all(self, customers):
        with open(self.database_file, 'w') as file:
            json.dump(customers, file, indent=4)
