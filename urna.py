while True:
    try:
        candidato1 = input("Candidato 1: ")
        if not candidato1.isalpha():
            raise ValueError("Erro: Apenas nomes são permitidos.")
        break
    except ValueError as e:
        print(e)
while True:
    try:
        candidato2 = input("Candidato 2: ")
        if not candidato2.isalpha():
            raise ValueError("Erro: Apenas nomes são permitidos.")
        break
    except ValueError as e:
        print(e)

print('')

while True:
    try:
        candidato1 = input("Partido do candidato 1: ")
        if not candidato1.isalpha():
            raise ValueError("Erro: Apenas nomes são permitidos.")
        break
    except ValueError as e:
        print(e)
while True:
    try:
        candidato2 = input("Partido do candidato 2: ")
        if not candidato2.isalpha():
            raise ValueError("Erro: Apenas nomes são permitidos.")
        break
    except ValueError as e:
        print(e)
print(' ')

while True:
    try:
        candidato1 = input("Número do candidato 1: ")
        if not candidato1.isnumeric():
            raise ValueError("Erro: Apenas números são permitidos.")
        break
    except ValueError as e:
        print(e)

while True:
    try:
        candidato2 = input("Número do candidato 2: ")
        if not candidato2.isnumeric():
            raise ValueError("Erro: Apenas números são permitidos.")
        break
    except ValueError as e:
        print(e)
print(' ')

import matplotlib.pyplot as plt

MAX_PESSOAS = 100

def obter_numero_pessoas(urna):
    while True:
        try:
            numero = input(f"Quantas pessoas podem votar na {urna}: ")
            if not numero.isnumeric():
                raise ValueError("Erro: Apenas números são permitidos.")
            numero = int(numero)
            if numero > MAX_PESSOAS:
                raise ValueError(f"Erro: O número máximo de pessoas é {MAX_PESSOAS}.")
            return numero
        except ValueError as e:
            print(e)
print(' ')

urna1_pessoas = obter_numero_pessoas("urna 1")
urna2_pessoas = obter_numero_pessoas("urna 2")


votos_candidato1 = 0
votos_candidato2 = 0
votos_nulos_brancos = 0

def votar(numero_pessoas):
    global votos_candidato1, votos_candidato2, votos_nulos_brancos
    for i in range(numero_pessoas):
        while True:
            try:
                voto = input(f"Voto {i+1}/{numero_pessoas} (1 para Candidato 1, 2 para Candidato 2, 0 para Nulo/Branco): ")
                if voto not in ["0", "1", "2"]:
                    raise ValueError("Erro: Apenas 0, 1 ou 2 são permitidos.")
                voto = int(voto)
                if voto == 1:
                    votos_candidato1 += 1
                elif voto == 2:
                    votos_candidato2 += 1
                else:
                    votos_nulos_brancos += 1
                break
            except ValueError as e:
                print(e)

print("Votação para urna 1:")
votar(urna1_pessoas)
print("Votação para urna 2:")
votar(urna2_pessoas)

print(f"\nResultados da votação:")
print(f"Candidato 1: {votos_candidato1} votos")
print(f"Candidato 2: {votos_candidato2} votos")
print(f"Votos Nulos/Brancos: {votos_nulos_brancos} votos")

labels = ['Candidato 1', 'Candidato 2', 'Nulos/Brancos']
votos = [votos_candidato1, votos_candidato2, votos_nulos_brancos]

plt.bar(labels, votos, color=['blue', 'green', 'red'])
plt.xlabel('Opções')
plt.ylabel('Número de Votos')
plt.title('Resultados da Votação')
plt.show()


