#!/usr/bin/env python3

APPROVED_BREEDS = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]


class Dog:
    def __init__(self, name="", breed=""):
        self._name = ""
        self._breed = ""
        self.name = name
        self.breed = breed

    def get_name(self):
        print("Retrieving name.")
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            print(f"Setting name to { name }.")
            self._name = name

        else:
            print("Name must be string between 1 and 25 characters.")

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed

        else:
            print("Breed must be in list of approved breeds.")

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)


Bosco = Dog("Bosco", "Stew")
print(Bosco.breed)
