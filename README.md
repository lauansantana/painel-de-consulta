# Painel de consulta

Pequeno painel simples que permite consultar os seguintes dados:

```
:: ::::::::::::::::::::::::: ::
:: :: PAINEL DE CONSULTA  :: ::
:: ::::::::::::::::::::::::: ::
-------------------------------
| MEU IP:              [X]    |
| IP:                  [X]    |
| COVID19:             [X]    |
| CNPJ:                [X]    |
| CEP:                 [X]    |
| CPF:                 [ ]    |
| PLACA:               [ ]    |
| TELEFONE:            [ ]    |
-------------------------------
:: ::::::::::::::::::::::::: ::
```

## Instalação e acesso (Linux e Termux)
pt.1
```shell script
apt update && apt upgrade -y
pkg i python git
pip install requests
```
pt.2
```shell script
git clone https://github.com/lauansantana/painel-de-consulta
cd painel-de-consulta
python3 painel.py
```
