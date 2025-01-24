while True:
    try:
        candidato1 = str(input("Canditato1: "))
        continue
    except ValueError:
        print('Erro ao cadastar')
        break
while True:
    try:
        candidato2 = str(input("Canditato2: "))
    except ValueError:
        print('Erro ao cadastar')
        break
    print('')