
if __name__ == "__main__":
    #Variaveis
    N = int(input("Qual é a ordem da matriz? "))
    count: int = 0

    #Matriz
    matriz: float = [[0 for x in range(N)] for x in range(N)]

    #Digitando os numeros
    for i in range(0, N):
        for j in range(0, N):
            matriz[i][j] = float(input(f"Elemento[{i},{j}]: "))

            if (matriz[i][j] < 0):
                count+=1


    print("Diagonal principal: ", end="")
    for i in range(0, N):
        print(i, end=" ")

    print(f"Quantidade de negativos = {count}")
    

