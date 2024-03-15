class ClLP312:
  def __init__(self, food, clothing, entertainment, rent):
    self.food = food
    self.clothing = clothing
    self.entertainment = entertainment
    self.rent = rent
    self._budget = 0 
    self._percents = [0]*4 

  def __percent(self, number):
    return round((number/self._budget) * 100, 2)

  def calculate(self):
    self._budget = self.food + self.clothing + \
                   self.entertainment + self.rent
    self._percents[0] = self.__percent(self.food)
    self._percents[1] = self.__percent(self.clothing)
    self._percents[2] = self.__percent(self.entertainment)
    self._percents[3] = self.__percent(self.rent)

  def displays(self):
    print("Category\t\tBudget")
    print(f"food\t\t\t{self._percents[0]}%")
    print(f"Clothing\t\t{self._percents[1]}%")
    print(f"Entertainment\t{self._percents[2]}%")
    print(f"Rent\t\t\t{self._percents[3]}%")
    print(f"Total amount spent: ${self._budget:.2f}")
    
    



def main():
  print("Enter the amount spent last moth on the following {items: \n")

  pass


if __name__ == "__main__":
  main()
