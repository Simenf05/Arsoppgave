

def sjekkOmPrimTall(input):
  boolean = True
  input = int(input)
  
  if input == 2 | 3:
    return boolean
  
  if input < 2:
    return False
  
  for i in range(2, input-1):
    if input % i == 0:
      boolean = False
      break
  return boolean
  
testTil = int(input())
primtallListe = []

for i in range(testTil):
  if sjekkOmPrimTall(i) == True:
    primtallListe.append(i)

print(primtallListe)

# print("skriv et tall du vil sjekke om er primtall")
# yeet = int(input())
# ikkeprim = str(yeet) + " er ikke primtall"
# prim = str(yeet) + " er et primtall"
# boolean = True

# if yeet == 2 | 3:
#   print(prim)
#   exit()

# for i in range(2, yeet-1):
#   if yeet % i == 0:
#     boolean = False
#     break

# if boolean == True:
#   print(prim)
# else:
#   print(ikkeprim)


# if (yeet % 2 == 0):
#   print(ikkeprim)
# elif yeet % 3 == 0:
#   if yeet != 3:
#     print(ikkeprim)
# else:
#   print("er primtall")

