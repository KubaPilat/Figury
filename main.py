print("Wybierz: ")
print("A to pole kwadrat")
print("B to pole prostokąt")
print("C to pole koło")
print("D to pole trapez")
print("E to pole romb")
print("0 oznacza wyjście z programu")



def kalkulator(): 

#pytanie o figurę
  Pytanie = str(input("A, B, C, D, E, 0: "))

#kwadrat
  while Pytanie == "A" or Pytanie == "a":
    A = int(input("Podaj A: "))
    print("Pole kwadratu wynosi", (A**2))
    break

#prostokąt
  while Pytanie == "B" or Pytanie == "b":
    A = int(input("Podaj A: "))
    B = int(input("Podaj B: "))
    print("Pole prostokąta wynosi", (A * B))
    break

#koło
  while Pytanie == "C" or Pytanie == "c":
    import math
    Pi = math.pi
    Promien = int(input("Długość R: "))
    print("Pole koła wynosi", ((math.pow(Promien, 2)) * Pi))
    break

#trapez
  while Pytanie == "D" or Pytanie == "d":
    A = int(input("Podaj długość boku A: "))
    B = int(input("Podaj długość boku B: "))
    C = int(input("Podaj wysokość : "))
    print("Pole trapez wynosi", (((A + B) * C)) / 2)
    break

#romb
  while Pytanie == "E" or Pytanie == "e":
    A = int(input("Podaj długość boku: "))
    B = int(input("Podaj wysokość: "))
    print("Pole Rombu wynosi", (A * B))
    break



#Pytanie o koniec
  Koniec= input('SPACJA –kontynuuj z wyjściem do głównego menu lub 0 –zakończ program.')

  while Koniec==" ":
    kalkulator()
    break

  if Koniec == "0":
    print("koniec")
  else:
    print("brak odpowiedzi")
    

kalkulator()

