# Your code here
def sequence_of_words(palabras):
    lista_palabras = palabras.split(",")
    ordenar_palabras = sorted(lista_palabras)
    resultado = ', '.join(ordenar_palabras)
    print(resultado)
sequence_of_words("without,hello,bag,world")