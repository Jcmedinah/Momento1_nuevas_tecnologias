from modules.utils import obtener_cantidad

def ingresar_libro(libros:dict)->dict:
    print('Ingresar libro')
    nombre = input('Ingrese el nombre del libro: ')
    cantidad = obtener_cantidad(input('Ingrese cantidad disponible: '))
    categoria = input('Ingrese la categoria (Matematicas,Novela,Sci-Fi,Auto-ayuda,etc): ')
    libros[nombre]= {'cantidad':cantidad,'categoria':categoria}

def actualizar_cantidades(libros:dict):
    libro,nombre = buscar_por_nombre(libros)
    if not libro:
        print('No existe el libro en el inventario')
        input('Presione Enter para continuar ...')
        return
    libro['cantidad'] = obtener_cantidad(input(('Ingrese cantidad disponible: ')))
        

def mostrar_inventario(libros:dict)->None:
    print('Inventario actual de Libros')
    for l in libros.keys():
        libro = libros.get(l)
        print(f'Libro: {l}, Cantidad: {libro.get('cantidad')}, Categoria: {libro.get('categoria')}')
    input('Presione Enter para continuar ...')

def buscar_por_nombre(libros):
    print('Buscar libro por nombre')
    nombre = input('Ingrese el nombre del libro')
    return libros.get(nombre),nombre
    
def buscar_libro_por_nombre(libros:dict)->None:
    libro,nombre = buscar_por_nombre(libros)
    if libro:
        return f'Libro: {nombre}, Cantidad: {libro.get('cantidad')}, Categoria: {libro.get('categoria')}'
    return 'No se encontro el libro'

def prestar_libro(libros):
    libro,nombre = buscar_por_nombre(libros)
    if libro:
        if libro['cantidad'] > 0:
            libro['cantidad']-=1
