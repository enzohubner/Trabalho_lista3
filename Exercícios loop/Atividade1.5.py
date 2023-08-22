lista = []
quantidade = int(input("Quantos numeros voce deseja? "))

for i in range(1, quantidade +1):
    numero = int(input("Digite um dos numeros: "))
    lista.append(numero) 
print(max(lista))