vector = [1 , 3 , 2 , 5 , 7]

def sort(vector):
    #Creamos variables las cuales las usaremos como listas donde almacenaremos los elementos del vector
    pivot = vector[0]  # El pivote es el primer elemento.
    izq = []
    der = []

    """
    Creamos un for donde compararemos los valores del vector si el numero es menor al pivote se 
    lo va a la lista izq, pero si es mayor se lo va a la lista der, despues de hacer esto se va haciendo
    el pivote con el valor que tenga el indice mas alto, y se va haciendo hasta que no se cumpla el vector ordenado
    """
    for i in range(1,len(vector)):
        if vector[i] < pivot:
            izq.append(vector[i])  # Elementos menores van a la lista `izq`.
        else:
            der.append(vector[i]) # Elementos mayores o iguales van a `der`.
            
    return izq , pivot , der

def quick (vector):
    if len(vector) < 2:
        return vector
    
    izq , pivot, der = sort(vector)
    return quick(izq) + [pivot] + quick(der)


print(quick(vector))
