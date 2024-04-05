def main():
  desT = float(input(" Enter time spent on designing in minuutes: "))
  codeT = float(input(" Enter time spent on codeing in minutes: "))
  deBugT = float(input(" Enter time spent on debugging in minutes: "))
  testT = float(input( " Enter time spent on Testing in minutes : "))

  #total time 
  totT = desT + codeT + deBugT + testT

  #  percents 
  desP = (desT / totT) * 100
  codeP = (codeT / totT) * 100
  deBugP = (deBugT / totT) * 100
  testP = (testT / totT) * 100

  #Display
  print("Total Times:")
  print("total time spent on design is ", desT)
  print("total time spent on codeing is ", codeT)
  print("total time spent on debugging is ", deBugT)
  print("total time spent on Testing is ", testT)

  print("Task\t\t %Time")
  print("designing\t\t" , desP)
  print("codeing\t\t", codeP)
  print("debugging\t\t" , deBugP)
  print("Testing\t\t" , testP)
  