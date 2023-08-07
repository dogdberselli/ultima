import pytest
from exercicioM3S3_2 import exercicio2

#testar valor X-Egg
def test_exercicio1():
    valor = exercicio2(102)
    assert valor == (12)

#testar valor refrigerante lata
def test_exercicio12():
    valor = exercicio2(200)
    assert valor == (5)

#testar valor chá gelado
def test_exercicio13():
    valor = exercicio2(201)
    assert valor == (4)