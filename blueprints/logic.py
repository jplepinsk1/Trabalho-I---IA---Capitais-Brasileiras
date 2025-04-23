from collections import deque
import heapq
from math import radians, sin, cos, sqrt, atan2
from blueprints.grafo import mapa

# Mapeamento de capital para estado
capital_estado = {
    'Rio Branco': 'AC', 'Maceió': 'AL', 'Manaus': 'AM', 'Salvador': 'BA',
    'Fortaleza': 'CE', 'Brasília': 'DF', 'Vitória': 'ES', 'Goiânia': 'GO', 'São Luís': 'MA',
    'Cuiabá': 'MT', 'Campo Grande': 'MS', 'Belo Horizonte': 'MG', 'Belém': 'PA', 'João Pessoa': 'PB',
    'Curitiba': 'PR', 'Recife': 'PE', 'Teresina': 'PI', 'Rio de Janeiro': 'RJ', 'Natal': 'RN',
    'Porto Alegre': 'RS', 'Porto Velho': 'RO', 'Boa Vista': 'RR', 'Florianópolis': 'SC',
    'São Paulo': 'SP', 'Aracaju': 'SE', 'Palmas': 'TO'
}

# Penalidade com base na qualidade da malha rodoviária
penalidade_estado = {
    "SP": 240.0, "AL": 1360.0, "DF": 1440.0, "MS": 1460.0, "GO": 1640.0, "RS": 1640.0, "SC": 1700.0,
    "ES": 1740.0, "SE": 1760.0, "RN": 1790.0, "PB": 1850.0, "PR": 1850.0, "RJ": 1890.0, "CE": 1930.0,
    "RR": 1970.0, "BA": 1990.0, "RO": 1990.0, "PI": 2050.0, "PE": 2060.0, "MA": 2110.0, "PA": 2110.0,
    "TO": 2120.0, "AC": 2150.0, "MG": 2190.0, "MT": 2250.0, "AP": 2440.0, "AM": 3180.0
}

# Coordenadas geográficas para distância em linha reta (Haversine)
coordenadas = {
    'Rio Branco': (-9.97499, -67.8243), 'Maceió': (-9.66599, -35.735), 'Manaus': (-3.10194, -60.025),
    'Salvador': (-12.9718, -38.5011), 'Fortaleza': (-3.71722, -38.5433), 'Brasília': (-15.7801, -47.9292),
    'Vitória': (-20.3155, -40.3128), 'Goiânia': (-16.6864, -49.2643), 'São Luís': (-2.53073, -44.3068),
    'Cuiabá': (-15.6014, -56.0974), 'Campo Grande': (-20.4486, -54.6295), 'Belo Horizonte': (-19.9167, -43.9345),
    'Belém': (-1.4554, -48.4902), 'João Pessoa': (-7.12022, -34.8804), 'Curitiba': (-25.4293, -49.2719),
    'Recife': (-8.0476, -34.877), 'Teresina': (-5.08921, -42.8016), 'Rio de Janeiro': (-22.9068, -43.1729),
    'Natal': (-5.79448, -35.211), 'Porto Alegre': (-30.0346, -51.2177), 'Porto Velho': (-8.76077, -63.8999),
    'Boa Vista': (2.8192, -60.6733), 'Florianópolis': (-27.5954, -48.548), 'São Paulo': (-23.5505, -46.6333),
    'Aracaju': (-10.9111, -37.0717), 'Palmas': (-10.2398, -48.3558)
}

# Função Haversine
def haversine(cidade1, cidade2):
    lat1, lon1 = coordenadas[cidade1]
    lat2, lon2 = coordenadas[cidade2]
    R = 6371
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

# Busca em Largura BFS
def busca_largura(mapa, origem, destino):
    fila = deque([(origem, [origem], 0)])
    visitados = set()
    while fila:
        atual, caminho, custo = fila.popleft()
        if atual == destino:
            return caminho, custo, len(visitados)
        visitados.add(atual)
        for vizinho, distancia in mapa[atual].items():
            estado = capital_estado.get(vizinho, "")
            penalidade = penalidade_estado.get(estado, 0)
            distancia_h = haversine(vizinho, destino)
            h = distancia_h + penalidade
            if vizinho not in visitados:
                fila.append((vizinho, caminho + [vizinho], custo + distancia))
    return None, float('inf'), len(visitados)

# Busca em Largura DFS
def busca_profundidade(mapa, origem, destino):
    pilha = [(origem, [origem], 0)]
    visitados = set()
    while pilha:
        atual, caminho, custo = pilha.pop()
        if atual == destino:
            return caminho, custo, len(visitados)
        visitados.add(atual)
        for vizinho, distancia in mapa[atual].items():
            estado = capital_estado.get(vizinho, "")
            penalidade = penalidade_estado.get(estado, 0)
            distancia_h = haversine(vizinho, destino)
            h = distancia_h + penalidade
            if vizinho not in visitados:
                pilha.append((vizinho, caminho + [vizinho], custo + distancia))
    return None, float('inf'), len(visitados)

# Busca A*
def busca_a_estrela(mapa, origem, destino):
    fila = [(0, 0, origem, [origem])]
    visitados = set()
    
    while fila:
        f, g, atual, caminho = heapq.heappop(fila)
        if atual == destino:
            return caminho, g, len(visitados)
        if atual in visitados:
            continue
        visitados.add(atual)
        for vizinho, distancia in mapa[atual].items():
            estado = capital_estado.get(vizinho, "")
            penalidade = penalidade_estado.get(estado, 0)
            distancia_h = haversine(vizinho, destino)
            h = distancia_h + penalidade
            novo_g = g + distancia
            novo_f = novo_g + h
            heapq.heappush(fila, (novo_f, novo_g, vizinho, caminho + [vizinho]))
    
    return None, float('inf'), len(visitados)

# Executar todas as buscas
def executar_buscas(origem, destino):
    resultados = []
    caminho, custo, visitados = busca_largura(mapa, origem, destino)
    resultados.append(("Busca em Largura (BFS)", caminho, custo, visitados))

    caminho, custo, visitados = busca_profundidade(mapa, origem, destino)
    resultados.append(("Busca em Profundidade (DFS)", caminho, custo, visitados))

    caminho, custo, visitados = busca_a_estrela(mapa, origem, destino)
    resultados.append(("Busca A*", caminho, custo, visitados))

    return resultados

# if __name__ == "__main__":
#     origem = input("Digite a cidade de origem: ").strip().title()
#     destino = input("Digite a cidade de destino: ").strip().title()

#     if origem not in mapa or destino not in mapa:
#         print("*** ERRO - Cidade de origem e/ou destino não encontrada. ***")
#         exit()

#     resultados = []
#     caminho, custo, visitados = busca_largura(mapa, origem, destino)
#     resultados.append(("BUSCA EM LARGURA (BFS)", caminho, custo, visitados))

#     caminho, custo, visitados = busca_profundidade(mapa, origem, destino)
#     resultados.append(("BUSCA EM LARGURA (DFS)", caminho, custo, visitados))

#     caminho, custo, visitados = busca_a_estrela(mapa, origem, destino)
#     resultados.append(("BUSCA A*", caminho, custo, visitados))

#     print("\n=== RESULTADOS DAS BUSCAS ===")

#     for metodo, caminho, custo, visitados in resultados:
#         print(f"\n {metodo}:")
#         print(f"Caminho percorrido: {' -> '.join(caminho)}")
#         print(f"Distância total percorrida: {custo} km")
#         print(f"Número de cidades visitadas: {visitados}")

#     # Comparativo geral
#     print("\n=== COMPARATIVO GERAL ===")
#     print("{:<25} {:<15} {:<20}".format("Método", "Distância (km)", "Cidades visitadas"))

#     for metodo, caminho, custo, visitados in resultados:
#         print("{:<25} {:<15} {:<20}".format(metodo, custo, visitados))

