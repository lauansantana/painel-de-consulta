import requests
import json
import os

def clear():
    os.system('cls')

def cabecalho(): 
    print("** ::::::::::::::::::::::::::::: **")
    print(":: :::::: Consulta de CNPJ ::::: ::")
    print("** ::::::::::::::::::::::::::::: **")
    print('')

def cabecalho2():
    print("** ::::::::::::::::::::::::::::: **")
    print(":: :::::: CNPJ Encontrado :::::: ::")
    print("** ::::::::::::::::::::::::::::: **")
    print('')

def consulta():
    clear()
    restart = 's'
    while restart == 's':
        while True:
            cabecalho()
            cnpj_input = input('Informe o CNPJ: ')
            if len(cnpj_input) !=14:
                clear()
                print('CNPJ inválido')
                restart = str(input('Deseja realizar uma nova consulta? S/N'))
                break

            request_cnpj = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj_input))
            requisicao_cnpj = request_cnpj.json()
            
            if 'message' in requisicao_cnpj:
                clear()
                print(requisicao_cnpj['message'])
                restart = str(input('Deseja realizar uma nova consulta? S/N '))
                break

            else:
                clear()
                cabecalho2()
                print('CNPJ: {}'.format(requisicao_cnpj['cnpj']))
                print('Abertura: {}'.format(requisicao_cnpj['abertura']))
                print('Situação: {}'.format(requisicao_cnpj['tipo']))
                print('Tipo: {}'.format(requisicao_cnpj['nome']))
                print('Nome fantasia: {}'.format(requisicao_cnpj['fantasia']))
                print('Porte: {}'.format(requisicao_cnpj['porte']))
                print('Atividade principal: {}'.format(requisicao_cnpj['atividade_principal'][0]['text']))
                print('Atividades secundárias: {}'.format(requisicao_cnpj['atividades_secundarias'][0]['text']))
                print('')
                print('Logradouro: {}'.format(requisicao_cnpj['logradouro']))
                print('Número: {}'.format(requisicao_cnpj['numero']))
                print('Complement: {}'.format(requisicao_cnpj['complemento']))
                print('Município: {}'.format(requisicao_cnpj['municipio']))
                print('Bairro: {}'.format(requisicao_cnpj['bairro']))
                print('UF: {}'.format(requisicao_cnpj['uf']))
                print('CEP: {}'.format(requisicao_cnpj['cep']))
                print('')
                print('Email: {}'.format(requisicao_cnpj['email']))
                print('Telefone: {}'.format(requisicao_cnpj['telefone']))
                print('Ultima atualização: {}'.format(requisicao_cnpj['ultima_atualizacao']))
                print('Status: {}'.format(requisicao_cnpj['status']))
                print('Capital Social: {}'.format(requisicao_cnpj['capital_social']))
                print('')
                restart = str(input('Deseja realizar uma nova consulta? S/N '))
                break

consulta()