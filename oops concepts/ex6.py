#methods:
#instance method:
class milestone:
    productid=980980
    def product(self):
        productname='oneplus'
        productcost=25000
        print('product name is',productname)
        print('product cost is',productcost)
        print('product id is',self.productid)
m=milestone()
m.product()
#note:we can access the class attributes into an instance method
#by using self argument.
