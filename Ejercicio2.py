'''Ejercicio 2
Utilizando todo lo que sabes sobre cadenas, listas, sus métodos internos... Transforma este texto:

un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro

En este otro:

Un día que el viento soplaba con fuerza...

- Mira como se mueve aquella banderola -dijo un monje.

- Lo que se mueve es el viento -respondió otro monje.

- Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.'''

texto = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

def separar(frases):
    texto_nuevo = texto.split("#")
    i = 0
    for frases in texto_nuevo:
        texto_nuevo[i] = frases.capitalize()
        if i == 0:
            texto_nuevo[i] = texto_nuevo[i] + "..."
            print(frases[i])
            i += 1
        else:
            texto_nuevo[i] = "-" + texto_nuevo[i] + "."
            print(frases[i])
            i +=1
            for frases in texto_nuevo:
                print(texto_nuevo)
separar(texto)