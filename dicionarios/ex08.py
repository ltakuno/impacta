def contar_frutas(lista_frutas):
    contadores_frutas = {}
    for fruta in lista_frutas:
        if fruta not in contadores_frutas:
            contadores_frutas[fruta] = 1
        else:
            contadores_frutas[fruta] += 1
    return contadores_frutas


def contar_frutas2(lista_frutas):
    contadores_frutas = {}
    for fruta in lista_frutas:
        contadores_frutas[fruta] = lista_frutas.count(fruta)
        
    return contadores_frutas

frutas = ['banana', 'pera', 'uva', 'pera', 'pera']
contador = contar_frutas2(frutas)
print(contador)
