import os

os.system("cls || clear")

login = input("Login: ")
senha = input("Senha: ")

if login == "Jeff@gmail.com" and senha == "123":
    print("Bem-vindo")
else:
    print("Login ou senha inválidos.")
