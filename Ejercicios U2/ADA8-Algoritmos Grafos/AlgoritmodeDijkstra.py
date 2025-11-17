def dijkstra(grafo, inicio):
    dist = {nodo: float('inf') for nodo in grafo}
    dist[inicio] = 0
    visitados = set()

    while len(visitados) < len(grafo):
        nodo_actual = None
        for nodo in grafo:
            if nodo not in visitados:
                if nodo_actual is None or dist[nodo] < dist[nodo_actual]:
                    nodo_actual = nodo

        visitados.add(nodo_actual)

        for vecino, peso in grafo[nodo_actual].items():
            nueva_dist = dist[nodo_actual] + peso
            if nueva_dist < dist[vecino]:
                dist[vecino] = nueva_dist

    return dist


grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'B': 1, 'D': 8},
    'D': {}
}

print(dijkstra(grafo, 'A'))