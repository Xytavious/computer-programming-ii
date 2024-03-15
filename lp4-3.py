egs = int(input("How many eggs do you have "))
mod = egs % 12
dozens = egs // 12
price = 0
if 0 < dozens < 4:
  price = 0.50 

elif 3 < dozens < 6:
  price = 0.45

elif 6 < dozens < 11:
  price = 0.40

elif 11 < dozens > 10000000:
  price = 0.35

print("price per dozern = $",price)
