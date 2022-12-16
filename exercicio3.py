notas = []
for nota in range(4):
    nota = float(input('Entre com suas notas: '))
    notas.append(nota)

tamanho = len(notas)
soma = sum(notas)
media = soma/tamanho
print(f'As suas notas foram: ' + ' '.join([str(nota) for nota in notas]) + f' e sua média foi de {media}')