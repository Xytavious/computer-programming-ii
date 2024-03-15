num1 = int(input(" enter num 1 "))
num2 = int(input(" enter num 2 "))
while (num2 > 0):
  temp = num1 % num2
  num1 = num2
  num2 = temp 
print(num1)
print(num2)