def find(padre, nodo):
    if padre[nodo] != nodo:
        padre[nodo] = find(padre, padre[nodo])
    return padre[nodo]

def union(padre, rango, a, b):
    ra = find(padre, a)
    rb = find(padre, b)
    if ra != rb:
        if rango[ra] < rango[rb]:
            padre[ra] = rb
        elif rango[ra] > rango[rb]:
            padre[rb] = ra
        else:
            padre[rb] = ra
            rango[ra] += 1

def kruskal(nodos, aristas):
    padre = {n: n for n in nodos}
    rango = {n: 0 for n in nodos}
    mst = []

    aristas = sorted(aristas, key=lambda x: x[2])

    for u, v, peso in aristas:
        if find(padre, u) != find(padre, v):
            union(padre, rango, u, v)
            mst.append((u, v, peso))

    return mst


nodos = ['A', 'B', 'C', 'D']
aristas = [
    ('A', 'B', 1),
    ('B', 'C', 2),
    ('A', 'C', 3),
    ('C', 'D', 4)
]

print(kruskal(nodos, aristas))