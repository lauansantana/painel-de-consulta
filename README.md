<p align="center">
<img src="https://user-images.githubusercontent.com/50887877/215918735-72fdc720-778e-4cad-8d33-a4d4fdd45ace.png"
</p>

# Painel de consulta

Pequeno painel simples que permite consultar os seguintes dados:

```
:: ::::::::::::::::::::::::: ::
-------------------------------
| MEU IP:              [X]    |
| IP:                  [X]    |
| COVID19:             [X]    |
| CNPJ:                [X]    |
| CEP:                 [X]    |
| DDD:                 [X]    |
| CPF:                 [ ]    |
| PLACA:               [ ]    |
| TELEFONE:            [ ]    |
-------------------------------
:: ::::::::::::::::::::::::: ::
```
## Necessário a biblioteca Requests 
Caso não tenha instalado:

``` > pip install requests ```

## Instalação e acesso (Linux e Termux)
pt.1
```shell script
> apt update && apt upgrade -y
> pkg i python git
> pip install requests
```
pt.2
```shell script
> git clone https://github.com/lauansantana/painel-de-consulta
> cd painel-de-consulta
> python3 painel.py
```
