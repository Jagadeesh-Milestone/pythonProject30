#DataFrame:
import pandas as p

data={'fruits':['apple','banana','mango'],
      'cost/kg':[100,40,60]}
print(data)
x=p.DataFrame(data,index=['fruitone','fruittwo','fruitthree'])
print(x)

print(x.loc['fruitone'])

