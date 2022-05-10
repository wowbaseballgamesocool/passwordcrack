import random, time
from statistics import mean

trys_per_method = 10000
possible_passwords = 10000
# default is 10000 for both


# +1 method
def plus1method():
    start = time.time()
    list = []
    for i in range(0, trys_per_method + 1):
        password = random.randint(1, possible_passwords)
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
def minus1method():
    start = time.time()
    list = []
    for i in range(0, trys_per_method + 1):
        password = random.randint(1, possible_passwords)
        x = possible_passwords
        attempts = 0
        while x != password:
            x -= 1
            attempts += 1
        list.append(attempts)
        #print(attempts)
        
    end = time.time()
    print("-1 method took " + str(round(end - start, 3)) + "s and " + str(round(mean(list), 2)) + " attempts")




# even/odd method
def evenoddmethod()
    start = time.time()
    list = []
    for i in range(0, trys_per_method + 1):
        password = random.randint(1, possible_passwords)
        x = 0
        attempts = 0
        while x != password:
            x += 2
            attempts += 1
            if x > possible_passwords: x = 1
        list.append(attempts)
        #print(attempts)
        
    end = time.time()
    print("even/odd method took " + str(round(end - start, 3)) + "s and " + str(round(mean(list), 2)) + " attempts")



# +10-1 method
# this method goes up by 10 each time, then 9, then 8 and so on
def plus10minus1method():
    start = time.time()
    list = []
    for i in range(0, trys_per_method + 1):
        password = random.randint(1, possible_passwords)
        x = 0
        mode = 0
        attempts = 0
        while x != password:
            x += 10 - mode
            attempts += 1
            if x > possible_passwords: mode += 1; x = 0
        list.append(attempts)
        #print(attempts)
        
    end = time.time()
    print("+10-1 method took " + str(round(end - start, 3)) + "s and " + str(round(mean(list), 2)) + " attempts")

