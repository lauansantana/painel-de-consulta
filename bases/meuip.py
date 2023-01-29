import requests
import json
import os

def clear():
    os.system('cls')

def cabecalho2():
    print("** ::::::::::::::::::::::::::::: **")
    print(":: ::::::: IP Encontrado ::::::: ::")
    print("** ::::::::::::::::::::::::::::: **")
    print('')

def consulta():
    restart = 's'
    while restart == 's':
        while True:
            clear()
            cabecalho2()
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
            restart = str(input('Para sair digite N: '))
            break

