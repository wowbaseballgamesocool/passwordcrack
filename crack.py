import random, time
from statistics import mean

trys_per_method = 10000


# +1 method

start = time.time()
list = []
for i in range(0, trys_per_method + 1):
    password = random.randint(1, 10000)
    x = 1
    attempts = 0
    while x != password:
        x += 1
        attempts += 1
    list.append(attempts)
    #print(attempts)
    
end = time.time()
print("+1 method took " + str(round(end - start, 3)) + "s and " + str(round(mean(list), 2)) + " attempts")



# -1 method
start = time.time()
list = []
for i in range(0, trys_per_method + 1):
    password = random.randint(1, 10000)
    x = 10000
    attempts = 0
    while x != password:
        x -= 1
        attempts += 1
    list.append(attempts)
    #print(attempts)
    
end = time.time()
print("-1 method took " + str(round(end - start, 3)) + "s and " + str(round(mean(list), 2)) + " attempts")




# even/odd method
start = time.time()
list = []
for i in range(0, trys_per_method + 1):
    password = random.randint(1, 10000)
    x = 0
    attempts = 0
    while x != password:
        x += 2
        attempts += 1
        if x > 10000: x = 1
    list.append(attempts)
    #print(attempts)
    
end = time.time()
print("even/odd method took " + str(round(end - start, 3)) + "s and " + str(round(mean(list), 2)) + " attempts")