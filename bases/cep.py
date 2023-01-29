import requests
import os

def clear():
    os.system('cls')

def cabecalho(): 
    print("** ::::::::::::::::::::::::::::: **")
    print(":: :::::: Consulta de CEP :::::: ::")
    print("** ::::::::::::::::::::::::::::: **")
    print('')

def cabecalho2():
    print("** ::::::::::::::::::::::::::::: **")
    print(":: ::::::: CEP Encontrado :::::: ::")
    print("** ::::::::::::::::::::::::::::: **")
    print('')

def consulta():

    clear()
    cabecalho()
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
                cabecalho2()
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
consulta()