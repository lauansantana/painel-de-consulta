import requests
import json
import os

def clear():
    os.system('cls')
def cabecalho(): 
    print("** ::::::::::::::::::::::::::::: **")
    print(":: ::::::: Consulta Covid :::::: ::")
    print("** ::::::::::::::::::::::::::::: **")
    print('')

def consulta():
    clear()
    cabecalho()
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
                break