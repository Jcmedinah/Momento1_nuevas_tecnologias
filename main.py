from modules.menu_opt import *

def main():

    libros = {}

    menu = True
    while menu:
        print('Gestion de Libros Edulend\n' \
        '1. Ingresar libro\n' \
        '2. Actualizar cantidades\n' \
        '3. Mostrar inventario\n' \
        '4. Buscar libro por nombre\n' \
        '5. Prestar libro\n'\
        '6. Salir.')
        opcion = int(input('Selecciona una opcion:'))
        match opcion:
            case 1:
                ingresar_libro(libros)
            case 2:
                actualizar_cantidades(libros)
            case 3:
                mostrar_inventario(libros)
            case 4:
                print(buscar_libro_por_nombre(libros))
            case 5:
                prestar_libro(libros)
            case 6:
                print('Saliendo')
                menu = False


if __name__ == '__main__':
    main()