#Archivo principal - Menú
import Funciones
import time
while True:
        print("\n*** Menú Empresa RVR ***\n1.-Registrar trabajador\n2.-Listar todos los trabajadores\n3.-Imprimir planilla de sueldos\n4.-Salir del programa\n")
        try:
            opcion=int(input("Seleccione una opción: "))
        except:
            print("**Error** ingrese un número")
        else:
            if opcion==1:
                Funciones.registrarTrabajador()
            elif opcion==2:
                Funciones.listaTodosLosTrabajadores()
            elif opcion==3:
                Funciones.planillaSueldo()
            elif opcion==4:
                print("Saliendo del programa...")
                time.sleep(3)
                break
            else:
                print("Opción no valida")