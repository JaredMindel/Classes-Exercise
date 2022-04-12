from xml.sax.handler import property_declaration_handler


class Animal:
    """Animal Class"""
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name

    def move():
        print("I'm moving!")
    
    def speak():
        print("*Unintelligible noises*")
    
    def sleep():
        print("Goodnight!")

class Book:
    """Book Class"""
    def __init__(self, name, author, isbn, page_count):
        self._name = name
        self._author = author
        self._isbn = isbn
        self._page_count = page_count
    
    def open():
        print("Opening book")

    def close():
        print("Closing book")

class Vehicle:
    """Vehicle Class"""

    def __init__(self, make, model):
        self._make = make
        self._model = model
    
    def move_forward():
        print("Moving forward")

    def move_backwards():
        print("Moving backwards")
    
    def stop():
        print("Stopping")