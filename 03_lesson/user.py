class User:

    def __init__(self, first_name, last_name):
        print("")
        self.first = first_name
        self.last = last_name

    def First(self):
        print("Моё имя", self.first)

    def Last(self):
        print("Моя фамилия", self.last)

    def name(self):
        print("Моё имя и фамилия:", self.first, self.last)
