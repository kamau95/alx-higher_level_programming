class Home:
    area = 40
    def __init__(self, location, people):
        self.location = location
        self.people = people
kaburus = Home(22, "children")
print(hasattr(kaburus, "location"))

