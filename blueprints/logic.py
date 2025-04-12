from collections import deque
import heapq
from blueprints.grafo import mapa


def busca_largura(mapa, origem, destino):
    fila = deque([(origem, [origem], 0)])
    visitados = set()
    while fila:
        atual, caminho, custo = fila.popleft()
        if atual == destino:
            return caminho, custo, len(visitados)
        visitados.add(atual)
        for vizinho, distancia in mapa[atual].items():
            if vizinho not in visitados:
                fila.append((vizinho, caminho + [vizinho], custo + distancia))
    return None, float('inf'), len(visitados)

def busca_profundidade(mapa, origem, destino):
    pilha = [(origem, [origem], 0)]
    visitados = set()
    while pilha:
        atual, caminho, custo = pilha.pop()
        if atual == destino:
            return caminho, custo, len(visitados)
        visitados.add(atual)
        for vizinho, distancia in mapa[atual].items():
            if vizinho not in visitados:
                pilha.append((vizinho, caminho + [vizinho], custo + distancia))
    return None, float('inf'), len(visitados)

# def busca_a_estrela(mapa, heuristica, origem, destino):
#     fila = [(heuristica.get(origem, 0), 0, origem, [origem])]
#     visitados = set()
#     while fila:
#         f, g, atual, caminho = heapq.heappop(fila)
#         if atual == destino:
#             return caminho, g, len(visitados)
#         if atual in visitados:
#             continue
#         visitados.add(atual)
#         for vizinho, distancia in mapa[atual].items():
#             novo_g = g + distancia
#             novo_f = novo_g + heuristica.get(vizinho, 0)
#             heapq.heappush(fila, (novo_f, novo_g, vizinho, caminho + [vizinho]))
#     return None, float('inf'), len(visitados)

def executar_buscas(origem, destino):
    resultados = []
    caminho, custo, visitados = busca_largura(mapa, origem, destino)
    resultados.append(("Busca em Largura", caminho, custo, visitados))

    caminho, custo, visitados = busca_profundidade(mapa, origem, destino)
    resultados.append(("Busca em Profundidade", caminho, custo, visitados))

    # caminho, custo, visitados = busca_a_estrela(mapa, heuristica, origem, destino)
    # resultados.append(("Busca A*", caminho, custo, visitados))
    print(resultados)
    return resultados

# # Execução principal
# if __name__ == "__main__":
#     origem = input("Digite a cidade de origem: ").strip().title()
#     destino = input("Digite a cidade de destino: ").strip().title()

#     resultados = executar_buscas(origem, destino)

#     for metodo, caminho, custo, visitados in resultados:
#         print(f"\n{metodo}:")
#         print(f"Caminho: {caminho}")
#         print(f"Custo total: {custo}")
#         print(f"Cidades visitadas: {visitados}")
