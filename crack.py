from time import time, sleep
from sys import argv
from random import randint
trys_per_method = 10000
possible_passwords = 10000
    # default is 10000 for both

seconds_decimal = 3
attempts_decimal = 2


try: trys_per_method = int(argv[2]); possible_passwords = int(argv[1]); seconds_decimal = int(argv[3]); attempts_decimal = int(argv[4]) # for use in terminal [ > crack.py 10000 10000 ]
except: pass

print("This will calculate which method is the fastest to brute force a password with " + str(possible_passwords) + " combinations, " + str(trys_per_method) + " times")

# +1 method
def plus1method():
    start = time()
    attempts = 1
    for i in range(0, trys_per_method + 1):
        password = randint(1, possible_passwords)
        x = 1
        while x != password:
            x += 1
            attempts += 1
        
        

    print("+1 method took " + str(round(time() - start, seconds_decimal)) + "s and " + str(round(attempts / trys_per_method, attempts_decimal)) + " attempts")



# -1 method
def minus1method():
    start = time()
    attempts = 1
    for i in range(0, trys_per_method + 1):
        password = randint(1, possible_passwords)
        x = possible_passwords
        
        while x != password:
            x -= 1
            attempts += 1
        

    print("-1 method took " + str(round(time() - start, seconds_decimal)) + "s and " + str(round(attempts / trys_per_method, attempts_decimal)) + " attempts")




# even/odd method
def evenoddmethod():
    start = time()
    attempts = 1
    for i in range(0, trys_per_method + 1):
        password = randint(0, possible_passwords - 1)
        x = 0
        
        while x != password:
            x += 2
            attempts += 1
            if x > possible_passwords: x = 1

        

    print("even/odd method took " + str(round(time() - start, seconds_decimal)) + "s and " + str(round(attempts / trys_per_method, attempts_decimal)) + " attempts")



# +10-1 method
# this method goes up by 10 each time, then 9, then 8 and so on
def plus10minus1method():
    start = time()
    
    attempts = 1
    for i in range(0, trys_per_method + 1):
        password = randint(0, possible_passwords - 1)
        x = 0
        mode = 0
        while x != password:
            x += 10 - mode
            attempts += 1
            if x > possible_passwords: mode += 1; x = 0

        

    print("+10-1 method took " + str(round(time() - start, seconds_decimal)) + "s and " + str(round(attempts / trys_per_method, attempts_decimal)) + " attempts")


plus1method()
minus1method()
evenoddmethod()
plus10minus1method()
#sleep(999)
