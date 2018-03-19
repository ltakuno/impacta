def extrair_impares(vetor):
    return [n for n in vetor if n % 2 == 1]


assert extrair_impares([1,2,3,4,5,6,7]) == [1,3,5,7]
assert extrair_impares([3,4,6,7]) == [3,7]
assert extrair_impares([3,4,6,8]) == [3]
assert extrair_impares([4,6,8]) == []
