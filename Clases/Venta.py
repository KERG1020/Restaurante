class Venta:

  def __init__(self,nMenus):
    self.__hora=None
    self.__menu=None
    self.__menus=None
    self.nMenus=nMenus

 #Getters
  @property
  def hora(self):
      return(self.__hora)
  @property
  def menu(self):
      return(self.__menu)

  @property
  def menus(self):
      return(self.__menus)


  #Setters
  @menus.setter
  def menus(self, menus):
      try:
            menusv=int(menus)
            self.__menus=menusv
      except:
          print("La cantidad de menus debe ser un numero")

  @hora.setter
  def hora(self, hora):
    self.__hora=hora
 
  @menu.setter
  def menu(self, menu):
    if (int(menu[1])>0 and int(menu[1])<self.nMenus):
      self.__menu=menu
    else: 
      print(f"No se puede hacer la venta porque el menu {menu} no esta registrado")
      self.__menu="m0"


          
