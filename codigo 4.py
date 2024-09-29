def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

# Exemplo de uso:
string = "exemplo"
string_invertida = inverter_string(string)
print(f"String original: {string}")
print(f"String invertida: {string_invertida}")
