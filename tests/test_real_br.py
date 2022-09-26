import pytest
from pytest import raises
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
    def test_se_real_br_aceita_numeros_floats_enormes(self):
        entrada = 100.12343242323123
        esperado = 'R$ 100,12'

        entrada = Real(entrada)
        entrada = str(entrada)

        assert entrada == esperado

    def test_se_real_br_aceita_numeros_str_enormes(self):
        entrada = '100,12343242323123'
        esperado = 'R$ 100,12'

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

    def test_se_real_br_centavos_em_int(self):
        entrada = 100  # Valor em centavos
        esperado = 'R$ 1,00'

        entrada = Real(entrada, centavos=True)
        entrada = str(entrada)

        assert entrada == esperado

    def test_se_real_br_centavos_em_str(self):
        entrada = '100'  # Valor em centavos
        esperado = 'R$ 1,00'

        entrada = Real(entrada, centavos=True)
        entrada = str(entrada)

        assert entrada == esperado

    def test_se_real_br_aceita_sinais(self):
        entradas = ['+100', '-100']
        esperado = ['R$ 100,00', 'R$ -100,00']

        entrada = [str(Real(x)) for x in entradas]

        assert entrada[0] == esperado[0] and entrada[1] == esperado[1]

    def test_de_entrada_como_letra(self):
        with pytest.raises(ValueError):
            entrada = 'A'
            saida = Real(entrada)
            assert saida



