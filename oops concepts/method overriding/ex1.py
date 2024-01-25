#method overriding:
class parent:
    def mobile(self):
        print('I will give 10000 to buy a mobile')
class child(parent):
    def mobile(self):
        print('I will buy a mobile for 25000')
c=child()
c.mobile()

p=parent()
p.mobile()