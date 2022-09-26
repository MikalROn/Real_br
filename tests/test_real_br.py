import pytest
from real_br import *

class Test:
    def test_se_calsse_aceita_numeros_inteiros(self):
        entrada = 100
        esperado = 'R$ 100,00'
        
        entrada = Real(entrada)
        entrada = str(entrada)
        
        assert entrada == esperado