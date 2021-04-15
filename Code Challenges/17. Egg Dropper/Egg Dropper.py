# To find the cirticalFloor while destorying a minimal number of eggs, you first have too drop an egg from the first floor. 
# If the egg breaks, you have found the criticalFloor. 
# If the egg doesn't break, you drop the egg from one floor higher.
# Therefore this proces will always result in finding the criticalFloor after dropping an egg from all 100 floors.

def minEggDropper100():
    minDrops100 = 100
    return minDrops100
    
# Alternatively

def minEggDropper100():
  numberFloors = 100
  currentFloor = 1
  while currentFloor < numberFloors:
    currentFloor += 1
  minDrops100 = currentFloor
  return minDrops100
    
# To find the cirticalFloor as quickly as possible using two eggs, you should use the first egg applying a binary search.
# You first drop an egg from the 50th floor.
# If the egg breaks, you drop the remaining egg from the first floor, increasing one floor at a time, untill the egg breaks.
# If the egg doesn't break, you drop the remaining egg from the 51st floor, increasing one floor at a time, untill the egg breaks.
# Therefore this proces will always result in finding the criticalFloor after dropping an egg from 51 floors.

def minEggDropper2():
    minDrops2 = 51
    return minDrops2
    
# To find the cirticalFloor as quickly as possible using x number of eggs, you should use the first eggs applying a binary search.
# You first drop an egg from the 50th floor.
# If the egg breaks, you drop the next egg from the 25th floor.
# If the egg doesn't break, you drop the egg from the 75th floor.
# You apply this binary search until you either have found the ciritcalFloor or you have only one egg remaining.
# In the latter case, you drop the remaining egg from one floor higher then the last succesfull drop.

def minEggDropperX(x, y):
    import math
    binaryDrops = math.ceil(math.log(y, 2))
    minDropsX = binaryDrops
    if binaryDrops > x:
        binaryDrops = x - 1
        remainingFloors = math.ceil(y // (2**(binaryDrops)))
        minDropsX = binaryDrops + remainingFloors
    return minDropsX
    
# Alternatively

def minEggDropperX(x, y):
    remaingingEggs = x
    usedEggs = 0
    remainingFloors = y
    while (remainingFloors > 1 and remaingingEggs > 1):
        remainingFloors -= remainingFloors // 2
        remaingingEggs -= 1
        usedEggs += 1
    minDropsX = usedEggs
    return usedEggs
  
