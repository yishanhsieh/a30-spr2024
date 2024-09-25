import random

(yes, times) = (0, 10000)

for t in range(times):
  r= ""
  for i in range (100):
    a = random.randint(0, 1)
    r = r + str(a)
  # print (r)
  if "000000" in r or "111111" in r:
  # if "111111" in r:
    yes += 1
print (yes / times * 100.0)


#======================

(yes, times) = (0, 10000)

for t in range(times):
  r= ""
  for i in range (100):
    a = random.randint(0, 1)
    r = r + str(a)
  for j in range(100 - 6):
    if r[0:6] in ["000000", "111111"]:
      yes += 1
      # print(r, "***")
    # else:
      # print (r)
    r = r[1:]
  # print(yes)
print (yes / (times * 94) * 100 / 2)