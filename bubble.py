#Compara un elemnto del vetor con el elemnto siguinte y lo va moviendo de lugar si es mayor


#Inicializimos el vector con los valores de la lista
vector = [1 , 3 , 5 , 4 , 2 , 6 , 55 , 955 , 5555]

"""
=> Creamos un for anidado, despues creamos una variable donde guardaremos la cantidad de elemntos del vector,
posteiormente creamos una condicion la cual comparara si el elemneto actual es mayor que el siguinte, si es asi guardara
ese valor en una variable y se lo asiganra a la posicion del vector que corresponde a la posicion del elemnto actualy la 
posicon actual del vector s ele asiganara a la posicion del siguinte, y asi se va haciendo hasta que no se cumpla el vector ordenado
"""
def burbuja (arr):
    num_vector = len(vector)
    for i in range(num_vector - 1):    
        for j in range(num_vector - 1):
            if arr[j] > arr[j + 1]:
                nv = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = nv


#Llamamos a la funcion burbuja
burbuja(vector)


#Imprimimos la fucion
print(f"El vector ordenado: {vector}")

