import pytest
from exercicioM3S3_3 import ler_dimensoes_objeto, calcular_preco_volume, validar_medida, ler_peso_objeto, calcular_multiplicador_peso, ler_rota, calcular_multiplicador_rota, calcular_frete

def teste_calcularprecodevolume():
    valor = calcular_preco_volume(1220)
    assert valor == (20)

def teste_validar_medida():
    valor = validar_medida(120)
    assert valor == (120)

def teste_multpeso():
    valor = calcular_multiplicador_peso(20)
    assert valor == (3)

def teste_multrota():
    valor = calcular_multiplicador_rota('br')
    assert valor == (1.5)
    valor1 = calcular_multiplicador_rota('rs')
    assert valor1 == (1)

def teste_lerrota():
    valor = ler_rota('br')
    assert valor == 1.5

def teste_calculofrete():
    valor = calcular_frete(20, 10, 5)
    assert valor == 1000