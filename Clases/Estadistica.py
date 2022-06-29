class Estadistica:
  
  def __init__(self):
    self.__rango=None

  @property
  def rango(self):
      return(self.__rango)

  #Setters
  @rango.setter
  def rango(self, rango):
      self.__rango=rango
     

  #HAGO EL DICCIONARIO QUE RELACIONA MENU CON PRECIOS
  def guardarMenu(self):
    archivoMenus=open("archivos/menu.txt")
    menus={}
    contador=0
    for renglon in archivoMenus:
      precioMenu=renglon.rstrip(",\n")
      menus['m'+str(contador)]=float(precioMenu)
      contador+=1 
    #elimino la cantidad de menus del arreglo
    menus.pop("m0")
    return(menus)
    #print menus {'m1': 2000.0, 'm2': 3000.0, 'm3': 6000.0}

  #HAGO EL ARREGLO QUE TIENE LAS VENTAS TOTALES DEL DIA POR HORA, CADA VENTA ES UN DICCIONARIO
  def guardarVentas(self):
    archivoVentas = open("archivos/ventas.txt")
    ventas={}
    ventasTotalesDia=[]
    for renglon in archivoVentas:
      venta =renglon.split(",") 
      venta= list(map(lambda l:l.rstrip(",\n"), venta))
      ventas["hora"]=venta[0]
      venta.pop(0)
      ventas["menus"]=venta
      ventasTotalesDia.append(ventas)
      ventas={}
    return(ventasTotalesDia)
    #print ventasTotalesDia[{'hora': '12:30', 'menus': ['m1', 'm2', 'm3']}, {'hora': '12:30', 'menus': ['m4', 'm1']}, {'hora': '4:50', 'menus': ['m2', 'm2']}] 

  #HAGO DICCIONARIO QUE RELACIONA CANTIDAD DE MENU VENDIDOS CON MENUS
  def hacerInventario(self,menus,ventasTotalesDia):
    cantidad=0
    cantidadVentas={}
    i=0
    #recorrer los menus que tienen precios
    for menu in menus:
      i+=1
    #recorrerlas todas las ventas del dia
      for venta in ventasTotalesDia:
        #recorrer las ventas por mesa
        for menusVenta in venta["menus"]:
          if menusVenta==menu:
            cantidad+=1
      cantidadVentas['m'+str(i)]=cantidad
      cantidad=0    
    return(cantidadVentas)
    #print cantidadVentas {'m1': 2, 'm2': 3, 'm3': 1}

  def ventasPorMenu(self,cantidadVentas,menus):
    subtotales={}
    for ventas in cantidadVentas:#cantidad
      for menu in menus:#precios
        if ventas==menu:
          subtotales[menu]=menus[menu]*cantidadVentas[ventas]
    return subtotales
  #print subtotales {'m1': 4000.0, 'm2': 9000.0, 'm3': 6000.0}
        
  def ventaTotal(self,subtotales):
    total=0
    for subtotal in subtotales:
      total+=subtotales[subtotal]
    return(total)
  #print total 19000.0

  def calcularMasVendidos(self,cantidadVentas):
    masVendidos = sorted(cantidadVentas,key = lambda cantidadVenta: cantidadVentas[cantidadVenta], reverse=True)
    return(masVendidos[0])

  def calcularMenosVendidos(self,cantidadVentas):
    menosVendidos = sorted(cantidadVentas,key = lambda cantidadVenta: cantidadVentas[cantidadVenta])
    return(menosVendidos[0])

  def calcularVentasHora(self,rango,ventasTotalesDia,menus):
    menusVendidosRango=[] 
    i=0
    totalVendidoRango=0
    #recorrerlas todas las ventas del dia
    for venta in ventasTotalesDia:
      if rango==venta["hora"]:
        for menusVenta in venta["menus"]:
          menusVendidosRango.append(menusVenta)

    if menusVendidosRango==[]:
      mensaje="no hubo ventas"
    else:
      for menu in menusVendidosRango:
        for m in menus:
          if m==menu:
            totalVendidoRango+=menus[menu]

      mensaje=str(totalVendidoRango)
    return mensaje
    
