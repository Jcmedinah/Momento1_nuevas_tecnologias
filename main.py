from modules.utils import obtener_cantidad

def ingresar_libro(libros:dict)->dict:
    print('Ingresar libro')
    nombre = input('Ingrese el nombre del libro: ')
    cantidad = obtener_cantidad(input('Ingrese cantidad disponible: '))
    categoria = input('Ingrese la categoria (Matematicas,Novela,Sci-Fi,Auto-ayuda,etc): ')
    libros[nombre]= {'cantidad':cantidad,'categoria':categoria}

def actualizar_cantidades(libros:dict):
    print('Buscar libro por nombre')
    nombre = input('Ingrese el nombre del libro')
    libro = libros.get(nombre)
    if not libro:
        print('No existe el libro en el inventario')
        input('Presione Enter para continuar ...')
        return
    libro['cantidad'] = int(input(('Ingrese cantidad disponible: ')))
        

def mostrar_inventario(libros:dict)->None:
    print('Inventario actual de Libros')
    for l in libros.keys():
        libro = libros.get(l)
        print(f'Libro: {l}, Cantidad: {libro.get('cantidad')}, Categoria: {libro.get('categoria')}')
    input('Presione Enter para continuar ...')

def buscar_libro_por_nombre(libros:dict)->None:
    print('Buscar libro por nombre')
    nombre = input('Ingrese el nombre del libro')
    libro = libros.get(nombre)
    if libro:
        return f'Libro: {nombre}, Cantidad: {libro.get('cantidad')}, Categoria: {libro.get('categoria')}'
    return 'No se encontro el libro'

def prestar_libro(libros):
    print('Buscar libro por nombre')
    nombre = input('Ingrese el nombre del libro')
    libro = libros.get(nombre)
    if libro:
        if libro['cantidad'] > 0:
            libro['cantidad']-=1

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