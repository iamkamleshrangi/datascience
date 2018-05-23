import numpy as np 

np.random.seed(123)

trails = [0]
for x in range(1000000) :
    coin = np.random.randint(0,2)
    trails.append(trails[x] + coin)

print("Heads => " + str(max(trails)))
print("Tails => " + str(len(trails) - 1))

per = ( float(max(trails)) / float((len(trails)) - 1)) * 100
print(per)
