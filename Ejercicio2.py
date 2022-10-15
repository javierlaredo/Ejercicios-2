'''Ejercicio 2
Utilizando todo lo que sabes sobre cadenas, listas, sus métodos internos... Transforma este texto:

un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro

En este otro:

Un día que el viento soplaba con fuerza...

- Mira como se mueve aquella banderola -dijo un monje.

- Lo que se mueve es el viento -respondió otro monje.

- Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.'''

texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

def separar(frase):
    nuevo_texto=texto.split("#")
    return nuevo_texto

def mayusculas(frase):
    resultado =''
    for i in frase:
        resultado += i[0].upper()
    return resultado

texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"
print(texto)
print(mayusculas)