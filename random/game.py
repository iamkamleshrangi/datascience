# Import numpy and set seed
import numpy as np
#np.random.seed(123)

# Starting step
step = 1

# Roll the dice
#dice = np.random.randint(1,7)

# Finish the control construct
for tries in range(100):
    dice = np.random.randint(1,7)
    if dice <= 2 :
        step = step - 1
    elif dice <= 5 :
        step = step + 1
    else :
        step = step + np.random.randint(1,7)

# Print out dice and step
print('dice ' + str(dice) + ' with steps of ' + str(step))
