import random, time, sys

trys_per_method = 10000
possible_passwords = 10000
# default is 10000 for both

seconds_decimal = 3
attempts_decimal = 2


try: trys_per_method = int(sys.argv[2]); possible_passwords = int(sys.argv[1]); seconds_decimal = int(sys.argv[3]); attempts_decimal = int(sys.argv[4]) # for use in terminal [ > crack.py 10000 10000 ]
except: pass

print("This will calculate which method is the fastest to brute force a password with " + str(possible_passwords) + " combinations, " + str(trys_per_method) + " times")

# +1 method
def plus1method():
    start = time.time()
    list = []
    attempts = 1
    for i in range(0, trys_per_method + 1):
        password = random.randint(1, possible_passwords)
        x = 1
        
        while x != password:
            x += 1
            attempts += 1
        
        
    end = time.time()
    print("+1 method took " + str(round(end - start, seconds_decimal)) + "s and " + str(round(attempts / trys_per_method, attempts_decimal)) + " attempts")



# -1 method
def minus1method():
    start = time.time()
    list = []
    attempts = 1
    for i in range(0, trys_per_method + 1):
        password = random.randint(1, possible_passwords)
        x = possible_passwords
        
        while x != password:
            x -= 1
            attempts += 1
        
        
    end = time.time()
    print("-1 method took " + str(round(end - start, seconds_decimal)) + "s and " + str(round(attempts / trys_per_method, attempts_decimal)) + " attempts")




# even/odd method
def evenoddmethod():
    start = time.time()
    list = []
    attempts = 1
    for i in range(0, trys_per_method + 1):
        password = random.randint(0, possible_passwords - 1)
        x = 0
        
        while x != password:
            x += 2
            attempts += 1
            if x > possible_passwords: x = 1

        
    end = time.time()
    print("even/odd method took " + str(round(end - start, seconds_decimal)) + "s and " + str(round(attempts / trys_per_method, attempts_decimal)) + " attempts")



# +10-1 method
# this method goes up by 10 each time, then 9, then 8 and so on
def plus10minus1method():
    start = time.time()
    list = []
    attempts = 1
    for i in range(0, trys_per_method + 1):
        password = random.randint(0, possible_passwords - 1)
        x = 0
        mode = 0
        
        while x != password:
            x += 10 - mode
            attempts += 1
            if x > possible_passwords: mode += 1; x = 0

        
    end = time.time()
    print("+10-1 method took " + str(round(end - start, seconds_decimal)) + "s and " + str(round(attempts / trys_per_method, attempts_decimal)) + " attempts")


plus1method()
minus1method()
evenoddmethod()
plus10minus1method()
time.sleep(999)