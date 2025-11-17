def floyd(matriz):
    n = len(matriz)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matriz[i][k] + matriz[k][j] < matriz[i][j]:
                    matriz[i][j] = matriz[i][k] + matriz[k][j]
    return matriz


INF = 99999
matriz = [
    [0,   3,   INF, 5],
    [2,   0,   INF, 4],
    [INF, 1,   0,   INF],
    [INF, INF, 2,   0]
]

resultado = floyd(matriz)
for fila in resultado:
    print(fila)