#!/usr/bin/pyton3
import pickle
class Custom0bject:
    def__init__(self, name: str, age: int, is_student: bool):
self. name = name
     self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError) as e:
            print(f"Serialization error: {e}")

    @classmethod
    def deserialize(cls, filename: str):
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                else:
                    print("Error: Loaded object is not of type CustomObject.")
                    return None
        except (FileNotFoundError, pickle.PickleError, EOFError) as e:
            print(f"Deserialization error: {e}")
            return None 
