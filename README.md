# Real brasileiro

> Status do projeto: Em desenvolvimento

este projeto tem como objetivo me ajudar na formatação, sanitização e apresentação dos valores com os quais eu diariamente trabalho.

## Entradas
```
from real_br import Real

print(ReaL(10.10),
    Real(10),
    Real('R$ 100,55'))

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
real = Real(valor)
print(real.centavos)

```
> A classe retorna float, str e inteiro sendo o valor em centavos

