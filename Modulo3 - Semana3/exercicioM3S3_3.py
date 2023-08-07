def ler_dimensoes_objeto(altura_lida, comprimento_lido, largura_lida):
    volume = 0
    lido_sucesso = False

    while not lido_sucesso:
        altura = validar_medida(altura_lida)
        if altura == -1:
            continue

        comprimento = validar_medida(comprimento_lido)
        if comprimento == -1:
            continue

        largura = validar_medida(largura_lida)
        if largura == -1:
            continue

        volume = altura * comprimento * largura

        if volume > 100000.0 or volume <= 0:
            print('Não aceitamos objetos com dimensões grandes e/ou zeradas')
            print('Entre com as dimensões desejadas novamente')
            continue

        lido_sucesso = True

    preco_volume = calcular_preco_volume(volume)
    print(f'Volume do Objeto (em cm³): {volume}')
    return preco_volume


def calcular_preco_volume(volume):
    valor_volume = 0.0

    if volume < 1000:
        valor_volume = 10.0
    elif volume >= 1000 and volume < 10000:
        valor_volume = 20.0
    elif volume >= 10000 and volume < 30000:
        valor_volume = 30.0
    elif volume >= 30000 and volume < 100000:
        valor_volume = 20.0

    return valor_volume


def validar_medida(medida):
    try:
        medida_validada = int(medida)
    except:
        print('Você digitou alguma dimensão do objeto com valor não numérico')
        print('Entre com as dimensões desejadas novamente')
        return -1

    return medida_validada


def ler_peso_objeto():
    lido_sucesso = False
    peso = 0

    while not lido_sucesso:
        peso_lido = input('Digite o peso do objeto (em Kg): ')
        try:
            peso = float(peso_lido)
            if peso > 30:
                print('Não é aceito objetos tão pesados')
                print('Por favor entre com o peso novamente')
                continue
            lido_sucesso = True
        except:
            print('Você digitou o peso do objeto com um valor não numérico')
            print('Por favor entre com o peso novamente')

    multiplicador_peso = calcular_multiplicador_peso(peso)
    return multiplicador_peso


def calcular_multiplicador_peso(peso):
    multiplicador = 0

    if peso < 0.1:
        multiplicador = 1.0
    elif peso >= 0.1 and peso < 1:
        multiplicador = 1.5
    elif peso >= 1 and peso < 10:
        multiplicador = 2.0
    elif peso >= 10 and peso <= 30:
        multiplicador = 3.0

    return multiplicador


def ler_rota(rota):
    #lido_sucesso = False

    #while not lido_sucesso:
    #    print('Selecione a rota: ')
    #    print('BR - De Brasília para Rio de Janeiro')
    #    print('BS - De Brasília para São Paulo')
    #    print('RB - De Rio de Janeiro para Brasília')
    #    print('RS - De Rio de Janeiro para São Paulo')
    #   print('SR - De São Paulo para Rio de Janeiro')
    #    print('SB - De São Paulo para Brasília')

    #    rota = rota.lower()
    #lido_sucesso = True
    
    multiplicador_rota = calcular_multiplicador_rota(rota)
    return multiplicador_rota


def calcular_multiplicador_rota(rota):
    multiplicador = 0.0
    if rota in ['rs', 'sr']:
        multiplicador = 1.0
    elif rota in ['bs', 'SB']:
        multiplicador = 1.2
    elif rota in ['br', 'rb']:
        multiplicador = 1.5

    return multiplicador


def calcular_frete(volume, multiplicador_peso, multiplicador_rota):
    total = volume * multiplicador_peso * multiplicador_rota
    return total
