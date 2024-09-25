#proyecto de Programación: Convertidor de unidades. Y más cosas debido a que tenemos que implementar todo lo visto en la clase...
#Dante Hernández Ramírez.
#Inicio del proyecto: Vie 23 de Ago de 2024.


opgen=int(input("Convertor de unidades e identifica si un número es primo o no B), selecciona una opcion:\n 1.Convertidor de unidades \n 2. Identificar si un número es primo\n"))

    #.........................................................................................................
if opgen==1:
    #declaración de la primer variable general.
    opcion1=float(input("Selecciona una unidad de medida o de peso: \n 1.metros \n 2.litros \n 3.temperatura (celcius y kelvin) \n 4.gramos \n"))

    #.........................................................................................................

    #después de haber leído la opción general, dependiendo de la misma, se le pedirá que seleccione la medida o cantidad que tenga el usuario, y a continuación a cual quiere convertirla.
    if opcion1==1:
        medida=float(input("¿Qué unidad de medida deseas convertir? \n 1.km \n 2.m \n 3.cm \n 4.mm \n"))
        medida2=float(input("ingrese el valor numérico de la medida: \n"))

    #Hacer la conversión según la medida seleccionada...
        if medida==1:
            m= medida2*1000
            mm=medida2*1000000
            cm=medida2*100000
            print (f"El valor de la medida en metros es {m}, en milímetros es {mm} y en centímetros es {cm} cm")
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
    #.........................................................................................................
    #Ahora la conversión a unidades de medida de volumen (litros, mililitros, etc.)
    elif opcion1 == 2:
        medida = float(input("¿Qué unidad de volumen deseas convertir? \n 1.L \n 2.ml \n 3.cl \n 4.dl \n"))
        medida2 = float(input("Ingrese el valor numérico del volumen: \n"))

        if medida == 1:
            ml = medida2 * 1000
            cl = medida2 * 100
            dl = medida2 * 10
            print(f"El valor del volumen en mililitros es {ml}, en centilitros es {cl} y en decilitros es {dl}")
        elif medida == 2:
            l = medida2 / 1000
            cl = medida2 / 10
            dl = medida2 / 100
            print(f"El valor del volumen en litros es {l}, en centilitros es {cl} y en decilitros es {dl}")
        elif medida == 3:
            l = medida2 / 100
            ml = medida2 * 10
            dl = medida2 / 10
            print(f"El valor del volumen en litros es {l}, en mililitros es {ml} y en decilitros es {dl}")
        elif medida == 4:
            l = medida2 / 10
            ml = medida2 * 100
            cl = medida2 * 10
            print(f"El valor del volumen en litros es {l}, en mililitros es {ml} y en centilitros es {cl}")
        else:
            print("Opción no válida, la operación ha terminado.")
    #.........................................................................................................
    # Ahora la conversión a unidades de peso (gramos, kilogramos, etc.)
    elif opcion1 == 4:
        medida = float(input("¿Qué unidad de peso deseas convertir? \n 1.kg \n 2.g \n 3.mg \n 4.T \n"))
        medida2 = float(input("Ingrese el valor numérico del peso: \n"))

        if medida == 1:
            g = medida2 * 1000
            mg = medida2 * 1000000
            t = medida2 / 1000
            print(f"El valor del peso en gramos es {g}, en miligramos es {mg} y en toneladas es {t}")
        elif medida == 2:
            kg = medida2 / 1000
            mg = medida2 * 1000
            t = medida2 / 1000000
            print(f"El valor del peso en kilogramos es {kg}, en miligramos es {mg} y en toneladas es {t}")
        elif medida == 3:
            kg = medida2 / 1000000
            g = medida2 / 1000
            t = medida2 / 1000000000
            print(f"El valor del peso en kilogramos es {kg}, en gramos es {g} y en toneladas es {t}")
        elif medida == 4:
            kg = medida2 * 1000
            g = medida2 * 1000000
            mg = medida2 * 1000000000
            print(f"El valor del peso en kilogramos es {kg}, en gramos es {g} y en miligramos es {mg}")
        else:
            print("Opción no válida, la operación ha terminado.")

    #.........................................................................................................
    # Por último la conversión de celcius a kelvin y viceversa
    elif opcion1 == 3:
        medida = float(input("¿Qué unidad de temperatura deseas convertir? \n 1.Kelvin \n 2.Celcius \n"))
        medida2=float(input("ingresa el valor numérico de los grados: \n"))

        if medida==1:
            c = medida2 - 273.15
            print(f"El valor de la temperatura en celcius es {c}")
        elif medida==2:
            k = medida2 + 273.15
            print(f"El valor de la temperatura en kelvin es {k}")
        else:
            print("Opción no válida, la operación ha terminado.")

    #.........................................................................................................
    # Si el usuario no selecciona una opción válida, aparecerá un mensaje de error...
    else:
        print("Opción invalida, el programa se va a cerrar.")



#Empezamos con la identificación de un número primo usando funciones y while...



if opgen==2:
 #identificar si un número es primo o no...   
    def primo(numero):
#si el número es menor o igual a 1, automáticamente lo descartamos...
        if numero <= 1:
            print("No es un número primo...")
        else:
            i = 2
            while i * i <= numero:
                if numero % i == 0:
                    print("no es un número primo...")
                    return
                i += 1
            print("es un número primo....")

numero = int(input("ingresa un número: \n"))
primo(numero)
    
