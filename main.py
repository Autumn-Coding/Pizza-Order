pizzas = [100]
toppings = [10,20,30,40,50,0]
x = 1000
prices = []

def distanceFromX(num):
  return abs(x-num)

for pizza in pizzas:
  prices.append(pizza)
  for i in range(len(toppings)):
    price = pizza + toppings[i]
    prices.append(price)
    for n in range(i+1,len(toppings)):
      thisPrice = price + toppings[n]
      prices.append(thisPrice)

prices.sort()
distances = list(map(distanceFromX,prices))
minDistance = min(distances)
minIndex = distances.index(minDistance)

print(prices[minIndex])