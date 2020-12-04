import math
# x = input("Enter x to calculate: ")

c1, c2, c3, c4 = 0, 0, 0, 0
def getChange(x):
  if x > 100000:
    c1 = int(x/100000)
    a = x % 100000
  if x > 50000:
    c2 = int(a/50000)
    a = a % 50000
  if x > 20000:
    c3 = int(a/20000)
    a = a % 20000
  if x > 10000:
    c4 = int(a/10000)
    a = a % 10000
  print("Change " + str(x) + " to " + str(c1) + " 100000, " + str(c2) + " 50000, " 
        + str(c3) + " 20000, " + str(c4) + " 10000")

# y1 = 4*(x**2 + 10*x*math.sqrt(x) + 3*x + 1)

# y2 = (math.sin(math.pi*x**2) + math.sqrt(x**2 + 1))/(math.e**(2*x) + math.cos((math.pi*x)/4))

# getChange(x)
for i in range(1,10):
  for j in range (1,10):
    if(i*j < 10):
      print(i*j, end ="  ")
    else:
      print(i*j, end =" ")
  print()