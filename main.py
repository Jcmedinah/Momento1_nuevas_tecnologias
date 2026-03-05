def ingresar_libro(libros:dict)->dict:
    print('Ingresar libro')
    nombre = input('Ingrese el nombre del libro: ')
    cantidad = int(input('Ingrese cantidad disponible: '))
    categoria = input('Ingrese la categoria (Matematicas,Novela,Sci-Fi,Auto-ayuda,etc): ')
    libros[nombre]= {'cantidad':cantidad,'categoria':categoria}
    return libros

def actualizar_cantidades():
    pass

def mostrar_inventario(libros:dict)->None:
    print('Inventario actual de Libros')
    for l in libros.keys():
        libro = libros[l]
        print(f'Libro:{l}, Cantidad: {libro.get('cantidad')}, Categoria: {libro.get('categoria')}')
    input('Presione Enter para continuar ...')

def buscar_libro_por_nombre():
    pass

def prestar_libro():
    pass

def main():

    libros = {}

    menu = True
    while menu:
        print('Gestion de Libros Edulend\n' \
        '1. Ingresar libro\n' \
        '2. Actualizar cantidades\n' \
        '3. Mostrar inventario\n' \
        '4. Buscar libro por nombre\n' \
        '5. Salir.')
        opcion = int(input('Selecciona una opcion:'))
        match opcion:
            case 1:
                libros = ingresar_libro(libros)
            case 2:
                print('Actualizar cantidades')
            case 3:
                mostrar_inventario(libros)
            case 4:
                print('Buscar libro por nombre')
            case 5:
                print('Saliendo')
                menu = False


if __name__ == '__main__':
    main()