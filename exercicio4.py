letras = []
for letra in range(10):
    letra = input('Digite uma letra do alfabeto: ')
    letras.append(letra)

consoantes = [letra for letra in letras if letra != 'a' and letra !='e' and letra !='i' and letra !='o'and letra !='u']

print(f'Foram digitadas {len(consoantes)} consoantes!')