from getdata import pedirdatos

while True: ##while para el programa se ejecute 
  op = int(input("Elija una acción:\n1.Actualización de datos\n2.Visualización de datos\nPara salir presione cualquier otro número\n"))
  if op == 1:
    # ticker = str(input("ingrese el nombre de la Acción:"))
    # fecha_ini = str(input("ingrese la fecha de inicio:"))
    # fecha_cierre = str(input("ingrese la fecha de fin:"))
    # print(f"Accion {ticker} desde {fecha_ini} hasta {fecha_cierre}")
    data = pedirdatos()
    print(data)
  elif op == 2:
    visu = int(input("Elija tipo de visualización:\n1.Resumen\n2.Grafico\n3.Para volver al menu anterior\n"))
    #print("opcion 2") #cuando sale un de estas que dispare una funcion o objero no se para hacer la grafica
    if visu == 1:
      print("disparar funcion 1")
    elif visu == 2:
      print("disparar funcion 2")      
  else:
    break
