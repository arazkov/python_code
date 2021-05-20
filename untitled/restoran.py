class Restoran():
    """docstring fs Restoran."""

    def __init__(self, restoran_name, cuisine_type):
        self.restoran_name = restoran_name
        self.cuisine_type = cuisine_type
        self.increment_number = 0

    def discrip_restoran(self):
        print(self.restoran_name, self.cuisine_type)

    def open_restoran(self):
        print('Restoran is open')

    def increment_number_served(self, increment_number):
        self.increment_number += increment_number

class IceCreamStand(Restoran):
    """docstring for IceCreamStand."""

    def __init__(self, restoran_name, cuisine_type):
        super().__init__(restoran_name, cuisine_type)
        self.flavorse = ['escimo', 'plombir']




restoran = Restoran('MacDack', 'fast food')
restoran_2 = Restoran('Wertul', 'european')
restoran_3 = Restoran('Hertef', 'japan')
icecream_stand = IceCreamStand('Pom Pom', 'stand')

# restoran.increment_number_served(25)
# print(restoran.increment_number)
# restoran.increment_number_served(50)
# print(restoran.increment_number)

print(icecream_stand.flavorse)
print(icecream_stand.restoran_name, icecream_stand.cuisine_type)
