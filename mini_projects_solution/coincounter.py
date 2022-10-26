# A coin is flipped a hundred times so this program counts the number of times the head and tail was each flipped

import random

heads = 0
tail = 0

for i in range(0,100):
    flip = random.randint(0,1)
    # print(flip)
    if flip == 0:
        heads += 1
    else:
        tail += 1
print("I flipped a coin 100 times:")       
print("\tHead is flipped %i" % heads +" times")
print("\tTail is flipped %i" % tail +" times")

#There is a probability that the coin will fall in it sides so in that case the program below will handle it

head = 0 
tail = 0 
side = 0 

for i in range(0,100):
    flip = random.randint(0,2)
    # print(flip)
    if flip == 0:
        head += 1
    elif flip == 1:
        tail += 1
    else:
        side += 1
        
print("\tHead is flipped %i" % head +" times")
print("\tTail is flipped %i" % tail +" times")
print("\tSide is flipped %i" % side +" times")             
        
        