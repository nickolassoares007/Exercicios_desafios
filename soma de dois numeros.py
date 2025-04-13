def addition(a, b): #Define a função de soma
    return a + b #Aqui estou retornando o resultado da soma

a = int(input("Digite o primeiro número: ")) #Aqui estou pedindo o primeiro número
b = int(input("Digite o segundo número: ")) #Aqui estou pedindo o segundo número

result = addition(a, b) #Aqui estou chamando a função de soma e passando os números como parâmetros
print(f"A soma de {a} e {b} é: {result}") #