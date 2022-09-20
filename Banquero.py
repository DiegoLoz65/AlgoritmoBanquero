from colorama import init, Fore, Back
import string
#Definición de Vector de Disponibles
def VectorDisponibles(MAA, A, E):
    i=0
    A=[]
    while i < len(MAA[0]):
        sum = 0
        for j in MAA:
            sum += j[i]
        A.append(E[i] - sum)
        i += 1
    return A

def DefinirProceso(MS, A):
    NumeroProceso = 0
    
    for i in MS:
        if i == A:
            return NumeroProceso
        NumeroProceso += 1

    NumeroProceso = 0
    for i in MS:
        count = 0
        ceros = 0
        for j in i:
            if j == 0:
                ceros += 1
            if j > A[count]:
                break
            if count == 3 and ceros != len(MS[0]):
                return NumeroProceso
            count += 1
        NumeroProceso += 1
    return -1

def Despacho(MAA, MS, P):
    i=0
    while i < len(MAA[P]):
        MAA[P][i] += MS[P][i]
        i += 1
    return MAA

def PostDespacho(MAA, MS, P):
    i = 0
    while i < len(MAA[P]):
        MAA[P][i] = 0
        MS[P][i] = 0
        i += 1
    return MAA

def LetraABC(P):
    abc = list(string.ascii_uppercase)
    return abc[P]


def main():
    init()
    #Vector de Recursos Existentes
    E = [6, 3, 4, 2]

    #Matriz de Solicitudes
    MS = [[1,1,0,0], [0,1,1,2], [3,1,0,0], [0,0,1,0], [2,1,1,0]]

    #Matriz de Asignación Actual Inicial
    MAA = [[3,0,1,1], [0,1,0,0], [1,1,1,0], [1,1,0,1], [0,0,0,0]]

    #Vector de Disponibles
    A = []

    #Proceso definido
    P = []

    iteracion = 1
    fin = False
    print(Fore.GREEN +"\nBienvenido a la representación del algoritmo del banquero \n")
    print(Fore.RED+ "El vector de recursos existentes es: E =" , E)
    A = VectorDisponibles(MAA, A, E)
    print("El vector de disponibles es: A = " , A, "\n")
    print("La matriz de solicitudes es: ", *MS , sep='\n')
    print("La matriz de asignación actual es: ", *MAA , sep='\n')
    
    

    print(Fore.CYAN + "\nSe comienza a despachar: \n")
    contador = 0
    while fin == False and contador < 5:
        contador += 1
        P = DefinirProceso(MS, A) 
        if P == -1:
            print("NO ES POSIBLE ATENDER EL PROCESO")
            exit()
        print(Fore.MAGENTA + " --------  Iteración #" , iteracion, "  --------")
        iteracion += 1
        letraProceso = LetraABC(P)
        print("Se despacha el proceso: ", letraProceso)
        print("Antes de ejecutar el proceso ", letraProceso)
        MAA = Despacho(MAA, MS, P)
        A = VectorDisponibles(MAA, A, E)
        print("Existentes = ", E, "     A = ", A)


        print("Matriz de Asignación Actual: " , *MAA , sep='\n')
        print("Matriz de Solicitudes: ", *MS , sep='\n')
        print(Fore.CYAN + "\nDespues de ejecutar el proceso ", letraProceso)
        MAA = PostDespacho(MAA, MS, P)
        A = VectorDisponibles(MAA, A, E)
        print("Existentes = ", E, "     A = ", A)
        print("Matriz de Asignación Actual: " , *MAA , sep='\n')
        print("Matriz de Solicitudes: ", *MS , sep='\n')
        print("\n\n")

        if MS == [[0,0,0,0], [0,0,0,0], [0,0,0,0]]:
            print(Fore.GREEN + "¡EL ESTADO INICIAL ES SEGURO!")
            fin = True

main()


