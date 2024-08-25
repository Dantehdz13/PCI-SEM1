#proyecto de Programación: Convertidor de unidades.
#Dante Hernández Ramírez.
#Inicio del proyecto: Vie 23 de Ago de 2024.

#.........................................................................................................

#declaración de la primer variable general.
opcion1=float(input("Selecciona una unidad de medida o de peso: \n 1.metros \n 2.litros \n 3.temperatura (celcius y kelvin) \n 4.gramos \n"))

#.........................................................................................................

#después de haber leído la opción general, dependiendo de la misma, se le pedirá que seleccione la medida o cantidad que tenga el usuario, y a continuación a cual quiere convertirla.
if opcion1==1:
    medida=float(input("¿Qué unidad de medida deseas convertir? \n 1.km \n 2.m \n 3.cm \n 4.mm \n"))
    medida2=float(input("ingrese el valor numérico de la nedida: \n"))

#Hacer la conversión según la medida seleccionada...
    if medida==1:
        m= medida2*1000
        mm=medida2*1000000
        cm=medida2*100000
        print (f"El valor de la medida en metros es {m}, en milímetros es {mm} y en centímetros es {cm}")
#elif se usa como un else if, pero resumido.
    elif medida==2:
        km= medida2/1000
        mm=medida2*1000
        cm=medida2*100
        print (f"El valor de la medida en kilometros es {km}, en milímetros es {mm} y en centímetros es {cm}")
        
    elif medida==3:
        km= medida2/100000
        m=medida2/100
        mm=medida2*10
        print (f"El valor de la medida en kilometros es {km}, en metros es {m} y en milímetros es {mm}")  

    elif medida==4:
        km= medida2/1000000
        m=medida2/1000
        cm=medida2/10
        print (f"El valor de la medida en kilometros es {km}, en metros es {m} y en centímetros es {cm}")  
#Para cualquier otra opción fuera de el rango de 1 a 4, terminará la operación automáticamente.  
    else:
        print("Opción no válida, la operación ha terminado.")