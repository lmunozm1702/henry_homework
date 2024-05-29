import numpy as np

class Pila:
  def init (self):
    self.items = []

  def cargaItems(self):
    self.items = list(np.random.randint(0, 20, 20))
    print('La pila creada contiene: ', self.items)

  def resultado(self):
    for jugada in self.jugadas:
      self.suma += jugada
    
    if self.suma >= 51:
      print('Perdiste, la suma de los elementos es: ', self.suma)
    else:
      resto = 0
      self.puntos = 10
      while self.suma + resto <= 50:
        resto += self.items.pop()
        self.puntos -= 1
      print('Ganaste, la suma de los elementos es: ', self.suma)
      print('Tus puntos son: ', self.puntos)

  def jugar(self):
    self.cargaItems()
    print('Elige la cantidad de elementos a jugar: ')
    self.n = int(input())
    self.jugadas = []
    self.suma = 0

    for i in range(self.n):
      self.jugadas.append(self.items.pop())

    print('Las jugadas son: ', self.jugadas)
    self.resultado()
    

p = Pila()
p.jugar()