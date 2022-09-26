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

    def test_se_real_br_aceita_infixo_R_cifrao(self):
        entrada = 'R$ 0,10'  # Valor em centavos
        esperado = 'R$ 0,10'

        entrada = Real(entrada)
        entrada = str(entrada)
        assert entrada == esperado

    def test_se_real_br_centavos_em_str(self):
        entrada = '100'  # Valor em centavos
        esperado = 'R$ 1,00'

        entrada = Real(entrada, centavos=True)
        entrada = str(entrada)

        assert entrada == esperado

    def test_se_real_br_centavos_menosres_que_1_real(self):
        entrada = '10'  # Valor em centavos
        esperado = 'R$ 0,10'

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

    def test_de_entrada_como_centavos_errada(self):

        with pytest.raises(ValueError):
            entrada = 'A'
            saida = Real(entrada, centavos=True)
            assert saida

    def test_de_entrada_errada_de_centavos(self):
        with pytest.raises(ValueError):
            entrada = 100.0
            saida = Real(entrada, centavos=True)
            assert saida

    def test_de_adicao(self):
        entrada = 100

        esperado = 'R$ 200,00'

        entrada = Real(entrada)

        saida = entrada + entrada
        assert str(saida) == esperado

    def test_de_subtracao(self):
        entrada = 100

        esperado = 'R$ 0,0'

        entrada = Real(entrada)

        saida = entrada - entrada
        assert str(saida) == esperado

    def test_de_divisao(self):
        entrada = 100

        esperado = 'R$ 50,00'

        entrada = Real(entrada)

        saida = entrada / 2
        assert str(saida) == esperado

    def test_de_multiplicacao(self):
        entrada = 100

        esperado = 'R$ 200,00'

        entrada = Real(entrada)

        saida = entrada * 2
        assert str(saida) == esperado

    def test_de_operacoes_logicas(self):

        entrada1 = Real(20)
        entrada2 = Real(20)
        entrada3 = Real(1)


        esperado = [ True, False, True, False, True, False]

        resultado = [
         entrada1 == entrada2
        , entrada1 != entrada2
        , entrada1 > entrada3
        ,  entrada1 < entrada3
        , entrada1 >= entrada3
        , entrada1 <= entrada3]

        assert esperado == resultado

    def test_de_entrada_0(self):

        entrada = Real(0)

        assert str(entrada) == 'R$ 0,0'

    def test_de_float(self):

        entrada = Real(100.10)

        assert float(entrada) == 100.10
    def test_de_int(self):

        entrada = Real(100.10)

        assert int(entrada) == 10010


