import json

# Exemplo de JSON de faturamento diário
faturamento_diario = {
    "dias": [
        {"dia": 1, "valor": 22174.1664},
        {"dia": 2, "valor": 24537.6698},
        {"dia": 3, "valor": 26139.6134},
        {"dia": 4, "valor": 0.0},  # Fim de semana/feriado
        {"dia": 5, "valor": 0.0},  # Fim de semana/feriado
        {"dia": 6, "valor": 26742.6612},
        # E assim por diante...
    ]
}

def calcular_estatisticas(faturamento):
    valores = [dia['valor'] for dia in faturamento['dias'] if dia['valor'] > 0]

    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)

    dias_acima_media = sum(1 for valor in valores if valor > media)

    return menor, maior, dias_acima_media

menor_valor, maior_valor, dias_acima_media = calcular_estatisticas(faturamento_diario)
print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
