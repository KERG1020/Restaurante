from Clases.Menu import Menu
from Clases.Venta import Venta
from Clases.Estadistica import Estadistica
opcion=0
while(opcion!=4):
    print("__________________________________")
    print("              Menú                ")
    print("__________________________________")
    print("1--> Admin. \n2--> Cliente \n3--> Estadistica  \n4--> SALIR ")
    print("__________________________________")
    opcion=int(input("Digite la opción deseada: "))

    if(opcion==1):
        i=0
        oMenu = Menu()
        file = open("archivos/menu.txt")
        oMenu.cant=input("Digite la cantidad de menús que va a registrar:   ")
        file.write(str(oMenu.cant)+'\n' )
        cantidad=int(oMenu.cant)
        for i in range(cantidad):
            oMenu.precio=input("Digite el precio del menu: ")
            file.write(str(oMenu.precio)+'\n' )
        file.close()
        
    elif(opcion==2):
        nMenus = len(open("archivos/menu.txt").readlines())
        k=0
        repetir=0
        archivoVentas = open("archivos/ventas.txt", "w")
        while(repetir==0):
            oVenta= Venta(nMenus)     
            oVenta.hora=input("Digite el la hora de la venta: ")
            oVenta.menus=input("Digite la cantidad de menus que va a comprar: ")
            bufer=""
            for k in range(oVenta.menus):
                oVenta.menu=input("Digite el menu:")
                menu=oVenta.menu+","
                bufer= bufer+ menu
            archivoVentas.write(oVenta.hora +","+bufer.rstrip(",") +'\n')
            volver=input("Si desea agregar otra venta digite 0, de lo contrario digite 1")
            if(volver=="1"):
                repetir=1
        archivoVentas.close()

    elif(opcion==3):
        opcionEst=0
        while(opcionEst!=6):
            print("__________________________________")
            print("              Menú                ")
            print("__________________________________")
            print("1--> Ver menus vendidos al dia. \n2--> Ver ventas por menu \n3--> Ver total vendido  \n4--> Ver menu mas vendido y menos vendido \n5--> Ver ventas Hora \n6-->Volver al menu principal")
            print("__________________________________")
            opcionEst=int(input("Digite la opción deseada: "))

            oEstadistica= Estadistica()
            menus=              oEstadistica.guardarMenu()
            ventasTotalesDia=   oEstadistica.guardarVentas()
            cantidadVentas=     oEstadistica.hacerInventario(menus,ventasTotalesDia)
            subtotales=         oEstadistica.ventasPorMenu(cantidadVentas,menus)
            total=              oEstadistica.ventaTotal(subtotales)
            menuMasVendido=     oEstadistica.calcularMasVendidos(cantidadVentas)
            menuMenosVendido=   oEstadistica.calcularMenosVendidos(cantidadVentas)
            

            if(opcionEst==1):
                print(cantidadVentas)
            
            elif(opcionEst==2):
                print(subtotales)

            elif(opcionEst==3):
                print(total)

            elif(opcionEst==4):
                print(f"el menu mas vendido fue: {menuMasVendido} y el menos vendido es {menuMenosVendido}")
            
            elif(opcionEst==5):
                oEstadistica.rango=input("digite la hora en la que  (1:00/2:00/1:30)")
                ventasPorHora=      oEstadistica.calcularVentasHora(oEstadistica.rango, ventasTotalesDia,menus)
                print(f"Las ventas hechas en la hora {oEstadistica.rango}: {ventasPorHora}")
            else:
                print("opcion no valida")
            
       
        
        
        
       
