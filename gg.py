class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, graduation_year):
        # DO not worry about the next line, we will come back to it very soon!
        super().__init__(name, age)
        self.graduation_year = graduation_year
    
    def graduates(self):
        print(f"{self.name} will graduate in {self.graduation_year}")