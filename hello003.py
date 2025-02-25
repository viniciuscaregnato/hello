"""
Programa Hello
Imprima a frase: "Hello World!"
Autor: Vinicius
Data: 25.02.2025
Versão: 0.0.3
Novidades da versão

25/02/2025
Nesta versão: 
1. Nesta versão o usuário poderá entrar com seu nome, para poder ser cumprimentado pelo programa.
"""
# Alocação de memoria

nome_usuario = ""
frase = "Hello, "

# Entrada de dados

nome_usuario = input("\nqual o seu nome: ")

# Processamento de dados

frase = frase + nome_usuario

#Saída de dados

print(frase)