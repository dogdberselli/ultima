pecas = [{'codigo': 48151, 'nome': 'pneu', 'fabricante': 'Michellin', 'valor': 154.8502}]


def cadastrar_peca(codigo, nome, fabricante, valor):
    #codigo = gerar_codigo()
    peca = []
    #print(f'\nCódigo da peça: {codigo:03d}')
    #nome = input('Por favor entre com o nome da peça: ')
    #fabricante = input('Por favor entre com o fabricante da peça: ')
    #valor = float(input('Por favor entre com o valor da peça (R$): '))
    peca = {
        'codigo': codigo,
        'nome': nome,
        'fabricante': fabricante,
        'valor': valor
    }

    pecas.append(peca)
    print('Peça Adicionada!\n')
    return peca


def imprimir_peca(peca):
    return (f'Código: {peca["codigo"]:03d} Fabricante: {peca["fabricante"]} Valor: R${peca["valor"]:.2f}')    


def consultar_pecas(opcao_consulta):
    finaliza_consulta = False
    while not finaliza_consulta:
        print('Você selecionou a opção para consultar peças')
        print('Escolha a opção desejada:')
        print('1 - Consultar todas as pecas')
        print('2 - Consultar peças por código')
        print('3 - Consultar peças por fabricante')
        print('4 - Retornar')
        print()
        if opcao_consulta == 1:
            for peca in pecas:
                imprimir_peca(peca)
            return('-' * 15)
        elif opcao_consulta == 2:
            codigo = int(input('Digite o código da peça: '))
            for peca in pecas:
                if peca['codigo'] == codigo:
                    imprimir_peca(peca)
                    print('-' * 15)
                    break
        elif opcao_consulta == 3:
            fabricante = input('Digite o fabricante da peça: ')
            for peca in pecas:
                if peca['fabricante'] == fabricante:
                    imprimir_peca(peca)
                    print('-' * 15)
        elif opcao_consulta == 4:
            finaliza_consulta = True
            print()
        else:
            print('Opção inválida. Tente novamente')


def remover_peca(codigo):
    print('Você selecionou a opção para remover uma peça')
    #codigo = int(input('Código da peça a ser removida: '))
    peca_remover = {}
    for peca in pecas:
        if peca['codigo'] == codigo:
            peca_remover = peca
            break

    pecas.remove(peca_remover)
    return 'Peça removida com sucesso'


def escolheropcao(opcao):
    #opcao = 0
    while opcao != 4:
        print('Escolha a opção desejada')
        print('1 - Cadastrar Peças')
        print('2 - Consultar Peças')
        print('3 - Remover Peças')
        print('4 - Sair')
    #    opcao = int(input('Opção desejada: '))

        if opcao == 1:
        #    cadastrar_peca()
            return 'cadastrar_peca'
        elif opcao == 2:
        #    consultar_pecas()
            return 'consultar_pecas'
        elif opcao == 3:
        #    remover_peca()
            return 'remover pecas'
        elif opcao >= 4 or opcao < 1:
            return 'Opção Inválida'

    print('Obrigado por usar nossos aplicativos')