import pytest
from real_br import *

class Test:
    
    def test_se_real_br_aceita_numeros_inteiros(self):
        entrada = 100
        esperado = 'R$ 100,00'
        
        entrada = Real(entrada)
        entrada = str(entrada)
        
        assert entrada == esperado
        
    def test_se_real_br_aceita_numeros_float(self):
        entrada = 100.00
        esperado = 'R$ 100,00'
        
        entrada = Real(entrada)
        entrada = str(entrada)
        
        assert entrada == esperado
        
    def test_se_real_br_aceita_numeros_em_str_sem_virgula_ou_ponto(self):
        entrada = '100'
        esperado = 'R$ 100,00'
        
        entrada = Real(entrada)
        entrada = str(entrada)
        
        assert entrada == esperado
        
    def test_se_real_br_aceita_numeros_em_str_com_virgula_e_uma_casa_decimal(self):
        entrada = '100,0'
        esperado = 'R$ 100,00'
        
        entrada = Real(entrada)
        entrada = str(entrada)
        
        assert entrada == esperado
        
    def test_se_real_br_aceita_numeros_em_str_com_virgula_e_duas_casas_decimais(self):
        entrada = '100,00'
        esperado = 'R$ 100,00'
        
        entrada = Real(entrada)
        entrada = str(entrada)
        
        assert entrada == esperado
        
    def test_se_real_br_aceita_numeros_em_str_com_ponto_e_duas_casas_decimais(self):
        entrada = '100.00'
        esperado = 'R$ 100,00'
        
        entrada = Real(entrada)
        entrada = str(entrada)
        
        assert entrada == esperado
        
    def test_se_real_br_aceita_numeros_em_str_com_ponto_e_uma_casa_decimal(self):
        entrada = '100.0'
        esperado = 'R$ 100,00'
        
        entrada = Real(entrada)
        entrada = str(entrada)
        
        assert entrada == esperado
        
    def test_se_real_br_aceita_numeros_em_str_com_ponto_e_sem_casa_decimal(self):
        entrada = '100'
        esperado = 'R$ 100,00'
        
        entrada = Real(entrada)
        entrada = str(entrada)
        
        assert entrada == esperado