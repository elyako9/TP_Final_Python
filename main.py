from getdata import actualizaracciones
from resudata import resumen

while True: ##while para el programa se ejecute 
  op = int(input("Elija una acción:\n1.Actualización de datos\n2.Visualización de datos\nPara salir presione cualquier otro número\n"))
  if op == 1:
    actualizaracciones()
    #copiaradb(data)
    print('Los datos se actualizaron exitosamente')

  elif op == 2:
    visu = int(input("Elija tipo de visualización:\n1.Resumen\n2.Grafico\n3.Para volver al menu anterior\n"))
    
    if visu == 1:
      print('Datos almacenados en Base de Datos:')
      resumen()

    elif visu == 2:
      print("disparar funcion 2")      
  
  else:
    break
