#prog162aRecursive.py
import sys
sys.setrecursionlimit(7900000)

def factloop(n):
  product = 1
  for num in range(n, 0, -1):
    product *= num 
  return product 

def fact (n):
  if n <= 1: return 1   # base/Ending case
  return n * fact(n-1)   # recursive case

def main():
  num = int(input("inter number: "))
  while num != 0:
    factn = fact(num)
    print(f"{num}! = {factn}")
    num = int(input("enter a number: "))


if __name__ == "__main__":
  main()