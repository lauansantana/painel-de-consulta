import requests
import json
import os
from bases import ddd

# Optei por juntar todos os scripts em um único código, ao invés de importar eles da pasta 'bases'

def clearw():
    os.system('cls')

def clear():
    os.system('clear')

# Meu IP
def cabecalho_meuip():
    print("** ::::::::::::::::::::::::::::: **")
    print(":: ::::::: IP Encontrado ::::::: ::")
    print("** ::::::::::::::::::::::::::::: **")
    print('')

def consulta_meuip():
    restart = 's'
    while restart == 's':
        while True:
            clear()
            clearw()
            cabecalho_meuip()
            requisicao = requests.get('http://ip-api.com/json/')
            requisicao_meuip = requisicao.json()

            print('IP: {}'.format(requisicao_meuip['query']))
            print('País: {}'.format(requisicao_meuip['country']))
            print('Região: {}'.format(requisicao_meuip['regionName']))
            print('Cidade: {}'.format(requisicao_meuip['city']))
            print('Provedor: {}'.format(requisicao_meuip['isp']))
            print('Latitude: {}'.format(requisicao_meuip['lat']))
            print('Longitude: {}'.format(requisicao_meuip['lon']))
            print('')
            restart = str(input('Deseja realizar outra consulta? S/N: '))
            break


# IP
def cabecalho_ip(): 
    print("** ::::::::::::::::::::::::::::: **")
    print(":: :::::: Consulta de IP ::::::: ::")
    print("** ::::::::::::::::::::::::::::: **")
    print('')

def cabecalho_ip2():
    print("** ::::::::::::::::::::::::::::: **")
    print(":: ::::::: IP Encontrado ::::::: ::")
    print("** ::::::::::::::::::::::::::::: **")
    print('')

def consulta_ip():
    clear()
    clearw()
    cabecalho_ip2()
    restart_cep = 's'
    while restart_cep == 's':
        while True:
            ip_input = input('Digite o IP: ')
            if len(ip_input) !=15:
                clear()
                clearw()
                print('IP Inválido:')
                restart_cep = str(input('Deseja realizar outra consulta S/N? '))
                break

            requisicao = requests.get('http://ip-api.com/json/{}'.format(ip_input))
            requisicao_ip = requisicao.json()

            if 'message' not in requisicao_ip:
                clear()
                clearw()
                cabecalho_ip2()
                print('IP: {}'.format(requisicao_ip['query']))
                print('País: {}'.format(requisicao_ip['country']))
                print('Região: {}'.format(requisicao_ip['regionName']))
                print('Cidade: {}'.format(requisicao_ip['city']))
                print('Provedor: {}'.format(requisicao_ip['isp']))
                print('Latitude: {}'.format(requisicao_ip['lat']))
                print('Longitude: {}'.format(requisicao_ip['lon']))
                print('')
                restart_cep = str(input('Deseja realizar outra consulta? S/N '))
                break
            else:
                clear()
                clearw()
                print(requisicao_ip['status'])
                print('IP inválido')
                restart_cep = str(input('Deseja realizar outra consulta? S/N '))
                break

# Covid19
def cabecalho_covid(): 
    print("** ::::::::::::::::::::::::::::: **")
    print(":: ::::::: Consulta Covid :::::: ::")
    print("** ::::::::::::::::::::::::::::: **")
    print('')

def consulta_covid():
    clear()
    clearw()
    cabecalho_covid()
    restart = 's'
    while restart == 's':
        while True:
            estado_input = input(str('Informe a sigla do estado desejado, Ex: BA, SP, RJ:'))

            requisicao = requests.get('https://covid19-brazil-api.vercel.app/api/report/v1/brazil/uf/{}'.format(estado_input))

            estado_requisicao = requisicao.json()


            if 'error' in estado_requisicao:
                restart = str(input('Estado não encontrado. \n Deseja realizar outra consulta S/N? '))
                break
                
            else:
                print('')
                print('UF: {}'.format(estado_requisicao['uf']))
                print('Estado: {}'.format(estado_requisicao['state']))
                print('Casos: {}'.format(estado_requisicao['cases']))
                print('Suspeitos: {}'.format(estado_requisicao['suspects']))
                print('Mortes: {}'.format(estado_requisicao['deaths']))
                print('Recusados: {}'.format(estado_requisicao['refuses']))
                print('Ultima atualização: {}'.format(estado_requisicao['datetime']))
                print('')

                restart = str(input('Deseja realizar outra consulta S/N?'))
                clear()
                clearw()
                break

# CNPJ
def cabecalho_cnpj(): 
    print("** ::::::::::::::::::::::::::::: **")
    print(":: :::::: Consulta de CNPJ ::::: ::")
    print("** ::::::::::::::::::::::::::::: **")
    print('')

def cabecalho_cnpj2():
    print("** ::::::::::::::::::::::::::::: **")
    print(":: :::::: CNPJ Encontrado :::::: ::")
    print("** ::::::::::::::::::::::::::::: **")
    print('')

def consulta_cnpj():
    clear()
    clearw()
    restart = 's'
    while restart == 's':
        while True:
            cabecalho_cnpj()
            cnpj_input = input('Informe o CNPJ: ')
            if len(cnpj_input) !=14:
                clear()
                clearw()
                print('CNPJ inválido')
                restart = str(input('Deseja realizar uma nova consulta? S/N'))
                break

            request_cnpj = requests.get('https://www.receitaws.com.br/v1/cnpj/{}'.format(cnpj_input))
            requisicao_cnpj = request_cnpj.json()
            
            if 'message' in requisicao_cnpj:
                clear()
                clearw()
                print(requisicao_cnpj['message'])
                restart = str(input('Deseja realizar uma nova consulta? S/N '))
                break

            else:
                clear()
                clearw()
                cabecalho_cnpj2()
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

#CEP
def cabecalho_cep(): 
    print("** ::::::::::::::::::::::::::::: **")
    print(":: :::::: Consulta de CEP :::::: ::")
    print("** ::::::::::::::::::::::::::::: **")
    print('')

def cabecalho_cep2():
    print("** ::::::::::::::::::::::::::::: **")
    print(":: ::::::: CEP Encontrado :::::: ::")
    print("** ::::::::::::::::::::::::::::: **")
    print('')

def consulta_cep():

    clear()
    clearw()
    cabecalho_cep()
    restart = 's'
    while restart == 's':
        while True:
            cep_input = input('Digite o cep:')
            if len(cep_input) != 8:
                print('Quantidade de dígitos inválida')
                restart = str(input('Deseja realizar outra consulta S/N? '))
                break

            requisicao = requests.get('https://cep.awesomeapi.com.br/json/{}'.format(cep_input))

            requisicao_cep = requisicao.json()


            if 'status' not in requisicao_cep:
                clear()
                clearw()
                cabecalho_cep2()
                print('CEP: {}'.format(requisicao_cep['cep']))
                print('Endereço: {}'.format(requisicao_cep['address']))
                print('Bairro: {}'.format(requisicao_cep['district']))
                print('Cidade: {}'.format(requisicao_cep['city']))
                print('Estado: {}'.format(requisicao_cep['state']))
                print('DDD: {}'.format(requisicao_cep['ddd']))
                print('Latitude: {}'.format(requisicao_cep['lat']))
                print('Longitude: {}'.format(requisicao_cep['lng']))
                print('')
                restart = str(input('Deseja realizar outra consulta S/N? '))
                break
            else:
                print('{}'.format(requisicao_cep['message']))
                restart = str(input('Deseja realizar outra consulta S/N? '))
                break

# DDD
def cabecalho_ddd(): 
    print("** ::::::::::::::::::::::::::::: **")
    print(":: :::::: Consulta de DDD :::::: ::")
    print("** ::::::::::::::::::::::::::::: **")
    print('')

    
def consulta_ddd():
    clear()
    clearw()
    cabecalho_ddd()
    restart = 's'
    while restart == 's':
        while True:
            ddd_input = input('Digite o DDD: ')
            if len(ddd_input) !=2:
                clear()
                clearw()
                print('DDD Inválido:')
                restart = str(input('Deseja realizar outra consulta S/N? '))
                break

            requisicao = requests.get('https://brasilapi.com.br/api/ddd/v1/{}'.format(ddd_input))
            requisicao_ddd = requisicao.json()

            if 'message' not in requisicao_ddd:
                clear()
                clearw()
                print('Estado: {}'.format(requisicao_ddd['state']))
                print('Cidades: {}'.format(requisicao_ddd['cities']))
                print('')
                restart = str(input('Deseja realizar outra consulta? S/N '))
                break
            else:
                clear()
                clearw()
                print('DDD nao encontrado')
                restart = str(input('Deseja realizar outra consulta? S/N '))
                break


def menu():
    clear()
    clearw()
    print("** ::::::::::::::::::::::::: **")
    print(":: :: PAINEL DE CONSULTA  :: ::")
    print("** ::::::::::::::::::::::::: **")
    print("-------------------------------")
    print("| MEU IP:          ->  [1]    |")
    print("| IP:              ->  [2]    |")
    print("| COVID19:         ->  [3]    |")
    print("| CNPJ:            ->  [4]    |")
    print("| CEP:             ->  [5]    |")
    print("| DDD:             ->  [6]    |")
    print("-------------------------------")
    print("** ::::::::::::::::::::::::: **")
    print('')

restart = 's'
while restart == 's':
    while True:
        menu()
        escolha = (input('Escolha a opção desejada: '))
        if escolha == '1':
            consulta_meuip()
        elif escolha == '2':
            consulta_ip()
        elif escolha == '3':
            consulta_covid()
        elif escolha == '4':
            consulta_cnpj()
        elif escolha == '5':
            consulta_cep()
        elif escolha == '6':
            consulta_ddd()
        else:
            restart = str(input('Entrada Inválida.\nDeseja tentar novamente? S/N '))
            break
