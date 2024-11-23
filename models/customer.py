import uuid

class Customer:
    def __init__(self, first_name, second_name, age, id=None):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.id = id or str(uuid.uuid4())[:15]

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "second_name": self.second_name,
            "age": self.age,
            "id": self.id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['first_name'], data['second_name'], data['age'], data['id'])
