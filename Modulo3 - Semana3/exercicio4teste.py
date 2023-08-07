import pytest
from exercicioM3S3_4 import cadastrar_peca, imprimir_peca, remover_peca, escolheropcao


def test_cadpeca():
    valor = cadastrar_peca('44', 'naxm', 'valo', 4.40)
    assert valor == {'codigo': '44', 'fabricante': 'valo', 'nome': 'naxm', 'valor': 4.4}

def test_imprimirpeca():
    pecas = {'codigo': 48151, 'nome': 'pneu', 'fabricante': 'Michellin', 'valor': 154.8502}
    valor = imprimir_peca(pecas)
    assert valor == 'Código: 48151 Fabricante: Michellin Valor: R$154.85'

def test_removerpeca():
    valor = remover_peca(48151)
    assert valor == 'Peça removida com sucesso'


def test_escolheropcao():
    valor = escolheropcao(2)
    assert valor == 'consultar_pecas'
    valor2 = escolheropcao(3)
    assert valor2 == 'remover pecas'
    valor3 = escolheropcao(5)
    assert valor3 == "Opção Inválida"

