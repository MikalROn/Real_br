# Real brasileiro

> Status do projeto: Em desenvolvimento

este projeto tem como objetivo me ajudar na formatação, sanitização e apresentação dos valores com os quais eu diariamente trabalho.

## Entradas
```
from real_br import Real

Rea(float)
Real(int)
Real(str)

```
> Nos testes você consegue conferir melhor em quais formatos a classe aceita os valores.


## Criando objeto

```
from real_br import Real

valor = 10
real = Real(valor)
print(real)

```
> você também pode obter o equivalente em centavos usando
```
from real_br import Real

valor = 10
real = Real(valo)
print(real.centavos)

```
