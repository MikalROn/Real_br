
import re

class Real:

    def __init__(self, valor: float or int or str,
                 centavos=False):  # Atenção com floats e strings com mais de 2 casa decimais serão arredondados
        self._sinal = None
        _valor = self._achar_sinal(valor)

        if not centavos:
            if type(_valor) is float:

                _valor = str(round(_valor, 2))
                self.centavos: int = self._verificar_valor(_valor)

            elif type(_valor) is str:

                self.centavos: int = self._verificar_valor(_valor)

            else:

                self.centavos: int = self._verificar_valor(_valor)

            self.reais: str = self._mascara_reais()
        else:
            _valor = str(_valor)
            verificacao = self._verifica_centavos(_valor)
            if verificacao:
                self.centavos = int(_valor)
                self.reais: str = self._mascara_reais()
            else:
                raise ValueError(f'Entrada de valor invalida! valor = {_valor}')

    def _mascara_reais(self):
        if len(str(self.centavos)) > 2:
            valor_sem_virgula = str(self.centavos)[:-2]
            formato_brasileiro = re.split(r'([0-9]{3})', f'{valor_sem_virgula[::-1]}'.strip())

            x = 0
            for item in formato_brasileiro:
                if item == '':
                    formato_brasileiro.pop(x)
                x += 1
            formato_brasileiro = ('.'.join(formato_brasileiro))

            return f'R$ {self._sinal}{formato_brasileiro[::-1]},{str(self.centavos)[-2:]}'
        else:
            return f'R$ {self._sinal}0,{str(self.centavos)}'

    def _verifica_centavos(self, valor: str):
        m = re.compile(r"[0-9]+")
        result = m.match(valor)
        return result

    def _verificar_valor(self, valor: str):

        m = re.compile(r"\d+[,]?[.]?(\d+)?")
        result = m.match(str(valor))
        if '-' in str(valor):
            self._sinal = '-'
            valor = str(valor).replace('_', '')
            if result:
                return self._sanitiza_valor(valor)

            if 'R$' in str(valor):
                return self._sanitiza_valor(valor.replace('R$', ''))

            else:

                raise ValueError(f'Entrada de valor invalida! valor = {valor}')
        else:
            if result:
                return self._sanitiza_valor(valor)

            if 'R$' in str(valor):
                return self._sanitiza_valor(valor.replace('R$', ''))

            else:

                raise ValueError(f'Entrada de valor invalida! valor = {valor}')

    def _sanitiza_valor(self, valor: str):

        valor_em_centavos = self._fatiar_valor(valor)

        if type(valor_em_centavos) is list:
            if len(valor_em_centavos[1]) == 1:

                return int(f'{valor_em_centavos[0]}{valor_em_centavos[1]}0')

            else:

                return int(f'{valor_em_centavos[0]}{valor_em_centavos[1]}')
        else:
            return valor_em_centavos

    # Separa o valor em itens de uma lista pra depois adicionar "." de 3 em 3 numeros usando re

    def _fatiar_valor(self, valor):

        if ',' in str(valor):
            valor = valor.replace('.', '')
            lista_fatiada = str(valor).split(",")
            lista_fatiada[1] = (lista_fatiada[1])[:3]
            return lista_fatiada


        elif '.' in str(valor):
            lista_fatiada = str(valor).split(".")
            lista_fatiada[1] = (lista_fatiada[1])[:3]
            return lista_fatiada

        else:
            return int(f'{valor}00')

    def _achar_sinal(self, valor: str):
        valor = str(valor)
        if '-' in valor:
            self._sinal = '-'
            return valor.replace('-', '')

        elif '+' in valor:
            self._sinal = ''
            return valor.replace('+', '')

        else:
            self._sinal = ''
            return valor

    def __str__(self):
        return self.reais

    # Operações 

    def __add__(self, other):
        return Real(self.centavos + other.centavos, centavos=True)

    def __sub__(self, other):
        return Real(self.centavos - other.centavos, centavos=True)

    def __truediv__(self, other):
        return Real(self.centavos / other.centavos, centavos=True)

    def __mul__(self, other):
        return Real(self.centavos * other.centavos, centavos=True)

    def __eq__(self, other):
        return self.centavos == other.centavos

    def __lt__(self, other):
        return self.centavos < other.centavos

    def __le__(self, other):
        return self.centavos <= other.centavos

    def __ne__(self, other):
        return self.centavos != other.centavos

    def __ge__(self, other):
        return self.centavos >= other.centavos

    def __gt__(self, other):
        return self.centavos > other.centavos