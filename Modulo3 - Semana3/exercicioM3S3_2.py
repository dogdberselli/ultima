def exercicio2(codigo):
    total = 0.0

    while True:
        if codigo == 100:
            print('Você pediu um Cachorro Quente no valor de 9,00')
            total += 9.00
        elif codigo == 101:
            print('Você pediu um Cachorro Quente Duplo no valor de 11,00')
            total += 11.00
        elif codigo == 102:
            print('Você pediu um X-Egg no valor de 12,00')
            total += 12.00
        elif codigo == 103:
            print('Você pediu um X-Salada no valor de 12,00')
            total += 12.00
        elif codigo == 104:
            print('Você pediu um X-Bacon no valor de 14,00')
            total += 14.00
        elif codigo == 105:
            print('Você pediu um X-Tudo no valor de 17,00')
            total += 17.00
        elif codigo == 200:
            print('Você pediu um Refrigerante Lata no valor de 5,00')
            total += 5.00
        elif codigo == 201:
            print('Você pediu um Chá Gelado no valor de 4,00')
            total += 4.00
        else:
            print('Opção inválida')
        return total
    
