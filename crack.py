import random

password = random.randint(1, 10000)
x = 0
attempts = 0
while True:
 x += 1
 if x == password: break
 else:
  attempts += 1
  
