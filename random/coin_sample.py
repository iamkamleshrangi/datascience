import numpy as np 

np.random.seed(123)

trails = [0]
for x in range(10) :
    coin = np.random.randint(0,2)
    print(coin)
    trails.append(trails[x] + coin)

print(trails)
