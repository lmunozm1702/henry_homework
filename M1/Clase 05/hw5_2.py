class Jarras:
  def init(self):
    self.jarra_5 = 0
    self.jarra_3 = 0

  def llenar_jarra_5(self):
    self.jarra_5 = 5
    print('La jarra de 5 litros ha sido llenada')

  def llenar_jarra_3(self):
    self.jarra_3 = 3
    print('La jarra de 3 litros ha sido llenada')

  def vaciar_jarra_5(self):
    actual = self.jarra_5
    self.jarra_5 = 0
    print('La jarra de 5 litros ha sido vaciada, tenía ', actual, ' litros')

  def vaciar_jarra_3(self):
    actual = self.jarra_3
    self.jarra_3 = 0
    print('La jarra de 3 litros ha sido vaciada, tenía ', actual, ' litros')  

  def ver_jarras(self):
    print('La jarra de 5 litros tiene ', self.jarra_5, ' litros')
    print('La jarra de 3 litros tiene ', self.jarra_3, ' litros')

  def verter_5_en_3(self):
    if self.jarra_5 > 0 and self.jarra_3 < 3:
      if self.jarra_5 + self.jarra_3 <= 3:
        self.jarra_3 += self.jarra_5
        self.jarra_5 = 0
      else:
        self.jarra_5 -= 3 - self.jarra_3
        self.jarra_3 = 3
      print('Se ha vertido agua de la jarra de 5 litros a la de 3 litros')
    
    
  def verter_3_en_5(self):
    if self.jarra_3 > 0 and self.jarra_5 < 5:
      if self.jarra_3 + self.jarra_5 <= 5:
        self.jarra_5 += self.jarra_3
        self.jarra_3 = 0
      else:
        self.jarra_3 -= 5 - self.jarra_5
        self.jarra_5 = 5
      print('Se ha vertido agua de la jarra de 3 litros a la de 5 litros')

juego = Jarras()
juego.llenar_jarra_3()
juego.llenar_jarra_5()

juego.ver_jarras()

juego.vaciar_jarra_3()
juego.ver_jarras()

juego.verter_5_en_3()
juego.ver_jarras()

juego.verter_3_en_5()
juego.ver_jarras()


