import requests
import json
import os

def clear():
    os.system('cls')

def cabecalho(): 
    print("** ::::::::::::::::::::::::::::: **")
    print(":: :::::: Consulta de IP ::::::: ::")
    print("** ::::::::::::::::::::::::::::: **")
    print('')

def cabecalho2():
    print("** ::::::::::::::::::::::::::::: **")
    print(":: ::::::: IP Encontrado ::::::: ::")
    print("** ::::::::::::::::::::::::::::: **")
    print('')
    
def consulta():
    clear()
    cabecalho()
    restart = 's'
    while restart == 's':
        while True:
            ip_input = input('Digite o IP: ')
            if len(ip_input) !=15:
                clear()
                print('IP Inválido:')
                restart = str(input('Deseja realizar outra consulta S/N? '))
                break

            requisicao = requests.get('http://ip-api.com/json/{}'.format(ip_input))
            requisicao_ip = requisicao.json()

            if 'message' not in requisicao_ip:
                clear()
                cabecalho2()
                print('IP: {}'.format(requisicao_ip['query']))
                print('País: {}'.format(requisicao_ip['country']))
                print('Região: {}'.format(requisicao_ip['regionName']))
                print('Cidade: {}'.format(requisicao_ip['city']))
                print('Provedor: {}'.format(requisicao_ip['isp']))
                print('Latitude: {}'.format(requisicao_ip['lat']))
                print('Longitude: {}'.format(requisicao_ip['lon']))
                print('')
                restart = str(input('Deseja realizar outra consulta? S/N '))
                break
            else:
                clear()
                print(requisicao_ip['status'])
                print('IP inválido')
                restart = str(input('Deseja realizar outra consulta? S/N '))
                break
