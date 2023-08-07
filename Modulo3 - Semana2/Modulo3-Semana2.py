def decorator_imprimir(funcao):
    def interno(capital, taxa, tempo):
        print(f'CAPITAL: {capital} TAXA: {taxa} TEMPO: {tempo}')
        resultado = funcao(capital, taxa, tempo)
        print(f'RESULTADO: {resultado}')
        return resultado
    return interno

@decorator_imprimir
def juros_simples(capital, taxa, tempo):
    return capital * (taxa/100) * tempo