#prog213.py
from Cl213f import



def main():
  try: 
    electbills = []
    with open("langdat/prog213f.dat", 'r') as f:
      for line in f:
        kwh = int(line)
        if kwh != -999:
          bill = Cl213f(kwh)
          electbills.append(bill)
    for bill in electbills:
      bill.calc()
      print(bill)    #print(str(bill))

  except Exception as e: 
    print("Error:", e)
    pass

  pass

if __name__ == "__main__":
  main()