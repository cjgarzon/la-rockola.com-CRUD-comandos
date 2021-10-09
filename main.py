import canciones

menu='''\n****************************
*       MENU CANCIONES        *
****************************
*                          *
*  i) Insertar Canción     *
*  e) Eliminar Canción     *
*  m) Modificar Canción    *
*  p) Imprimir Canciones   *
*  b) Buscar Canción       *
*  x) Salir                *
*                          *
****************************'''

def main():

    opcion='0'
    while opcion !='X':
        print(menu)
        opcion = input("¿Que opción deseas?: ").upper()
        print()
        if opcion == 'I':
            print("*****  Insertar Canción  *****")
            NombreCancion = input("Introduce el nombre de la nueva canción: ")
            NombreArtista = input("Introduce el nombre del artista: ")
            GeneroCancion = input("Introduce el género: ")
            AnioPubli = input("Introduce el año de publicación: ")
            EnlaceCancion = input("Introduce el enlace: ")
            r = canciones.inserta_cancion(NombreCancion,NombreArtista,GeneroCancion,AnioPubli,EnlaceCancion)
            if(r==0):
                print("-> No se pudo insertar la canción...")
            else:
                print("-> La canción se insertó correctamente")
        elif opcion == 'E':
            print("*****  Eliminar Canción  *****")
            IdCan = int(input("Introduce el Id de la canción que desea eliminar: "))
            r = canciones.elimina_cancion(IdCan)
            if(r==0):
                print("-> La canción con ese Id no existe")
            else:
                print("-> La canción se eliminó correctamente")
        elif opcion == 'M':
            print("*****  Modificar Canción  *****")
            IdCan = int(input("Introduce el Id de la canción que desea modificar: "))
            cancionmod = canciones.buscar_id(IdCan)
            if cancionmod == None:
                print("-> La canción con ese Id no existe")
            else:
                print("*** Canción a modificar: ")
                print(cancionmod)
                print()
                NombreCancion = input("Introduce el nuevo nombre de la canción: ")
                NombreArtista = input("Introduce el nuevo nombre del  artista: ")
                GeneroCancion = input("Introduce el nuevo genero de la cancion: ")
                AnioPubli = input("Introduce el nuevo año de publicación: ")
                EnlaceCancion = input("Introduce el nuevo enlace de la canción: ")
                r = canciones.modifica_cancion(IdCan,NombreCancion,NombreArtista,GeneroCancion,AnioPubli,EnlaceCancion)
                if(r==0):
                    print("-> Error al modificar la canción...")
                else:
                    print("-> La canción se modificó correctamente")

        elif opcion == 'P':
            print("*****  Imprimir Canciones  *****")
            canciones.consulta_canciones()
        elif opcion == 'B':
            print("*****  Buscar canción  *****")
            IdCan = input("Introduce el Id de la canción a buscar: ")
            canciones.buscar_id(IdCan)
            if IdCan == None:
                print("-> La canción con ese Id no existe")
            else:
                print(canciones.buscar_id(IdCan))
        elif opcion == 'X':
            print("-> Saliendo del sistema")
        else:            
            print("-> Opción no válida")



if __name__ == "__main__":
    main()
