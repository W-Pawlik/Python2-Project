import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def get_database():
    username = os.getenv("MONGODB_USERNAME")
    password = os.getenv("MONGODB_PWD")
    connection_string = (
        f"mongodb+srv://{username}:{password}"
        "@pharmacyproducts.7r8kbft.mongodb.net/?retryWrites=true&w=majority"
    )
    client = MongoClient(connection_string)
    return client.PharmacyProducts
