class PersonH:

    first_name: str
    last_name: str

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        super().__init__()

    def __repr__(self):
        return f'Person: {self.first_name} {self.last_name} hash = {hash(self)}'








# Hash is an algorithm that turn object of an unknown size to a fixed immutable size.
# it helps to make collection types more faster to access and easier to compare objects


# i =42
# hash(i)
# ==> 42
# (42).__hash__
# ==> 42
#(82).__hash__
# ==> 82
#