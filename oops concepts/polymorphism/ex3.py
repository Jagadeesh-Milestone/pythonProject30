class vehicle:
    def transport(self):
        print('vehicles are used to travel')
class car(vehicle):
    def transport(self):
        print('car is used to travel on roads')
class train(vehicle):
    def transport(self):
        print('train is used to travel on tracks')
class ship(vehicle):
    def transport(self):
        print('ship is used tp travel on water')
class aeroplane(vehicle):
    def transport(self):
        print('an aeroplane is used to travel in air')
a=aeroplane()
a.transport()

s=ship()
s.transport()

t=train()
t.transport()

c=car()
c.transport()