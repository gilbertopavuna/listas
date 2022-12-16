notas = []
while True:
    entrada = input('Digite um número: ')
    if entrada == '-1':
        break
    notas.append(float(entrada))
    
tamanho = len(notas)
print(f'Foram lidas {tamanho} notas') #valores que foram lidos
print('Os valores digitados foram: ' + ' '.join([str(nota) for nota in notas])) #valores que foram informados uma ao lado do outro
notas.reverse()
for nota in notas:
    print(nota) #Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro

soma = sum(notas)
print(f'A soma das notas digitadas foi {soma}') #Calcule e mostre a soma dos valores

media = soma / tamanho
print(f'A média das notas digitadas foi {media}') #Calcule e mostre a média dos valores

print('As notas acima da média foi: ' + ' '.join([str(nota) for nota in notas if nota > media]))
#Calcule e mostre a quantidade de valores acima da média calculada

print('As notas abaixo de 7 foi: ' + ' '.join([str(nota) for nota in notas if nota < 7]))
#Calcule e mostre a quantidade de valores abaixo de sete

print('Programa encerrado!')