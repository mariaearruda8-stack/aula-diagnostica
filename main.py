nome= input()

num = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

import random

opcoes = ["Cara", "Coroa"]
resultado = random.choice(opcoes)
print(f"O resultado do lançamento foi: {resultado}")

print("Olá, mundo!")

print(15 + 35)

print("Python! " * 5)

print(type("Texto"))

print(len("Programação"))
