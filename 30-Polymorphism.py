# Polymorphism = One function, multiple forms
class bird:
    def fly(self):
        return "Bird is flying"

class airplane:
    def fly(self):
        return "Airplane is flying"

# Same method name, different behavior depending on object
for obj in [bird(), airplane()]:
    print(obj.fly())