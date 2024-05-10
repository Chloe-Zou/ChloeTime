import random

chop = ['onion', 'potato', 'garlic', 'tomato']

other= ['salt', 'pepper', 'chicken', 'lettuce', 'bread', 'ham']

def mix(num):
  if num == 2:
    ing1 = random.randint(0,9)
    ing2 = random.randint(0,9)
    print("Recipe: " + chop[ing1]+ " " +other[ing2])
