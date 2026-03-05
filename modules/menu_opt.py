from modules.utils import obtener_cantidad

def ingresar_libro(libros:dict)->dict:
    print('Ingresar libro')
    nombre = input('Ingrese el nombre del libro: ')
    cantidad = obtener_cantidad(input('Ingrese cantidad disponible: '))
    categoria = input('Ingrese la categoria (Matematicas,Novela,Sci-Fi,Auto-ayuda,etc): ')
    if not libros.get(nombre):
        libros[nombre]= {'cantidad':cantidad,'categoria':categoria}
        input('Libro creado con exito. Presiona Enter para continuar ...')
        return
    input('Libro ya existe en la base de datos.Presiona Enter para continuar.')
    

def actualizar_cantidades(libros:dict):
    libro,nombre = buscar_por_nombre(libros)
    if not libro:
        print('No existe el libro en el inventario')
        input('Presione Enter para continuar ...')
        return
    libro['cantidad'] = obtener_cantidad(input(('Ingrese cantidad disponible: ')))
    input(f'Se actualizo las cantidades del libro {nombre} exitosamente, hay {libro['cantidad']} unds. presione Enter para continuar')
        

def mostrar_inventario(libros:dict)->None:
    print('Inventario actual de Libros')
    for l in libros.keys():
        libro = libros.get(l)
        print(f'Libro: {l}, Cantidad: {libro.get('cantidad')}, Categoria: {libro.get('categoria')}')
    input('Presione Enter para continuar ...')

def buscar_por_nombre(libros):
    print('Buscar libro por nombre')
    nombre = input('Ingrese el nombre del libro: ')
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
            input(f'Se presto el libro {nombre} exitosamente, quedan {libro['cantidad']} unds. presione Enter para continuar')
            return
        input('No hay suficiente cantidad para prestar el libro. Presione Enter para continuar...')
        return
    input('No existe el libro buscado. Presione Enter para continuar ...')
    return