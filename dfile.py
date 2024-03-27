
def main():
  try: 
    with open("Langdat/prog213f.dat", 'r') as f:
      for line in f:
        ladta = line.split(" ")

  except Exception as e: 
    print("Error:", e)
    pass

  pass

if __name__ == "__main__":
  main()