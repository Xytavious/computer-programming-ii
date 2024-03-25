#inheritance.py
class Animal:
    def __init__(self, name, age):
      self. name = name 
      self. age = age

    def sayHi(self):
        print("Hi")


# cat inherits name, age, and sayHi from animal 
class Cat(Animal): 
  def __init__(self, name, age, sound):
    # Animal.__init_(name, age)
    super().__init__(name, age)
    self.sound = sound

  def saySound(self):
    print(self.sound)
cat = Cat("Billy", 5, "Meow")
cat.sayHi()
cat.saySound()

#dog inherits Name age and say hi\
class Dog(Cat):
  def __init__(self, name, age, soundDog):
   super().__init__(name, age, soundDog)
   self.soundDog = soundDog
  def saySoundDog(self):
    print(self.soundDog)
dog = Dog("Billy", 5, "*Bark Bark*")
dog.sayHi()
dog.saySound()
