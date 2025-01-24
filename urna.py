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

MAX_PESSOAS = 100

while True:
    try:
        urna1 = input("Quantas pessoas podem votar na urna 1: ")
        if not urna1.isnumeric():
            raise ValueError("Erro: Apenas números são permitidos.")
        urna1 = int(urna1)
        if urna1 > MAX_PESSOAS:
            raise ValueError(f"Erro: O número máximo de pessoas é {MAX_PESSOAS}.")
        break
    except ValueError as e:
        print(e)

while True:
    try:
        urna2 = input("Quantas pessoas vão votar na urna 2: ")
        if not urna2.isnumeric():
            raise ValueError("Erro: Apenas números são permitidos.")
        urna2 = int(urna2)
        if urna2 > MAX_PESSOAS:
            raise ValueError(f"Erro: O número máximo de pessoas é {MAX_PESSOAS}.")
        break
    except ValueError as e:
        print(e)

print('')

