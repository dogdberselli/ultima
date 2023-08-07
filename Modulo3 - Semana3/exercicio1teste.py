import pytest
from exercicioM3S3_1 import exercicio1

#testar desconto de 0,95
def test_exercicio1():
    valor = exercicio1(1,10)
    assert valor == (10, 9.5)

#testar desconto de 0,90
def test_exercicio12():
    valor = exercicio1(22, 135)
    assert valor == (2970, 2673)

#testar desconto de 0,85
def test_exercicio13():
    valor = exercicio1(1520, 1020)
    assert valor == (1550400, 1317840)