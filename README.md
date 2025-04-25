# 🗺️ Trabalho de Inteligência Artificial — Métodos de Busca

Este projeto implementa algoritmos de busca em grafos para o cálculo de rotas entre capitais brasileiras. O sistema considera distâncias rodoviárias, heurísticas de distância geográfica (baseada na fórmula de Haversine) e penalidades associadas à qualidade da malha rodoviária de cada estado.

## 📖 Descrição

O objetivo do projeto é aplicar e comparar diferentes estratégias de busca — Busca em Largura (BFS), Busca em Profundidade (DFS) e Busca A* — sobre um grafo que representa as capitais do Brasil e suas distâncias, simulando a seleção de rotas mais eficientes entre duas cidades.

Uma interface web foi desenvolvida utilizando o framework Flask, permitindo que o usuário selecione a cidade de origem e destino e visualize os caminhos percorridos, distâncias totais e comparativo entre os métodos.

## 📊 Métodos de Busca Implementados

- **Busca em Largura (BFS)**  
  Explora os caminhos disponíveis expandindo primeiro os nós mais próximos da origem.

- **Busca em Profundidade (DFS)**  
  Prioriza seguir um caminho até o final antes de retornar para explorar outros.

- **Busca A\***  
  Combina o custo acumulado (distância percorrida) e uma heurística baseada na distância geográfica em linha reta (fórmula de Haversine) somada a uma penalidade da malha rodoviária estadual, priorizando os caminhos mais promissores.

## 🛠️ Tecnologias Utilizadas

- Python 3.11
- Flask
- HTML + CSS (responsivo)
- Função Haversine (cálculo de distância geográfica)
- Vercel (deploy web)
