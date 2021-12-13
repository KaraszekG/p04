# Írj programot, mely beolvas három egész számot, és kiírja a képernyőre a legkisebbet!


egy = int(input("Írj egy számot: "))
ketto = int(input("Írj mégegy számot: "))
harom = int(input("Írj mégegy számot: "))


if egy > ketto < harom:
  print("A(z) " , ketto , " kissebb")


if ketto > egy < harom:
  print("A(z) " , egy , " kissebb")


if ketto > harom < egy:
  print("A(z) " , harom , " kissebb")
































