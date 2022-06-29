class Menu:
     
  def __init__(self):
      self.__cant=None
      self.__precio=None
 
#Getters
  @property
  def cant(self):
      return(self.__cant)
  @property
  def precio(self):
      return(self.__precio)


  #Setters
  @cant.setter
  def cant(self, cant):
      try:
            cantv=int(cant)
            self.__cant=cantv
      except:
          print("La cantidad debe ser un numero")

  @precio.setter
  def precio(self, precio):
      try:
            preciov=float(precio)
            self.__precio=preciov
      except:
          print("El precio debe ser un numero")

          
    