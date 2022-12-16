notas = [10, 9, 5, 8]
tamanho = len(notas)
soma = sum(notas)
media = soma/tamanho
print(f'As suas notas foram: ' + ' '.join([str(nota) for nota in notas]) + f' e sua média foi de {media}')