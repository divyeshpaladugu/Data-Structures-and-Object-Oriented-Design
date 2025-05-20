class Professor:
    def __init__(self, name, age, starting_year, title, courses=None):
        self.name = name
        self.age = age
        self.starting_year = starting_year
        self.title = title

        if courses is None:
            self.courses = []
        self.courses = courses

    def __str__(self):
        return f"Professor: {self.name} Started {self.starting_year}"