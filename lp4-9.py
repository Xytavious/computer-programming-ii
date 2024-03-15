import random 
rnd = random.randint(1,20)
secNum = int(input("Pick a number between 1 and 20 "))

DevNum = rnd
print("Computers Number is", DevNum)
if secNum == DevNum:
  print("YOU WON!!!")

print("Players number is", secNum)
if secNum != DevNum:
  print("Better luck next time"):