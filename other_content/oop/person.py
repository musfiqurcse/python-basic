
class Person:

    def get_name(self):
        return f"Name of the Person is: {self.__name}"

    def __init__(self, name: str, dob: int):
        self.__name = name
        self.__dob = dob

    def get_name(self):
        return f"Name of the Person is: {self.__name}"

	# a default string function to represent the Person
    def __str__(self):
        return self.get_name()

# def set_name(self, name):
#     self.__name = name
