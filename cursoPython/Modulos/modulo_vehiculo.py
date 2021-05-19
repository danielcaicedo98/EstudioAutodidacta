class Vehiculos():

  def __init__(self,marca,modelo):
    self.marca= marca
    self.modelo= modelo
    self.enmarcha=False
    self.acelera=False
    self.frena=False

  def arrancar(self):
    self.enmarcha=True
 
  def frenar(self):
    self.frena=True

  def estado(self):
    print("Marca: ", self.marca,"\nModelo: ",self.modelo,
          "\nEn Marcha: ",self.enmarcha,"\nAcelerando: ",self.acelera,
          "\nFrenando: ", self.frena)
class Moto (Vehiculos):
  stunt=""
  
  def stuntt(self):
    self.stunt = "lift the motorbike"
    
  def estado(self):
    print("Marca: ", self.marca,"\nModelo: ",self.modelo,
          "\nEn Marcha: ",self.enmarcha,"\nAcelerando: ",self.acelera,
          "\nFrenando: ", self.frena, "\n",self.stunt)

class Furgoneta(Vehiculos):
  def carga(self, cargar):
    self.cargado=cargar
    if self.cargado:
      return "Esta cargada la furgo"
    else: 
      return "Furgoneta no cargada"  

class Electricos(Vehiculos):
  def __init__(self,_marca,_modelo):
    super().__init__(_marca,_modelo)
    self.autonomia=100
  def cargaEnergia(Self):
    self.cargando=True