while True:
    try:
        candidato1 = str(input("Canditato1: "))
        break
    except ValueError:
        print('Erro ao cadastar')
        break
while True:
    try:
        candidato2 = str(input("Canditato2: "))
        break
    except ValueError:
        print('Erro ao cadastar')
        break
    print('')