from vehicle import Vehicle

class Car(Vehicle):
    # top_speed = 100
    # warnings = []

    def brag(self):
        print('Look how cool my car is.')

car1 = Car()
car1.drive()

car1.add_warning('new warning')
# car1.__warnings.append('blah')
print(car1)

car2 = Car(200)
car2.drive()

print(car2.get_warnings())

car3 = Car(300)
car3.drive()