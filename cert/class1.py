
class Car():
    def __init__(self, name, model):
        self.name = name 
        self.model = model 

    def __str__(self):
        return f"The current car named as {self.name } , and model {self.model}.  "

car1 = Car("beast", "Verna")
print(car1)
print(car1.__dict__)
print(car1.name , car1.model)
