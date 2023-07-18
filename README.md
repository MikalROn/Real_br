# Real brasileiro

> Status do projeto: Em desenvolvimento

este projeto tem como objetivo me ajudar na formatação, sanitização e apresentação dos valores com os quais eu diariamente trabalho.
## Download

```shell
$pip install real-brasileiro
```

## Entradas
```python
from real_br import Real

print(Real(10.10),
    Real(10),
    Real('R$ 100,55'))

```
> Nos testes você consegue conferir melhor em quais formatos a classe aceita os valores.


## Criando objeto

```python
from real_br import Real

valor = 10
real = Real(valor)
print(real)

```

> você também pode obter o equivalente em centavos usando

```python
from real_br import Real

valor = 10
real = Real(valor)
print(real.centavos)

```
> A classe retorna float, str e int (int é retornado em centavos)

```python
from real_br import Real

valor = 10
real = Real(valor)
print(float(real),  int(real), str(real))

```
# A classe possui 100% de cobertura de testes
````shell
pytest -cov
````
