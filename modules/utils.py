def obtener_cantidad(x:str)->int:
    try:
        return int(x)
    except:
        print('la cantidad ingresada no representa un entero, se asigna 0 como valor por defecto')
        return 0