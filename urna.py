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

