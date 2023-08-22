numero = int(input("Digite o tamanho da lista: "))
par = 0
impar = 0
for i in range(1, numero + 1):
    if i % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1        
print(f'tem {impar} numeros impares e {par} numeros pares')        