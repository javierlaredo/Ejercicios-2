'''Ejercicio 3
Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:
Borrar los elementos duplicados.
Ordenar la lista de mayor a menor.
Eliminar todos los números impares.
Realizar una suma de todos los números que quedan.
Añadir como primer elemento de la lista la suma realizada.
Devolver la lista modificada.
Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista, tal que así:
nueva_lista = modificar(lista)
print( nueva_lista[0] == sum(nueva_lista[1:]) )
True'''

elementos= [1, 6, 9, 4, 11, 67, 3, 6, 67]

def modificar(lista):
    conjunto = set(lista)   #Borrar duplicados
    lista = list(conjunto)
    
    lista.sort(reverse=True) #Ordenar de mayor a menor

    pares = []
    for n in lista:             #Como quieres eliminar los impares, solo coges los pares
        if n%2 == 0:
            pares.append(n)

    suma= sum(pares)    
    pares.insert(0, suma)   #Añado en la posición 0 la suma de los pares

    return pares

nueva_lista = modificar(elementos)
print(nueva_lista)
print(nueva_lista[0] == sum(nueva_lista[1:]))    


    
    



