q1 = int(input("Enter the Quantity; "))

 

price = 0
am = price * q1
if 0 < q1 < 100:
  price = 5.95
  am = price * q1
  print("Amount: ", am)

elif 100 <= q1 < 200:
  price = 5.75
  am = price * q1
  print("Amount: ", am)

elif 200 <= q1 < 300:
  price = 5.40
  am = price * q1
  print("Amount: ", am)

elif 300 <= q1 > 10000000:
  price = 5.15
  am = price * q1
  print("Amount: ", am)

  
print(price)