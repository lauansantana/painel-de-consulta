import requests
import json
import os

def clear():
    os.system('cls')

def cabecalho_ddd(): 
    print("** ::::::::::::::::::::::::::::: **")
    print(":: :::::: Consulta de DDD :::::: ::")
    print("** ::::::::::::::::::::::::::::: **")
    print('')

    
def consulta_ddd():
    clear()
    cabecalho_ddd()
    restart = 's'
    while restart == 's':
        while True:
            ddd_input = input('Digite o DDD: ')
            if len(ddd_input) !=2:
                clear()
                print('DDD Inválido:')
                restart = str(input('Deseja realizar outra consulta S/N? '))
                break

            requisicao = requests.get('https://brasilapi.com.br/api/ddd/v1/{}'.format(ddd_input))
            requisicao_ddd = requisicao.json()

            if 'message' not in requisicao_ddd:
                clear()
                print('Estado: {}'.format(requisicao_ddd['state']))
                print('Cidades: {}'.format(requisicao_ddd['cities']))
                print('')
                restart = str(input('Deseja realizar outra consulta? S/N '))
                break
            else:
                clear()
                print('DDD nao encontrado')
                restart = str(input('Deseja realizar outra consulta? S/N '))
                break
