# Your code here
def list_and_tuple(*args):
    lista = [str(arg) for arg in args]
    tupla = tuple(lista)
    return lista, tupla
resultado_lista, resultado_tupla = list_and_tuple(34,67,55,33,12,98)
print(resultado_lista)
print(resultado_tupla)