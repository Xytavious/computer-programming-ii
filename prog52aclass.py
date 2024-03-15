class Shape:
  # constructer sets up class data 
  def __init__(self, length, width):
    self.length = length
    self.width = width 
    self._area = 0 # _ prefix means its basicaly private
    self._perim = 0 # it should only be called in the class

  # Mutator/setter: modifies class data 
  def calculate(self):
    self._area = self.length * self.width
    self._perim = 2 * self.length + 2 * self.width

  def setLength(self, length):  # Redundant
    self.length = length

  # Accessor/Getter: returns class data
  def getArea(self):
    return self._area

  def getPerimeter(self):
    return self._perim
  


def main():
  len = int(input("Enter Length "))
  wid = int(input(" Enter Lidth "))
  # make a new "shape" object 
  shape = Shape(len, wid) # call "Shape" constructor
  # could say "shape.setlength(5)"
  shape.calculate()
  print("Area:", shape.getArea())
  print("Perimeter:", shape.getPerimeter())
  pass


if __name__ == "__main__":
  main()
