
import re

class Real:

    def __init__(self, valor: float or int or str, centavos=False) -> str or int or float:
        self._sinal = ''
        _valor: str = self._achar_sinal(valor)

        if not centavos:
            self.centavos: int = self._verificar_valor(_valor)
            self.reais: str = self._mascara_reais()

        else:
            _valor = _valor
            verificacao = self._verifica_centavos(_valor)
            if verificacao:
                self.centavos = int(_valor)
                self.reais: str = self._mascara_reais()
            else:
                raise ValueError(f'Entrada de valor invalida! valor = {_valor}')


    def _mascara_reais(self):
        centavos = str(self.centavos).replace(self._sinal, '')
        if len(centavos) > 2:
            valor_sem_virgula = centavos[:-2]
            formato_brasileiro = re.split(r'([0-9]{3})', f'{valor_sem_virgula[::-1]}'.strip())

            x = 0
            for item in formato_brasileiro:
                if item == '':
                    formato_brasileiro.pop(x)
                x += 1
            formato_brasileiro = ('.'.join(formato_brasileiro))

            return f'R$ {self._sinal}{formato_brasileiro[::-1]},{centavos[-2:]}'

        elif len(centavos) == 1:
            return f'R$ {self._sinal}0,0{centavos}'

        else:
            return f'R$ {self._sinal}0,{centavos}'

    def _verifica_centavos(self, valor: str) -> bool:
        m = re.compile(r"[0-9]+")
        result = m.match(valor)
        return result

    def _verificar_valor(self, valor: str) -> str:

        m = re.compile(r"\d+[,]?[.]?(\d+)?")
        result = m.match(valor)
        if result:
            return self._sanitiza_valor(valor)

        elif 'R$' in valor:
            return self._sanitiza_valor(valor.replace('R$', ''))

        else:
            raise ValueError(f'Entrada de valor invalida! valor = {valor}')

    def _sanitiza_valor(self, valor: str) -> int:
        valor = valor.strip()
        valor_em_centavos = self._fatiar_valor(valor)

        if type(valor_em_centavos) is list:
            if len(valor_em_centavos[1]) == 1:

                return int(f'{self._sinal}{valor_em_centavos[0]}{valor_em_centavos[1]}0')

            else:

                return int(f'{self._sinal}{valor_em_centavos[0]}{(valor_em_centavos[1])[:2]}')
        else:
            return int(f'{self._sinal}{valor_em_centavos}')

    # Separa o valor em itens de uma lista pra depois adicionar "." de 3 em 3 numeros usando re

    def _fatiar_valor(self, valor: str) -> list:

        if ',' in valor:
            valor = valor.replace('.', '')
            lista_fatiada = valor.split(",")
            lista_fatiada[1] = (lista_fatiada[1])[:3]
            return lista_fatiada


        elif '.' in valor:
            lista_fatiada = valor.split(".")
            lista_fatiada[1] = (lista_fatiada[1])[:3]
            return lista_fatiada

        else:
            return int(f'{valor}00')

    def _achar_sinal(self, valor: str) -> str:
        valor = str(valor).replace(' ', '')
        if '-' in valor:
            self._sinal = '-'
            return valor.replace('-', '')

        elif '+' in valor:
            return valor.replace('+', '')

        else:
            return valor

    # <>

    def __str__(self):
        return self.reais

    def __float__(self):
        return (self.centavos / 100)

    def __int__(self):
        return self.centavos

    # Operações

    def __add__(self, other: object) -> object:
        return Real(self.centavos + other.centavos, centavos=True)

    def __sub__(self, other: object) -> object:
        return Real(self.centavos - other.centavos, centavos=True)

    def __truediv__(self, other: int or float) -> object:
        return Real((self.centavos/100) / other)

    def __mul__(self, other: int or float) -> object:
        return Real((self.centavos) * other, centavos=True)

    def __eq__(self, other: object) -> bool:
        return self.centavos == other.centavos

    def __lt__(self, other: object) -> bool:
        return self.centavos < other.centavos

    def __le__(self, other: object)-> bool:
        return self.centavos <= other.centavos

    def __ne__(self, other: object) -> bool:
        return self.centavos != other.centavos

    def __ge__(self, other: object) -> bool:
        return self.centavos >= other.centavos

    def __gt__(self, other: object)-> bool:
        return self.centavos > other.centavos