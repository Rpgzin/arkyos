import cmd
import textwrap
import sys
import os
import time
import random
import colorama
from colorama import Fore, Back, Style
from utilitarios import(
    limpar_tela,
    loading,
    intervalo
)

colorama.init()

#TO-DO:
'''
Drop de itens especificos de boss
'''

######### Setup do jogador ########
class Player:
    def __init__(self):
        self.nome = ''
        self.classe = ''
        self.nivel = 1
        self.xp = 0
        self.xp_max = 100
        self.vida_base = 0
        self.vida = 0
        self.vida_max = 0
        self.mana_base = 0
        self.mana = 0
        self.mana_max = 0
        self.forca = 1
        self.fortitude = 1
        self.inteligencia = 1
        self.atk_base = 0
        self.atk = 0
        self.dano_magico = 0
        self.ouro = 500
        self.atk_final = self.atk
        self.item_equipado = None
        self.mochila = []
        self.efeitos_status = []
        self.magias = []
        self.local = 'começo'
        self.game_over = False
        self.pular_turno = False
    
    def add_item(self, item):
        self.mochila.append(item)
    
    def add_efeito(self, efeito):
        for i, efeito_existente in enumerate(self.efeitos_status):
            if efeito_existente.nome == efeito.nome:
                efeito.tempo += efeito_existente.tempo
                self.efeitos_status.pop(i)
        self.efeitos_status.append(efeito)

meu_jogador = Player()

def calcular_atributos(jogador):
    jogador.vida_max = jogador.vida_base + (jogador.fortitude * 10)
    jogador.vida = jogador.vida_max
    jogador.mana_max = jogador.mana_base + (jogador.inteligencia * 8)
    jogador.mana = jogador.mana_max
    jogador.atk = jogador.atk_base + (jogador.forca * 2)
    jogador.atk_final = jogador.atk
    if jogador.item_equipado:
        jogador.atk_final += jogador.item_equipado.atk
    jogador.dano_magico = jogador.inteligencia * 2

def atualizar_atributos(jogador):
    jogador.vida_max = jogador.vida_base + (jogador.fortitude * 10)
    jogador.mana_max = jogador.mana_base + (jogador.inteligencia * 8)
    jogador.atk = jogador.atk_base + (jogador.forca * 2)
    jogador.atk_final = jogador.atk
    if jogador.item_equipado:
        jogador.atk_final += jogador.item_equipado.atk
    jogador.dano_magico = jogador.inteligencia * 2

def subi_nivel(jogador):
    jogador.nivel += 1
    print(f'{jogador.nome} subiu de nivel para o LVL:'+Fore.GREEN+f'{jogador.nivel}'+Style.RESET_ALL+'!!!')
    pontos = 0
    while jogador.xp >= jogador.xp_max:
        pontos += 3
        resto_xp = jogador.xp - jogador.xp_max
        jogador.xp = resto_xp
        jogador.xp_max +=50
    while pontos > 0:
        print(f'Pontos restantes: '+Fore.YELLOW+f'{pontos}')
        escolha = input(Fore.GREEN+"Aumentar Forca (for)"+Style.RESET_ALL+", "+Fore.RED+"Fortitude (fort)"+Style.RESET_ALL+" ou "+Fore.BLUE+"Inteligência (int)"+Style.RESET_ALL+": ").lower()
        if escolha == 'for':
            jogador.forca += 1
            print(f'for: {jogador.forca}')
        elif escolha == 'fort':
            jogador.fortitude += 1
            print(f'fortitude: {jogador.fortitude}')
        elif escolha == 'int':
            jogador.inteligencia += 1
            print(f'inteligência: {jogador.inteligencia}')
        else:
            print(Fore.RED+'Comando invádido'+Style.RESET_ALL)
            continue
        pontos -= 1
    atualizar_atributos(meu_jogador)

def exibir_status(jogador):
    limpar_tela()
    print('▬'*100)
    print('''
        ┌───────────────────────────────────────────────────┐
        │███████╗████████╗ █████╗ ████████╗██╗   ██╗███████╗│
        │██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║   ██║██╔════╝│
        │███████╗   ██║   ███████║   ██║   ██║   ██║███████╗│
        │╚════██║   ██║   ██╔══██║   ██║   ██║   ██║╚════██║│
        │███████║   ██║   ██║  ██║   ██║   ╚██████╔╝███████║│
        │╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝│
        └───────────────────────────────────────────────────┘   
'''.upper())
    print(f'Nome:{jogador.nome} LVL: {jogador.nivel}'+Style.RESET_ALL+f' XP: {jogador.xp}/{jogador.xp_max}')
    print('vida:'+Fore.RED+f' {jogador.vida}/{jogador.vida_max}'+Style.RESET_ALL+ ' / MANA: '+Fore.BLUE+f'{jogador.mana}/{jogador.mana_max}'+Style.RESET_ALL+' / ATK: '+Fore.YELLOW+f'{jogador.atk}'+Style.RESET_ALL+' / MAG.ATK: '+Fore.LIGHTBLUE_EX+f'{jogador.dano_magico}')
    if jogador.item_equipado:
        print(f'arma: {jogador.item_equipado.nome} ATK: {jogador.item_equipado.atk}')
    else:
        print('arma: Nenhuma arma equipada')
    print(f'forca: {jogador.forca} fortitude: {jogador.fortitude} inteligência: {jogador.inteligencia}')

class Monstro:
    def __init__(self, nome, vida, nivel, atk, xp, ouro, boss, atk_efeito=None, drops=None):
        self.nome = nome
        self.vida = vida*nivel
        self.vida_max = vida*nivel
        self.nivel = nivel
        self.atk = atk
        self.xp = xp
        self.ouro = ouro
        self.drops = drops if drops else []  # Lista de itens que o monstro dropa
        self.boss = boss
        self.efeitos_status = []
        self.pular_turno = False
        self.atk_turnos = 0
        self.atk_efeito = atk_efeito

    def add_efeito(self, efeito):
        for i, efeito_existente in enumerate(self.efeitos_status):
            if efeito_existente.nome == efeito.nome:
                efeito.tempo += efeito_existente.tempo
                self.efeitos_status.pop(i)
        self.efeitos_status.append(efeito)

def encontro_aleatorio():
    if meu_jogador.local != 'c1':
        print('Você não está em um circulo de invocação!')
        main_game_loop()
    numero = random.randint(0, 1)
    if numero == 0:
        print('Um monstro apareceu!')
        luta(monstro_aleatorio(), meu_jogador)
    else:
        print('Falha na invocação!!! Você recebeu 5 de dano!')
        meu_jogador.vida -= 5
        main_game_loop()

def monstro_aleatorio():
    monstro_invocacao = random.choice(lista_monstros_invocacoes)
    return Monstro(monstro_invocacao['nome'], monstro_invocacao['vida'], monstro_invocacao['nivel'], monstro_invocacao['atk'], monstro_invocacao['xp'], monstro_invocacao['ouro'], monstro_invocacao['boss'])

def experiencia(monstro):
    meu_jogador.xp += monstro.xp
    if meu_jogador.xp >= meu_jogador.xp_max:
        subi_nivel(meu_jogador)

class Item:
    def __init__(self, nome, atk, desc, equipado, consumivel, preco, especial):
        self.nome = nome
        self.atk = atk
        self.desc = desc
        self.equipado = equipado
        self.consumivel = consumivel
        self.preco = preco
        self.especial = especial
    
class Magia:
    def __init__(self, nome, dano, desc, mana_gasta, efeito=None):
        self.nome = nome
        self.dano = dano
        self.desc = desc
        self.mana_gasta = mana_gasta
        self.efeito = efeito

class Efeito:
    def __init__(self, nome, tipo, tempo, dano=None):
        self.nome = nome
        self.tipo = tipo
        self.tempo = tempo
        self.dano = dano

def mostrar_loja():
        if meu_jogador.game_over:
            main_game_loop() 
        if meu_jogador.local != 'b2':
            print('NãO HÁ LOJAS POR AQUI')
            main_game_loop()
        print('Itens para venda:')
        for i in range(len(lista_itens_loja)):
            status = '(COMPRADO)' if lista_itens_loja[i]["comprado"] else ''
            if not lista_itens_loja[i]['consumivel']:
                print(f"{i+1}. {lista_itens_loja[i]['nome']} | ATK: {lista_itens_loja[i]['atk']} | Preço: {lista_itens_loja[i]['preco']} - Descricao: {lista_itens_loja[i]['desc']} {status}\n")
                continue
            print(f"{i+1}. {lista_itens_loja[i]['nome']} | Preço: {lista_itens_loja[i]['preco']} | Descricao: {lista_itens_loja[i]['desc']} {status}\n")
        print(f'Ouro: {meu_jogador.ouro}')
        print('>> USE NÚMEROS PARA SELECIONAR O ITEM OU [vender | fechar]')
        escolha = input(Fore.LIGHTYELLOW_EX + '>>'+ Style.RESET_ALL).lower()
        if escolha == 'fechar':
            print_local()
        elif escolha == 'vender':
            limpar_tela()
            vender_item()
        try:
            escolha = int(escolha)-1
            if escolha not in range(0, len(lista_itens_loja)):
                if meu_jogador.game_over:
                    main_game_loop() 
                print('**ITEM INVÁLIDO**')
                mostrar_loja()
            
            if lista_itens_loja[escolha]['consumivel']:
                print(f"{lista_itens_loja[escolha]['nome']} | Preço: {lista_itens_loja[escolha]['preco']} | Descricao: {lista_itens_loja[escolha]['desc']} {status}\n")
            else:
                print(f"{lista_itens_loja[escolha]['nome']} | ATK: {lista_itens_loja[escolha]['atk']} | Preço: {lista_itens_loja[escolha]['preco']} | Descricao: {lista_itens_loja[escolha]['desc']} {status}\n")
            print('[compra | voltar | fechar]')
            acao = input(Fore.LIGHTYELLOW_EX + '>>'+Style.RESET_ALL)
            if acao not in ['comprar', 'voltar', 'fechar']:
                print('**COMANDO INVÁLIDO**')
                mostrar_loja()
            if acao == 'comprar':
                comprar(escolha)
            elif acao == 'voltar':
                mostrar_loja()
            elif acao == 'fechar':
                print_local()

        except:
            if meu_jogador.game_over:
                main_game_loop() 
            print('**ITEM INVÁLIDO**')
            mostrar_loja()

def vender_item():
    print('ITENS DA MOCHILA:')
    for i, item in enumerate(meu_jogador.mochila):
        if item.equipado:
            print(f'{i+1}. {item.nome} | {item.desc} | valor: {item.preco} | (EQUIPADO)')
            continue
        print(f'{i+1}. {item.nome} | {item.desc} | valor: {item.preco}')
    print('>> USE NÚMEROS PARA SELECIONAR O ITEM OU [comprar | fechar]')
    escolha = input(Fore.LIGHTYELLOW_EX + '>>'+Style.RESET_ALL).lower()
    if escolha == 'fechar':
        print_local()
    elif escolha == 'comprar':
        limpar_tela()
        mostrar_loja()
    try:
        escolha = int(escolha)-1
        if escolha not in range(0, len(lista_itens_loja)):
            print('**ITEM INVÁLIDO**')
            vender_item()
        
        if meu_jogador.mochila[escolha].equipado:
            print(f'{meu_jogador.mochila[escolha].nome} | {meu_jogador.mochila[escolha].desc} | valor: {meu_jogador.mochila[escolha].preco} | (EQUIPADO)')
        else:
            print(f'{meu_jogador.mochila[escolha].nome} | {meu_jogador.mochila[escolha].desc} | valor: {meu_jogador.mochila[escolha].preco}')
        print('[vender | voltar | fechar]')
        acao = input(Fore.LIGHTYELLOW_EX + '>>'+Style.RESET_ALL)
        if acao not in ['vender', 'voltar', 'fechar']:
            print('**COMANDO INVÁLIDO**')
            vender_item()
        if acao == 'vender':
            if meu_jogador.mochila[escolha].especial:
                print('Item não pode ser vendido')
                vender_item()
            vender_acao(escolha)
        elif acao == 'voltar':
            vender_item()
        elif acao == 'fechar':
            print_local()
    except:
        print('**ITEM INVÁLIDO**')
        vender_item()

def vender_acao(escolha):
    item = meu_jogador.mochila[escolha]
    meu_jogador.ouro += item.preco
    if item.equipado:
        meu_jogador.item_equipado = None
        meu_jogador.atk = meu_jogador.atk_base + (meu_jogador.forca * 2)
        meu_jogador.atk_final = meu_jogador.atk
    meu_jogador.mochila.pop(escolha)
    vender_item()

def add_item_comprado(item):
    if lista_itens_loja[0]['comprado'] == True:
        meu_jogador.add_item(item)

def pocao_vida():
    meu_jogador.vida += 15
    if meu_jogador.vida > meu_jogador.vida_max:
        meu_jogador.vida = meu_jogador.vida_max
    print ("Você bebeu a poção!!!")
def pocao_vida_media():
    meu_jogador.vida += 30
    if meu_jogador.vida > meu_jogador.vida_max:
        meu_jogador.vida = meu_jogador.vida_max
    print ("Você bebeu a poção!!!")
def pocao_vida_alta():
    meu_jogador.vida += 60
    if meu_jogador.vida > meu_jogador.vida_max:
        meu_jogador.vida = meu_jogador.vida_max
    print ("Você bebeu a poção!!!")

def pocao_mana():
    meu_jogador.mana += 15
    if meu_jogador.mana > meu_jogador.mana_max:
        meu_jogador.mana = meu_jogador.mana_max
    print ("Você bebeu a poção!!!")
def pocao_mana_media():
    meu_jogador.mana += 30
    if meu_jogador.mana > meu_jogador.mana_max:
        meu_jogador.mana = meu_jogador.mana_max
    print ("Você bebeu a poção!!!")
def pocao_mana_alta():
    meu_jogador.mana += 60
    if meu_jogador.mana > meu_jogador.mana_max:
        meu_jogador.mana = meu_jogador.mana_max
    print (" você bebeu a poção!!!")

lista_itens_loja = [
    { 'nome': 'Espada de ferro', 'atk': 5, 'preco': 100, 'desc': 'Uma espada de ferro, muito forte.', 'item': 'espada de ferro', 'comprado': False, 'equipado': False, 'consumivel': False, 'especial': False},
    { 'nome': 'Arco longo', 'atk': 4,'preco': 100, 'desc': 'Um arco longo, muito forte.', 'item': 'arco longo', 'comprado': False, 'equipado': False, 'consumivel': False, 'especial': False},
    { 'nome': 'Pocao de vida baixa', 'atk': 0,'preco': 50, 'desc': 'Uma pocao de vida baixa, cura 15 pontos de vida.', 'item': 'pocao de vida baixa', 'comprado': False, 'equipado': False, 'consumivel': True, 'especial': False},
    { 'nome': 'Pocao de vida media', 'atk': 0,'preco': 100, 'desc': 'Uma pocao de vida media, cura 30 pontos de vida.', 'item': 'pocao de vida media', 'comprado': False, 'equipado': False, 'consumivel': True, 'especial': False},
    { 'nome': 'Pocao de vida alta', 'atk': 0,'preco': 150, 'desc': 'Uma pocao de vida alta, cura 60 pontos de vida.', 'item': 'pocao de vida alta', 'comprado': False, 'equipado': False, 'consumivel': True, 'especial': False},
    { 'nome': 'Pocao de mana baixa', 'atk': 0,'preco': 50, 'desc': 'Uma pocao de mana baixa, cura 20 pontos de mana.', 'item': 'pocao de mana baixa', 'comprado': False, 'equipado': False, 'consumivel': True, 'especial': False},
    { 'nome': 'Pocao de mana media', 'atk': 0,'preco': 50, 'desc': 'Uma pocao de mana media, cura 20 pontos de mana.', 'item': 'pocao de mana media', 'comprado': False, 'equipado': False, 'consumivel': True, 'especial': False},
    { 'nome': 'Pocao de mana alta', 'atk': 0,'preco': 50, 'desc': 'Uma pocao de mana alta, cura 20 pontos de mana.', 'item': 'pocao de mana alta', 'comprado': False, 'equipado': False, 'consumivel': True, 'especial': False},
]

lista_consumiveis = [
    { 'nome': 'Pocao de vida baixa', 'atk': 0,'preco': 50, 'desc': 'Uma pocao de vida, cura 15 pontos de vida.', 'equipado': False, 'consumivel': True, 'especial': False},
    { 'nome': 'Pocao de vida media', 'atk': 0,'preco': 100, 'desc': 'Uma pocao de vida media, cura 30 pontos de vida.', 'comprado': False, 'equipado': False, 'consumivel': True, 'especial': False},
    { 'nome': 'Pocao de vida alta', 'atk': 0,'preco': 150, 'desc': 'Uma pocao de vida alta, cura 60 pontos de vida.', 'comprado': False, 'equipado': False, 'consumivel': True, 'especial': False},
    { 'nome': 'Pocao de mana baixa', 'atk': 0,'preco': 50, 'desc': 'Uma pocao de mana, cura 15 pontos de mana.', 'equipado': False, 'consumivel': True, 'especial': False},
    { 'nome': 'Pocao de mana media', 'atk': 0,'preco': 100, 'desc': 'Uma pocao de mana media, cura 30 pontos de mana.', 'comprado': False, 'equipado': False, 'consumivel': True, 'especial': False},
    { 'nome': 'Pocao de mana alta', 'atk': 0,'preco': 150, 'desc': 'Uma pocao de mana alta, cura 60 pontos de mana.', 'comprado': False, 'equipado': False, 'consumivel': True, 'especial': False},
]

lista_armas = [
    {'nome': 'Adaga enferrujada', 'atk': 3, 'preco': 100, 'desc': 'Parece ser bem antiga', 'equipado': False, 'consumivel': False, 'especial': False},
    {'nome': 'Varinha capenga', 'atk': 3, 'preco': 100, 'desc': 'É nova, mas bem barata', 'equipado': False, 'consumivel': False, 'especial': False},
    {'nome': 'Espada longa', 'atk': 4, 'preco': 100, 'desc': 'A espada de todo guerreiro.', 'equipado': False, 'consumivel': False, 'especial': False},
    {'nome': 'Grimório', 'atk': 2, 'preco': 100, 'desc': 'O grimório de um mago, o local de sua sabedoria.', 'equipado': False, 'consumivel': False, 'especial': False},
]
lista_armas_especiais = [
    {'nome': 'Manoplas de ferro', 'atk': 20, 'preco': 150, 'desc': 'Usada a muito tempo por um exímio monge, as manoplas de ferro são uma das mais fortes armas de um monge', 'equipado': False, 'consumivel': False, 'especial': False},
    {'nome': 'Espada do guerreiro impetuoso', 'atk': 15, 'preco': 150, 'desc': 'espada usada por um guerreiro impetuoso, ela tem um grande poder de ataque', 'equipado': False, 'consumivel': False, 'especial': False},
    {'nome': 'Grimório Morbius', 'atk': 0, 'preco': 150, 'desc': 'Um grimório desconhecido e com um grande potencial', 'equipado': False, 'consumivel': False, 'especial': False},    
]

lista_itens_especiais = [
    {'nome': 'Anel Desconhecido', 'atk': 0, 'preco': 00, 'desc': 'Um anel feito de ouro. Sua origem é desconhecida.', 'equipado': False, 'consumivel': False, 'especial': True},
    {'nome': 'Máscara da Raiva', 'atk': 0, 'preco': 00, 'desc': 'Máscara pega no Salão das Vozes Vazias. O uso da mesma é desconhecido.', 'equipado': False, 'consumivel': False, 'especial': True},
    {'nome': 'Máscara da Medo', 'atk': 0, 'preco': 00, 'desc': 'Máscara pega no Salão das Vozes Vazias. O uso da mesma é desconhecido.', 'equipado': False, 'consumivel': False, 'especial': True},
    {'nome': 'Máscara da Alegria', 'atk': 0, 'preco': 00, 'desc': 'Máscara pega no Salão das Vozes Vazias. O uso da mesma é desconhecido.', 'equipado': False, 'consumivel': False, 'especial': True},
    {'nome': 'Máscara da Loucura', 'atk': 0, 'preco': 00, 'desc': 'Máscara pega no Salão das Vozes Vazias. O uso da mesma é desconhecido.', 'equipado': False, 'consumivel': False, 'especial': True},
]  
lista_itens_bosses = [
    { 'nome': 'Pocao de vida baixa', 'atk': 0,'preco': 50, 'desc': 'Uma pocao de vida, cura 15 pontos de vida.', 'equipado': False, 'consumivel': True, 'especial': False},
    { 'nome': 'Pocao de mana baixa', 'atk': 0,'preco': 50, 'desc': 'Uma pocao de mana, cura 15 pontos de mana.', 'equipado': False, 'consumivel': True, 'especial': False},

] 

lista_magias = [
    {'nome': 'Bola de fogo', 'dano': 200, 'desc':'A magia mais forte de um mago', 'mana_gasta': 30},
    {'nome': 'Rajada de Gelo', 'dano': 10, 'desc':'Esfrio né', 'mana_gasta': 35},
]

lista_efeitos = [
    {'nome': 'queimação', 'tipo': 'dano', 'tempo': 2, 'dano': 5},
    {'nome': 'envenamento', 'tipo': 'dano', 'tempo': 3, 'dano': 4},
    {'nome': 'congelamento', 'tipo': 'pular', 'tempo': 3},
]

lista_monstros_normais = [
    {'nome': 'slime', 'vida': 10, 'nivel': 1, 'atk': 2, 'xp': 150, 'ouro': 100, 'boss': False},
    {'nome': 'goblin', 'vida': 20, 'nivel': 2, 'atk': 4, 'xp': 100, 'ouro': 200, 'boss': False},
    {'nome': 'lobo selvagem', 'vida': 25, 'nivel': 3, 'atk': 5, 'xp': 15, 'ouro': 100, 'boss': False},
    {'nome': 'esqueleto', 'vida': 30, 'nivel': 4, 'atk': 6, 'xp': 20, 'ouro': 200, 'boss': False},
    {'nome': 'zumbi', 'vida': 35, 'nivel': 4, 'atk': 4, 'xp': 18, 'ouro': 100, 'boss': False},
    {'nome': 'morcego gigante', 'vida': 28, 'nivel': 3, 'atk': 6, 'xp': 12, 'ouro': 200, 'boss': False},
    {'nome': 'aranha venenosa', 'vida': 22, 'nivel': 2, 'atk': 7, 'xp': 14, 'ouro': 100, 'boss': False},
    {'nome': 'orc', 'vida': 40, 'nivel': 5, 'atk': 8, 'xp': 25, 'ouro': 200, 'boss': False},
    {'nome': 'troll da caverna', 'vida': 50, 'nivel': 6, 'atk': 10, 'xp': 30, 'ouro': 300, 'boss': False},
    {'nome': 'gárgula', 'vida': 45, 'nivel': 5, 'atk': 9, 'xp': 28, 'ouro': 200, 'boss': False},
]

lista_monstros_invocacoes = [
    {'nome': 'Tieflíngs', 'vida': 50, 'nivel': 5, 'atk': 5, 'xp': 50, 'ouro': 10, 'boss': False},
    {'nome': 'Tieflíngs', 'vida': 50, 'nivel': 6, 'atk': 6, 'xp': 60, 'ouro': 15, 'boss': False},
    {'nome': 'Demônio Inferior', 'vida': 50, 'nivel': 7, 'atk': 7, 'xp': 70, 'ouro': 20, 'boss': False},
    {'nome': 'Demônio Inferior', 'vida': 50, 'nivel': 8, 'atk': 8, 'xp': 80, 'ouro': 25, 'boss': False},
    {'nome': 'Demoníaco', 'vida': 50, 'nivel': 9, 'atk': 9, 'xp': 90, 'ouro': 30, 'boss': False},
    {'nome': 'Demoníaco', 'vida': 50, 'nivel': 10, 'atk': 10, 'xp': 100, 'ouro': 35, 'boss': False},
]
lista_monstros_fixos = [
    {'nome': 'Guardião Enraizado', 'vida': 100, 'nivel': 1, 'atk': 6, 'xp': 40, 'ouro': 50, 'boss': True},
]

def raiva():
    if meu_jogador.local == 'b1' and mapa[meu_jogador.local]['SOLVED'] == False:
        fala1 = 'Máscara da raiva adicionada ao seu inventário!\n'
        for falas in fala1:
            sys.stdout.write(falas)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1.5)
        item1 = lista_itens_especiais[1]
        meu_jogador.add_item(Item(item1['nome'], item1['atk'], item1['desc'], item1['equipado'], item1['consumivel'], item1['preco'], item1['especial']))
        mapa[meu_jogador.local]['SOLVED'] = True  # Marca a sala como resolvida
        limpar_tela()
        print_local()
        main_game_loop()
    else:
        print(Fore.RED +'Comando inválido.'+Style.RESET_ALL)
        locais()
def medo():
    if meu_jogador.local == 'b1' and mapa[meu_jogador.local]['SOLVED'] == False:
        fala2 = 'Máscara do medo adicionada ao seu inventário!\n'
        for falas in fala2:
            sys.stdout.write(falas)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1.5)
        item2 = lista_itens_especiais[2]
        meu_jogador.add_item(Item(item2['nome'], item2['atk'], item2['desc'], item2['equipado'], item2['consumivel'], item2['preco'], item2['especial']))
        mapa[meu_jogador.local]['SOLVED'] = True
        limpar_tela()
        print_local()
        main_game_loop()
    else:
        print(Fore.RED +'Comando inválido.'+Style.RESET_ALL)
        locais()
def alegria():
    if meu_jogador.local == 'b1' and mapa[meu_jogador.local]['SOLVED'] == False:
        fala3 = 'Máscara da alegria adicionada ao seu inventário!\n'
        for falas in fala3:
            sys.stdout.write(falas)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1.5)
        item3 = lista_itens_especiais[3]
        meu_jogador.add_item(Item(item3['nome'], item3['atk'], item3['desc'], item3['equipado'], item3['consumivel'], item3['preco'], item3['especial']))
        mapa[meu_jogador.local]['SOLVED'] = True
        limpar_tela()
        print_local()
        main_game_loop()
    else:
        print(Fore.RED +'Comando inválido.'+Style.RESET_ALL)
        locais()

def loucura():
    if meu_jogador.local == 'b1' and mapa[meu_jogador.local]['SOLVED'] == False:
        fala3 = 'Máscara da loucura adicionada ao seu inventário!\n'
        for falas in fala3:
            sys.stdout.write(falas)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1.5)
        item4 = lista_itens_especiais[4]
        meu_jogador.add_item(Item(item4['nome'], item4['atk'], item4['desc'], item4['equipado'], item4['consumivel'], item4['preco'], item4['especial']))
        mapa[meu_jogador.local]['SOLVED'] = True
        limpar_tela()
        print_local()
        main_game_loop()
    else:
        print(Fore.RED +'Comando inválido.'+Style.RESET_ALL)
        locais()

monstro = lista_monstros_fixos[0]
monstro2 = lista_monstros_normais[1]
efeito_boss = Efeito(lista_efeitos[1]['nome'], lista_efeitos[1]['tipo'], lista_efeitos[1]['tempo'], lista_efeitos[1]['dano'])
guardiao_enraizado = Monstro(monstro['nome'], monstro['vida'], monstro['nivel'], monstro['atk'], monstro['xp'], monstro['ouro'], monstro['boss'], efeito_boss)
monstro_exemplo2 = Monstro(monstro2['nome'], monstro2['vida'], monstro2['nivel'], monstro2['atk'], monstro2['xp'], monstro2['ouro'], monstro2['boss'])

guardiao_enraizado.drops = [
    {'item': Item(lista_itens_bosses[0]['nome'], lista_itens_bosses[0]['atk'],
                 lista_itens_bosses[0]['desc'], lista_itens_bosses[0]['equipado'],
                 lista_itens_bosses[0]['consumivel'], lista_itens_bosses[0]['preco'],
                 lista_itens_bosses[0]['especial']),
     'chance': 1},  
     
    {'item': Item(lista_itens_bosses[1]['nome'], lista_itens_bosses[1]['atk'],
                 lista_itens_bosses[1]['desc'], lista_itens_bosses[1]['equipado'],
                 lista_itens_bosses[1]['consumivel'], lista_itens_bosses[1]['preco'],
                 lista_itens_bosses[1]['especial']),
     'chance': 1},   
]

######### Tela de título #########
def navegação_tela_titulo():
    opção = input(">").lower()
    while opção not in ['jogar', 'ajuda', 'sair']:
        print("Por favor, utilize um comando válido.")
        opção = input(Fore.LIGHTYELLOW_EX + ">>"+Style.RESET_ALL).lower()
    if opção == "jogar":
        setup_jogo()
    elif opção == "ajuda":
        ajuda_menu()
    elif opção == "sair":
        sair()

def tela_titulo():
    limpar_tela()
    titulo ='''
             _____                                                                                 _____ 
            ( ___ )                                                                               ( ___ )
             |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
             |   |                                                                                 |   | 
             |   |    █████████   ███████████   █████   ████ █████ █████    ███████     █████████  |   | 
             |   |   ███░░░░░███ ░░███░░░░░███ ░░███   ███░ ░░███ ░░███   ███░░░░░███  ███░░░░░███ |   | 
             |   |  ░███    ░███  ░███    ░███  ░███  ███    ░░███ ███   ███     ░░███░███    ░░░  |   | 
             |   |  ░███████████  ░██████████   ░███████      ░░█████   ░███      ░███░░█████████  |   | 
             |   |  ░███░░░░░███  ░███░░░░░███  ░███░░███      ░░███    ░███      ░███ ░░░░░░░░███ |   | 
             |   |  ░███    ░███  ░███    ░███  ░███ ░░███      ░███    ░░███     ███  ███    ░███ |   | 
             |   |  █████   █████ █████   █████ █████ ░░████    █████    ░░░███████░  ░░█████████  |   | 
             |   | ░░░░░   ░░░░░ ░░░░░   ░░░░░ ░░░░░   ░░░░    ░░░░░       ░░░░░░░     ░░░░░░░░░   |   | 
             |   |                                                                                 |   | 
             |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
            (_____)                                                                               (_____)
                                            ────────────────────────────────
                                                 Uma torre esquecida...
                                             Onde magia e trevas se colidem
                                            ────────────────────────────────
 '''
    opcoes = Fore.YELLOW + '''
                                                     [@] Jogar
                                                     [@] Ajuda''' + Style.RESET_ALL
    Sair = Fore.RED + '''                            
                                                     [@] Sair      
            
          ''' + Style.RESET_ALL
    for titulo1 in titulo:
        sys.stdout.write(titulo1)
        sys.stdout.flush()
        time.sleep(0.0001)
    for opcao in [opcoes, Sair]:
        sys.stdout.write(opcao)
        sys.stdout.flush()
        time.sleep(0.01)

    navegação_tela_titulo()

def ajuda_menu():
    limpar_tela()
    print('''
             _____                                                                                 _____ 
            ( ___ )                                                                               ( ___ )
             |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
             |   |                                                                                 |   | 
             |   |    █████████   ███████████   █████   ████ █████ █████    ███████     █████████  |   | 
             |   |   ███░░░░░███ ░░███░░░░░███ ░░███   ███░ ░░███ ░░███   ███░░░░░███  ███░░░░░███ |   | 
             |   |  ░███    ░███  ░███    ░███  ░███  ███    ░░███ ███   ███     ░░███░███    ░░░  |   | 
             |   |  ░███████████  ░██████████   ░███████      ░░█████   ░███      ░███░░█████████  |   | 
             |   |  ░███░░░░░███  ░███░░░░░███  ░███░░███      ░░███    ░███      ░███ ░░░░░░░░███ |   | 
             |   |  ░███    ░███  ░███    ░███  ░███ ░░███      ░███    ░░███     ███  ███    ░███ |   | 
             |   |  █████   █████ █████   █████ █████ ░░████    █████    ░░░███████░  ░░█████████  |   | 
             |   | ░░░░░   ░░░░░ ░░░░░   ░░░░░ ░░░░░   ░░░░    ░░░░░       ░░░░░░░     ░░░░░░░░░   |   | 
             |   |                                                                                 |   | 
             |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
            (_____)                                                                               (_____)''')
    print(Fore.YELLOW + '''
          
                        [@]principais comandos: [mover / olhar / mochila / status / mapa]
          
                    [@] Digite seus comandos para executá-los
                    [@] Digite mover para se movimentar
                    [@] Use o comando "olhar" para examinar a área
                    [@] Use o comando "mochila" para abrir a mochila
                    [@] Use o comando "status" para ver seus status
                    [@] Use o comando "mapa" para ver o mapa
                    [@] Boa sorte e não morra :p
          ''' + Style.RESET_ALL)
    
    if meu_jogador.nome != '':
        print(Fore.CYAN + 'Voltar ao game? [s/n]'+Style.RESET_ALL)
        voltar_game = input(Fore.LIGHTYELLOW_EX +'>>'+Style.RESET_ALL).lower()
        if voltar_game != 's':
            limpar_tela()
            ajuda_menu()
        print_local()
        main_game_loop()
    print(Fore.CYAN + "- voltar ao MENU? [s/n]"+Style.RESET_ALL)
    voltar_menu = input(Fore.LIGHTYELLOW_EX +'>>'+Style.RESET_ALL).lower()
    if voltar_menu != 's':
        limpar_tela()
        ajuda_menu()
    tela_titulo()

#### Funções do jogo ####
def start_game():
    meu_jogador.local = 'a1'

#### Mapa #####
DESCRICAO = 'DESCRICAO'
EXAMINAR = 'EXAMINAR'
SOLVED = 'SOLVED'
SUBIR = 'SUBIR'
DESCER = 'DESCER'
AVANÇAR = 'AVANÇAR'
RETORNAR = 'RETORNAR'

lugares_resolvidos = {
    'a1': False, 'a2': False,
    'b1': False, 'b2': False,
    'c1': False, 'c2': False,
    'd1': False, 'd2': False,
}

mapa = {
    'a1': {
        'NOME_LOCAL': 'Sala do Trono',
        'DESCRICAO': 'Uma sala grande e luxuosa, com uma grande mesa em frente ao trono.',
        'EXAMINAR': '\nTudo ao seu redor parece morto.\nPorem voce nota um brilho fraco vindo de frente de um trono destruido.\nDigite trono para examinar o trono.\n',
        'SOLVED': False,
        'SUBIR': '',
        'DESCER': '',
        'AVANÇAR': 'a2',
        'RETORNAR': '',
        'MONSTRO': '',
        'LOCAIS': 'trono',
        'contador' : 0
    },
    'a2': {
        'NOME_LOCAL': "Sala do Guardião Enraizado",
        'DESCRICAO': '''
         Um odor de terra úmida e carne podre invade seus sentidos. A sala adiante parece
         uma antiga estufa esquecida, onde raízes negras tomaram os pilares de pedra...''',
        'EXAMINAR': '''
                      No centro do local, uma árvore retorcida cresce a partir de um altar quebrado. 
                      Seus galhos têm formas humanoides penduradas, como se absorvessem ecos de vida.
                                                        .....
        Uma criatura — metade carne, metade madeira — jaz ajoelhada, presa por correntes de prata, seus olhos fechados.
                       (para enfrentar o guardião Enraizado, digite 'enfrentar', para retornar digite sair)
        ''',
        'SOLVED': False,
        'SUBIR': '',
        'DESCER': 'b1',
        'AVANÇAR': '',
        'RETORNAR': 'a1',
        'MONSTRO': '',
        'LOCAIS': 'enfrentar',
        'contador' : 0
    },
    'b1': { 
        'NOME_LOCAL': "O Salão das Vozes Vazias",
        'DESCRICAO': '''
Ao entrar, o som desaparece. Nenhum eco. Nenhuma respiração. No lugar, apenas sussurros em sua mente — 
vozes que carregam seu nome, mas ditas por pessoas que você não lembra.
''',
        'EXAMINAR': '''
As paredes são cobertas por máscaras penduradas, cada uma com uma representação diferente sendo elas raiva, medo, alegria, loucura.
Quando você se aproxima, elas viram lentamente... te observando. '
(Digite raiva, medo, alegria ou loucura para ir até a máscara correspondente.)
''',
        'SOLVED': False,
        'SUBIR': 'a2',
        'DESCER': '',
        'AVANÇAR': 'b2',
        'RETORNAR': '',
        'MONSTRO': '',
        'LOCAIS': ['raiva', 'medo', 'alegria', 'loucura'],
        'contador' : 0
    },
    'b2': {
        'NOME_LOCAL': "O Poço das Memórias Afundadas",
        'DESCRICAO': '''
Um poço escuro sussurra memórias esquecidas. Símbolos antigos cobrem as paredes úmidas, e o ar é carregado de nostalgia.
''',
        'EXAMINAR': '''
                No centro de um salão de pedra úmida, há um poço negro como breu. 
Correntes quebradas o rodeiam, e marcas de garras riscam o chão como se algo tivesse sido arrastado para fora.
              Ao se aproximar, imagens distorcidas começam a surgir na água parada
                são lembranças suas, mas... distorcidas, erradas, talvez falsas.
                      No fundo do poço você vê uma arma, deseja pegar? 
                  (Para pegar digite 'pegar', para ignorar digite 'sair')
                ''',
        'SOLVED': True,
        'SUBIR': '',
        'DESCER': 'c1',
        'AVANÇAR': '',
        'RETORNAR': 'b1',
        'MONSTRO': '',
        'LOCAIS': 'pegar',
        'contador' : 0,
        'contador2' : 0
    },
    'c1': {
        'NOME_LOCAL': "Sala1 Terceiro andar",
        'DESCRICAO': 'Descrição da sala c1.',
        'EXAMINAR': 'Velhas tapeçarias nas paredes.',
        'SOLVED': False,
        'SUBIR': 'b2',
        'DESCER': '',
        'AVANÇAR': 'c2',
        'RETORNAR': '',
        'MONSTRO': '',
        'LOCAIS': '',
        'contador' : 0
    },
    'c2': {
        'NOME_LOCAL': "Sala2 Terceiro andar",
        'DESCRICAO': 'Descrição da sala c2.',
        'EXAMINAR': 'Eco assustador.',
        'SOLVED': False,
        'SUBIR': '',
        'DESCER': '',
        'AVANÇAR': '',
        'RETORNAR': 'c1',
        'MONSTRO': '',
        'LOCAIS': '',
        'contador' : 0
    },
}

def mostrar_mapa():
    if meu_jogador.local == 'a1':
        limpar_tela()
        print('▬'*100)
        print('Mapa:')
        print('''
                |x| |
                | | |
                | | |
    ''')
    elif meu_jogador.local == 'a2':
        limpar_tela()
        print('Mapa:')
        print('''
                | |x|
                | | |
                | | |
    ''')
    elif meu_jogador.local == 'b1':
        limpar_tela()
        print('Mapa:')
        print('''
                | | |
                |x| |
                | | |
    ''')
    elif meu_jogador.local == 'b2':
        limpar_tela()
        print('Mapa:')
        print('''
                | | |
                | |x|
                | | |
    ''')
    elif meu_jogador.local == 'c1':
        limpar_tela()
        print('Mapa:')
        print('''
                | | |
                | | |
                |x| |
    ''')
    elif meu_jogador.local == 'c2':
        limpar_tela()
        print('Mapa:')
        print('''
                | | |
                | | |
                | |x|
    ''')

##### Interações em jogo #####
def print_local():
    if meu_jogador.local != 'a1':
        limpar_tela()
    local_nome = mapa[meu_jogador.local]['NOME_LOCAL']
    local_desc = mapa[meu_jogador.local]['DESCRICAO']
    print('\n' + '▄'*100 + Fore.YELLOW + f''' 
                       
                                    {local_nome.upper()}
            {local_desc}
''' + Style.RESET_ALL + '\n')   
    print('▄' * 100)

    mostrar_status(meu_jogador)
    if mapa[meu_jogador.local]['MONSTRO'] != '':
        print(f"há um" + Fore.RED + f" {mapa[meu_jogador.local]['MONSTRO'].nome}" + Style.RESET_ALL + " na sala. O que deseja fazer?" + Fore.YELLOW + "\n[lutar / fugir / falar]")
        escolha = input(Fore.YELLOW + ">>"+Style.RESET_ALL).lower()
        if escolha not in ['lutar', 'fugir', 'falar']:
            print_local()
        acao_luta(escolha, mapa[meu_jogador.local]['MONSTRO'])
    main_game_loop()

def prompt():
    print("\n" + "▬"*100)
    print(Fore.LIGHTYELLOW_EX + "O que deseja fazer?"+Style.RESET_ALL)
    acao = input(Fore.LIGHTYELLOW_EX +">>"+Style.RESET_ALL).lower()
    acoes_aceitas = ['invocar','status', 'mover', 'loja', 'sair', 'ajuda', 'olhar', 'inspecionar', 'teleportar', 'dormir', 'mochila', 'mapa']
    while acao not in acoes_aceitas:
        print(Fore.RED + "Ação inválida, tente novamente.\n")
        acao = input(Fore.YELLOW +">> "+Style.RESET_ALL).lower()
    if acao == 'sair':
        sair()
    if acao in ['mover', 'teleportar']:
        jogador_mover()
    elif acao == 'ajuda':
        ajuda_menu()
    elif acao in ['olhar', 'inspecionar']:
        jogador_examinar()
    elif acao == 'dormir':
        jogador_dormir()
    elif acao == 'mochila' and acao != 'sair':
        abrir_mochila()
    elif acao == 'loja':
        mostrar_loja()
        acao_loja(input(Fore.LIGHTYELLOW_EX +'>>'+Style.RESET_ALL).lower())
    elif acao == 'status':
        exibir_status(meu_jogador)
    elif acao == 'mapa':
        mostrar_mapa()
    elif acao == 'invocar':
        encontro_aleatorio()

def locais():
    print(Fore.LIGHTYELLOW_EX + 'O que deseja fazer?' + Style.RESET_ALL)
    acao = input(Fore.LIGHTYELLOW_EX +'>>'+Style.RESET_ALL).lower()
    acoes_aceitas = mapa[meu_jogador.local]['LOCAIS'],'raiva','medo','alegria','loucura', 'sair', 'pegar',
    
    while acao not in acoes_aceitas:
        print(Fore.RED + 'Acao inválida, tente novamente. (caso não tenha mais opções, digite sair)'+Style.RESET_ALL)
        acao = input(Fore.LIGHTYELLOW_EX +'>>'+Style.RESET_ALL).lower()
    
    if acao == 'sair':
        main_game_loop()
        print_local()
    if acao == 'trono':
        trono()
    elif acao == 'bau':
        # Adicione aqui a função para o baú quando existir
        pass
    elif acao == 'enfrentar':
        boss_enraizado()
    elif acao == 'raiva':
        raiva()
    elif acao == 'medo':
        medo()
    elif acao == 'alegria':
        alegria()
    elif acao == 'loucura':
        loucura()
    elif acao == 'pegar':
        pegar()
    else:
        print('Acao inválida, tente novamente.')
        locais()

def acao_loja(escolha):
    if escolha == 'comprar':
        comprar()
    elif escolha == 'vender':
        vender()

### Objetos interativos dos andares ###
def trono():
    print('▬'*100)
    if meu_jogador.local == 'a1' and mapa[meu_jogador.local]['SOLVED'] == False:
        fala1 ='Você vai até o brilho e vê um anel dourado.\nao toca-lo um frio intenso percorre seu braço.\nSeu dedo o aceita sem resistência, como se ele sentisse que voce era o seu Dono.\n'
        for fala in fala1:
            sys.stdout.write(fala)
            sys.stdout.flush()
            time.sleep(0.01)
        item = lista_itens_especiais[0]
        meu_jogador.add_item(Item(item['nome'], item['atk'], item['desc'], item['equipado'], item['consumivel'], item['preco'], item['especial']))
        fala2 = Fore.YELLOW + 'Anel desconhecido adicionado ao seu inventario!' + Style.RESET_ALL
        for fala in fala2:
            sys.stdout.write(fala)
            sys.stdout.flush()
            time.sleep(0.01)
        print('\n', '▬'*100)
        mapa[meu_jogador.local]['SOLVED'] = True
        time.sleep(1.5)
        limpar_tela()
        main_game_loop()
    elif meu_jogador.local == 'a1' and mapa[meu_jogador.local]['SOLVED'] == True:
        fala3 = 'Nã há mais nada no trono.'
        for fala in fala3:
            sys.stdout.write(fala)
            sys.stdout.flush()
            time.sleep(0.01)
        print('\n', '▬'*100)
        time.sleep(1.5)
        limpar_tela()
        main_game_loop()
    else:
        print(Fore.RED + 'Comando inválido.'+Style.RESET_ALL)
        main_game_loop()

def boss_enraizado():
    if meu_jogador.local == 'a2':
        if mapa[meu_jogador.local]['SOLVED'] == False:
            lutar = 'Quando você se aproxima…'+Fore.RED+' ela desperta.'+Style.RESET_ALL
            for fala in lutar:
                sys.stdout.write(fala)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1)
            limpar_tela()
            luta(guardiao_enraizado, meu_jogador)        
    elif meu_jogador.local == 'a2' and mapa[meu_jogador.local]['SOLVED'] == True:
        fala1 = Fore.LIGHTYELLOW_EX+'O monstro está caido morto bem a sua frente.'+Style.RESET_ALL
        for fala in fala1:
            sys.stdout.write(fala)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1.5)
        limpar_tela()
        main_game_loop()
    else:
        print(Fore.RED+'Comando inválido.'+Style.RESET_ALL)
        main_game_loop()

def pegar():
    item = lista_armas_especiais[0]
    item2 = lista_armas_especiais[1]
    item3 = lista_armas_especiais[2]
    if meu_jogador.local == 'b2' and mapa['b2']['contador2'] == 0:
        if meu_jogador.classe == 'monge':
            meu_jogador.add_item(Item(item['nome'], item['atk'], item['desc'], item['equipado'], item['consumivel'], item['preco'], item['especial']))
            mapa['b2']['contador2'] += 1
            fala_monge = Fore.YELLOW+'Você se lembra da arma que usava antes, colocando a mão dentro do poço você a pega e agora ela está na sua mao.\n'+Style.RESET_ALL
            for fala in fala_monge:
                sys.stdout.write(fala)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1.5)
            limpar_tela()
            main_game_loop()
        elif meu_jogador.classe == 'guerreiro':
            meu_jogador.add_item(Item(item2['nome'], item2['atk'], item2['desc'], item2['equipado'], item2['consumivel'], item2['preco'], item2['especial']))
            mapa['b2']['contador2'] += 1
            fala_guerreiro = Fore.YELLOW+' Vocé se lembra da arma que usava antes, colocando a mão dentro do poço vocé a pega e agora ela está na sua mao.\n'+Style.RESET_ALL
            for fala in fala_guerreiro:
                sys.stdout.write(fala)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1.5)
            limpar_tela()
            print_local()
            main_game_loop()
        elif meu_jogador.classe == 'mago':
            meu_jogador.add_item(Item(item3['nome'], item3['atk'], item3['desc'], item3['equipado'], item3['consumivel'], item3['preco'], item3['especial']))
            mapa['b2']['contador2'] += 1
            fala_mago = Fore.YELLOW+' Vocé se lembra da arma que usava antes, colocando a mão dentro do poço vocé a pega e agora ela está na sua mao.\n'+Style.RESET_ALL
            for fala in fala_mago:
                sys.stdout.write(fala)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1.5)
            limpar_tela()
            print_local()
            main_game_loop()
    else:
        print(Fore.RED+'Comando inválido.'+Style.RESET_ALL)
        locais()


########################################
def comprar(escolha):
        lista_itens_loja[escolha]['comprado'] = True
        item = lista_itens_loja[escolha]
        item_add = Item(item['nome'], item['atk'], item['desc'], item['equipado'], item['consumivel'], item['preco'], item['especial'])
        print(Fore.GREEN +'**VOCE COMPROU'+Style.RESET_ALL+f' {item_add.nome}**')
        meu_jogador.add_item(item_add)
        meu_jogador.ouro -= lista_itens_loja[escolha]['preco']
        mostrar_loja()
    
def vender(self):
    self.vendido = True

def sair():
    print(Fore.LIGHTRED_EX+"Tem certeza que deseja sair? [s/n] "+Style.RESET_ALL)
    confirmar = input(Fore.LIGHTYELLOW_EX +'>>'+Style.RESET_ALL).lower()
    if confirmar not in ['s', 'n']:
        print(Fore.RED+'\ncomando inválido'+Style.RESET_ALL)
        sair()
    if confirmar == 's':
        meu_jogador.game_over = True
        main_game_loop()
    else:
        if meu_jogador.nome == '':
            tela_titulo()
        main_game_loop()

def acao_luta(escolha, monstro):
    if escolha == 'lutar':
        luta(monstro, meu_jogador)
    elif escolha == 'fugir':
        fugir()
    elif escolha == 'falar':
        loading()
        print(Fore.RED + f'O {monstro.nome} não te entende e te ataca'+Style.RESET_ALL)
        intervalo()
        meu_jogador.vida -= monstro.atk
        luta(monstro, meu_jogador)

def abrir_mochila():
    if meu_jogador.game_over:
        main_game_loop()
    if meu_jogador.mochila:
        print ('G:' + Fore.YELLOW + f' {meu_jogador.ouro}'+Style.RESET_ALL)
        for i in range(len(meu_jogador.mochila)):
            if meu_jogador.mochila[i].consumivel:
                print(Fore.YELLOW + f'[{i+1}]' + Style.RESET_ALL + f' {meu_jogador.mochila[i].nome} desc: {meu_jogador.mochila[i].desc}')
                continue
            if meu_jogador.mochila[i].equipado == True:
                print(Fore.YELLOW + f'[{i+1}]' + Style.RESET_ALL + f' {meu_jogador.mochila[i].nome} ATK: {meu_jogador.mochila[i].atk} desc: {meu_jogador.mochila[i].desc} (EQUIPADO)')
                continue
            print(Fore.YELLOW + f'[{i+1}]' + Style.RESET_ALL + f' {meu_jogador.mochila[i].nome} ATK: {meu_jogador.mochila[i].atk} desc: {meu_jogador.mochila[i].desc}')
        print('>> Use números para selecionar os itens ou [fechar]')
        escolha = input(Fore.LIGHTYELLOW_EX + ">>"+Style.RESET_ALL)
        if escolha == 'fechar':
            print_local()
        try:
            escolha = int(escolha)-1
            if escolha not in range(0, len(meu_jogador.mochila)):
                abrir_mochila()
            if meu_jogador.mochila[escolha].consumivel or meu_jogador.mochila[escolha].especial:
                print(f'item: {meu_jogador.mochila[escolha].nome} | desc: {meu_jogador.mochila[escolha].desc}')
            else:    
                print(f'item: {meu_jogador.mochila[escolha].nome} | ATK: {meu_jogador.mochila[escolha].atk} | desc: {meu_jogador.mochila[escolha].desc}')
            # jogador selecionou com item equipao
            if meu_jogador.item_equipado:
                # jogador selecionou item equipado
                if meu_jogador.mochila[escolha].equipado == True:
                    print('[desequipar / remover / voltar / '+ Fore.RED + 'fechar]'+Style.RESET_ALL)
                    acao = input(Fore.LIGHTYELLOW_EX +'>>'+Style.RESET_ALL).lower()
                    if acao not in ['desequipar', 'remover', 'voltar', 'fechar']:
                        print('\ncomando inválido')
                        abrir_mochila()
                    
                    if acao == 'desequipar':
                        print(Fore.RED + '**VOCÊ DESEQUIPOU ' + Style.RESET_ALL + f' {meu_jogador.item_equipado.nome}**')
                        meu_jogador.item_equipado = False
                        meu_jogador.mochila[escolha].equipado = False
                        meu_jogador.atk_final = meu_jogador.atk
                        abrir_mochila()
                    elif acao == 'remover':
                        print(Fore.RED + f'**VOCÊ DESEQUIPOU '+ Style.RESET_ALL + f'{meu_jogador.item_equipado.nome}**')
                        print(Fore.RED + f'**VOCÊ DROPOU '+ Style.RESET_ALL + f'{meu_jogador.item_equipado.nome}**')
                        meu_jogador.item_equipado = None
                        meu_jogador.mochila.pop(escolha)
                        meu_jogador.atk_final = meu_jogador.atk
                        abrir_mochila()
                    elif acao == 'voltar':
                        abrir_mochila()
                    elif acao == 'fechar':
                        print_local()
                # jogador selecionou item NÂO equipado
                else:
                    if meu_jogador.mochila[escolha].especial:
                        print('[voltar / '+ Fore.RED +'fechar]'+Style.RESET_ALL)
                        acao = input(Fore.LIGHTYELLOW_EX +'>>'+Style.RESET_ALL).lower()
                        if acao not in ['voltar' ,'fechar']:
                            abrir_mochila()
                        elif acao == 'voltar':
                            abrir_mochila()
                        elif acao == 'fechar':
                            print_local()
                        
                    if meu_jogador.mochila[escolha].consumivel:
                        print('[usar / remover / voltar / '+ Fore.RED + 'fechar]'+Style.RESET_ALL)
                        acao = input(Fore.LIGHTYELLOW_EX +'>>'+Style.RESET_ALL).lower()
                        if acao not in ['usar', 'remover', 'voltar', 'fechar']:
                            print(Fore.RED + '\ncomando inválido'+Style.RESET_ALL)
                            abrir_mochila()
                        if acao == 'usar':
                            if meu_jogador.mochila[escolha].nome == 'Pocao de vida baixa':
                                pocao_vida()
                            elif meu_jogador.mochila[escolha].nome == 'Pocao de vida media':
                                pocao_vida_media()
                            elif meu_jogador.mochila[escolha].nome == 'Pocao de vida alta':
                                pocao_vida_media()
                            elif meu_jogador.mochila[escolha].nome == 'Pocao de mana baixa':
                                pocao_mana()
                            elif meu_jogador.mochila[escolha].nome == 'Pocao de mana media':
                                pocao_mana_media()
                            elif meu_jogador.mochila[escolha].nome == 'Pocao de mana alta':
                                pocao_mana_alta()
                            meu_jogador.mochila.pop(escolha)
                            abrir_mochila()
                            
                    print('[equipar / remover / voltar / '+ Fore.RED +'fechar]'+Style.RESET_ALL)
                    
                    acao = input(Fore.LIGHTYELLOW_EX +'>>'+Style.RESET_ALL).lower()
                    if acao not in ['equipar', 'remover', 'fechar']:
                        print(Fore.RED + '\ncomando inválido'+Style.RESET_ALL)
                        abrir_mochila()

                    if acao == 'equipar':
                        print(Fore.RED + '**VOCÊ DESEQUIPOU '+ Style.RESET_ALL +f'{meu_jogador.item_equipado.nome}**')
                        for i in range(len(meu_jogador.mochila)):
                            if meu_jogador.mochila[i].equipado == True:
                                meu_jogador.mochila[i].equipado = False
                                break
                        meu_jogador.item_equipado = meu_jogador.mochila[escolha]
                        meu_jogador.mochila[escolha].equipado = True
                        meu_jogador.atk_final = meu_jogador.atk + meu_jogador.item_equipado.atk
                        print(Fore.GREEN +f'**VOCÊ EQUIPOU '+Style.RESET_ALL +f'{meu_jogador.item_equipado.nome}**')
                        abrir_mochila()
                    elif acao == 'remover':
                        print(Fore.RED + '**VOCÊ DROPOU '+Style.RESET_ALL +f'{meu_jogador.mochila[escolha].nome}')
                        meu_jogador.mochila.pop(escolha)
                        abrir_mochila()
                    elif acao == 'voltar':
                        abrir_mochila()
                    elif acao == 'fechar':
                        print_local()
                        main_game_loop()
            # jogador selecionou sem item equipado
            else:
                if meu_jogador.mochila[escolha].especial:
                    print('[voltar / '+Fore.RED +'fechar]'+Style.RESET_ALL)
                    acao = input(Fore.LIGHTYELLOW_EX +'>>'+Style.RESET_ALL).lower()
                    if acao not in ['voltar' ,'fechar']:
                        abrir_mochila()
                    elif acao == 'voltar':
                        abrir_mochila()
                    elif acao == 'fechar':
                        print_local()
                if meu_jogador.mochila[escolha].consumivel:
                        print( '[usar / remover / voltar / '+Fore.RED +'fechar]'+Style.RESET_ALL)
                        acao = input(Fore.LIGHTYELLOW_EX +'>>'+Style.RESET_ALL).lower()
                        if acao not in ['usar', 'remover', 'voltar', 'fechar']:
                            print('\ncomando inválido')
                            abrir_mochila()
                        if acao == 'usar':
                            if meu_jogador.mochila[escolha].nome == 'Pocao de vida baixa':
                                pocao_vida()
                                meu_jogador.mochila.pop(escolha)
                                abrir_mochila()
                            elif meu_jogador.mochila[escolha].nome == 'Pocao de vida media':
                                pocao_vida_media()
                                meu_jogador.mochila.pop(escolha)
                                abrir_mochila()
                            elif meu_jogador.mochila[escolha].nome == 'Pocao de vida alta':
                                pocao_vida_alta()
                                meu_jogador.mochila.pop(escolha)
                                abrir_mochila()
                            elif meu_jogador.mochila[escolha].nome == 'Pocao de mana baixa':
                                pocao_mana()
                                meu_jogador.mochila.pop(escolha)
                                abrir_mochila()
                            elif meu_jogador.mochila[escolha].nome == 'Pocao de mana media':
                                pocao_mana_media()
                                meu_jogador.mochila.pop(escolha)
                                abrir_mochila()
                            elif meu_jogador.mochila[escolha].nome == 'Pocao de mana alta':
                                pocao_mana_alta()
                                meu_jogador.mochila.pop(escolha)
                                abrir_mochila()
                        elif acao == 'remover':
                            print(Fore.RED +f'**VOCÊ DROPOU '+Style.RESET_ALL +f'{meu_jogador.mochila[escolha].nome}')
                            meu_jogador.mochila.pop(escolha)
                            abrir_mochila()
                        elif acao == 'voltar':
                            abrir_mochila()
                        elif acao == 'fechar':
                            print_local()
                print('[equipar / remover / '+Fore.RED +'fechar]'+Style.RESET_ALL)
                acao = input(Fore.LIGHTYELLOW_EX +'>>'+Style.RESET_ALL).lower()
                if acao not in ['equipar', 'remover', 'fechar']:
                    print('\ncomando inválido')
                    abrir_mochila()
                
                if acao == 'equipar':
                    meu_jogador.mochila[escolha].equipado = True
                    meu_jogador.item_equipado = meu_jogador.mochila[escolha]
                    meu_jogador.atk_final = meu_jogador.item_equipado.atk + meu_jogador.atk
                    print(Fore.GREEN + '**VOCÊ EQUIPOU '+Style.RESET_ALL +f'{meu_jogador.item_equipado.nome}**')
                    abrir_mochila()
                elif acao == 'remover':
                    print(Fore.RED+f'**VOCÊ DROPOU '+Style.RESET_ALL+f'{meu_jogador.mochila[escolha].nome}')
                    meu_jogador.mochila.pop(escolha)
                    abrir_mochila()
                elif acao == 'voltar':
                    abrir_mochila()
                elif acao == 'fechar':
                    print_local()
        except:
            abrir_mochila()
    else:
        print(Fore.RED +"Mochila vazia"+Style.RESET_ALL)

def luta(monstro, meu_jogador):
    print('▀'*100)
    efeitos = ''
    for efeito in monstro.efeitos_status:
        efeitos += ("" + efeito.nome + " ")
    print(f'\n{monstro.nome} #{monstro.nivel} efeitos: {efeitos}')
    print(f'vida: {monstro.vida}/{monstro.vida_max} ATK: {monstro.atk}')
    print('▀'*100)
    if meu_jogador.efeitos_status:
        aplicar_efeito(meu_jogador)
    mostrar_status(meu_jogador)
    print('atacar / magia / mochila / fugir')
    acao = input(">>").lower()
    if acao not in ['atacar', 'magia', 'mochila', 'fugir']:
        limpar_tela()
        print("comando invádido".upper())
        luta(monstro, meu_jogador)
    if acao == 'atacar':
        monstro.vida -= meu_jogador.atk_final
        print(f"você ataca {monstro.nome}\n")
        loading()
        intervalo()
        
        if monstro.vida > 0:
            monstro.atk_turnos += 1
            if monstro.efeitos_status:
                aplicar_efeito(monstro)
            if monstro.pular_turno:
                luta(monstro, meu_jogador)
            if monstro.atk_turnos >= 3:
                meu_jogador.vida -= monstro.atk*2
                print(f'O {monstro.nome} te ataca ferozmente')
                monstro.atk_turnos = 0
                if monstro.atk_efeito:
                    meu_jogador.add_efeito(monstro.atk_efeito)
                meu_jogador.add_efeito(monstro.atk_efeito)
                luta(monstro, meu_jogador)
            meu_jogador.vida -= monstro.atk
            print(f'\no {monstro.nome} te ataca\n')
            loading()
        intervalo()
        
    elif acao == 'magia':
        if meu_jogador.magias:
            for i in range(len(meu_jogador.magias)):
                magia = meu_jogador.magias[i]
                print(f'{i+1}. {magia.nome} | DANO: {magia.dano} + DANO ADICIONAL: {meu_jogador.dano_magico} | custo de mana: {magia.mana_gasta} | desc: {magia.desc}')
            print("Use números para escolher as magias")
            escolha = input(">>")
            try:
                escolha = int(escolha)-1
                if escolha not in range(0, len(meu_jogador.magias)):
                    print('Magia inválida')
                    luta(monstro, meu_jogador)

                if meu_jogador.mana < meu_jogador.magias[escolha].mana_gasta:
                    print('**MANA INSUFICIENTE**')
                    luta(monstro, meu_jogador)

                monstro.vida -= (meu_jogador.magias[escolha].dano + meu_jogador.dano_magico)
                meu_jogador.mana -= meu_jogador.magias[escolha].mana_gasta
                monstro.add_efeito(meu_jogador.magias[escolha].efeito)
                print(f'Você lança {meu_jogador.magias[escolha].nome} em {monstro.nome}')
                loading()
                intervalo()

                if monstro.vida > 0:
                    
                    monstro.atk_turnos += 1
                    if monstro.efeitos_status:
                        aplicar_efeito(monstro)
                    if monstro.pular_turno:
                        luta(monstro, meu_jogador)
                    if monstro.atk_turnos >= 3:
                        meu_jogador.vida -= monstro.atk*2
                        print(f'O {monstro.nome} te ataca ferozmente')
                        monstro.atk_turnos = 0
                        if monstro.atk_efeito:
                            meu_jogador.add_efeito(monstro.atk_efeito)
                        luta(monstro, meu_jogador)

                    meu_jogador.vida -= monstro.atk
                    print(f'\no {monstro.nome} te ataca\n')
                    loading()
                intervalo()
            except:
                print('\nComando inválido')
                luta(monstro, meu_jogador)
        else:
            print('Você ainda não sabe magias')
            loading()
            meu_jogador.vida -= monstro.atk
            print(f'o {monstro.nome} te ataca')
            intervalo()
    elif acao == 'mochila':
        consumiveis = []
        for consumivel in meu_jogador.mochila:
            if consumivel.consumivel:
                consumiveis.append(consumivel)
        if not consumivel:
            print('Nenhum item para ser usado')
            luta(monstro, meu_jogador)
        for i, consumivel in enumerate(consumiveis):
            print(f'{i+1}. {consumivel.nome} | {consumivel.desc}')
        print('Use os números para selecionar os itens')
        escolha = input('>>').lower()
        try:
            escolha = int(escolha)-1
            if escolha not in range(0, len(consumiveis)):
                print('\nComando inválido')
                luta(monstro, meu_jogador)
            print(f'{consumiveis[escolha].nome} | {consumiveis[escolha].desc}')
            print('[usar | voltar]')
            acao = input('>>').lower()
            if acao not in ['usar', 'voltar']:
                print('\nComando inválido')
                luta(monstro, meu_jogador)
            if acao == 'usar':
                if meu_jogador.mochila[escolha].nome == 'Pocao de vida baixa':
                    pocao_vida()
                elif meu_jogador.mochila[escolha].nome == 'Pocao de vida media':
                    pocao_vida_media()
                elif meu_jogador.mochila[escolha].nome == 'Pocao de vida alta':
                    pocao_vida_alta()
                elif meu_jogador.mochila[escolha].nome == 'Pocao de mana baixa':
                    pocao_mana()
                elif meu_jogador.mochila[escolha].nome == 'Pocao de mana media':
                    pocao_mana_media()
                elif meu_jogador.mochila[escolha].nome == 'Pocao de mana alta':
                    pocao_mana_alta()
                for i, item in enumerate(meu_jogador.mochila):
                    if item.nome == consumiveis[escolha].nome:
                        meu_jogador.mochila.pop(i)
                luta(monstro, meu_jogador)
            elif acao == 'voltar':
                luta(monstro, meu_jogador)
        except:
            print('\nComando inválido')
            luta(monstro, meu_jogador)
    
    elif acao == 'fugir':
        fugir()
    
    # fim do turno
    if meu_jogador.vida > 0 and monstro.vida > 0:
        luta(monstro, meu_jogador)
        
    # jogador morre
    if meu_jogador.vida <= 0:
        meu_jogador.local = 'a1'
        meu_jogador.vida = meu_jogador.vida_max
        limpar_tela()
        print('Você morreu e acorda na sala inicial')

    # monstro morre
    elif monstro.vida <= 0:
        limpar_tela()
        print(f'VOCÊ DERROTOU {monstro.nome}')
        experiencia(monstro)
        time.sleep(1)
        if monstro.boss == True:
            mapa[meu_jogador.local]['SOLVED'] = True
        drop(monstro)  # Sem verificação de chance, sempre chama o drop
        print_local()
        main_game_loop()

def aplicar_efeito(alvo):
    for i, efeito in enumerate(alvo.efeitos_status):
        if efeito.tipo == 'dano':
            alvo.vida -= efeito.dano
            print(f'{alvo.nome} sofreu {efeito.nome} e sofreu {efeito.dano} de dano')
            alvo.efeitos_status[i].tempo -= 1
            if alvo.efeitos_status[i].tempo == 0:
                alvo.efeitos_status.pop(i)
        elif efeito.tipo == 'pular':
            alvo.pular_turno = True
            if random.random() < 0.5:
                alvo.pular_turno = False
                alvo.efeitos_status.pop(i)
                continue
            print(f'{alvo.nome} está conglado e não pode atacar')
def drop(monstro):
    print(f'Você ganhou {monstro.ouro} de ouro!')
    meu_jogador.ouro += monstro.ouro
    
    itens_que_droparam = []
    
    # Verifica cada item para ver se dropou
    for drop in monstro.drops:
        if random.random() <= drop['chance']:  # Gera um número entre 0 e 1
            itens_que_droparam.append(drop['item'])
    
    if not itens_que_droparam:
        print(f"\nO {monstro.nome} não dropou nenhum item.")
        mapa[meu_jogador.local]['MONSTRO'] = ''
        print_local()
        main_game_loop()
    
    # Mostra os itens que droparam
    print(f"\nO {monstro.nome} dropou os seguintes itens:")
    for item in itens_que_droparam:
        print(f"- {item.nome}")
    
    print('\n[pegar / ignorar]')
    acao = input('>>').lower()
    
    if acao not in ['pegar', 'ignorar']:
        print('\nComando inválido!')
        return drop(monstro)
    
    if acao == 'pegar':
        mapa[meu_jogador.local]['MONSTRO'] = ''
        for item in itens_que_droparam:
            meu_jogador.add_item(item)
        print("\nVocê pegou todos os itens!")
    elif acao == 'ignorar':
        mapa[meu_jogador.local]['MONSTRO'] = ''
        print('\nVocê ignorou os itens.')
    
    print_local()
    main_game_loop()
    
def fugir():
    if meu_jogador.local == 'a2':
        meu_jogador.local = 'a1'
    elif meu_jogador.local == 'b1':
        meu_jogador.local = 'a2'
    elif meu_jogador.local == 'b2':
        meu_jogador.local = 'b1'
    elif meu_jogador.local == 'c1':
        meu_jogador.local = 'b2'
    elif meu_jogador.local == 'c2':
        meu_jogador.local = 'c1'
    print('você voltou para a sala anterior')
    main_game_loop()

def mostrar_status(self):
    print('▬'*100)
    print(f'{self.nome} LVL:{self.nivel} XP: {self.xp}/{self.xp_max}')
    print(f'vida: {self.vida}/{self.vida_max} ATK: {self.atk} MANA: {self.mana}/{self.mana_max}\nefeitos:', end=' ')
    for efeito in self.efeitos_status:
        print(f'{efeito.nome}', end=' ')
    if self.item_equipado:
        print(f'\narma: {self.item_equipado.nome} ATK: {self.item_equipado.atk}')
    else:
        print('\narma: sem arma equipada')

def jogador_dormir():
    if meu_jogador.local in ['a1', 'c1']:
        if meu_jogador.vida == meu_jogador.vida_max:
            print("Dormindo... mas não recupegou vida (hp cheio)")
        elif meu_jogador.vida < meu_jogador.vida_max:
            print("dormindo... Você recuperou vida!!")
            meu_jogador.vida += 5
            if meu_jogador.vida > meu_jogador.vida_max:
                meu_jogador.vida = meu_jogador.vida_max
    else:
        print('Você não pode dormir aqui.')
    
def jogador_mover():
    if mapa[meu_jogador.local]['SOLVED'] == False:
        if meu_jogador.local == 'a1' and not mapa[meu_jogador.local]['SOLVED']:
            fala = 'Você não consegue passar pela porta, alguma energia estranha te impede'
            for falas in fala:
                sys.stdout.write(falas)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1)
            main_game_loop()
        elif meu_jogador.local == 'a2' and not mapa[meu_jogador.local]['SOLVED']:
            fala1 = 'Algumas raizes impedem a passagem, aparentemente vem do Enraizado.'
            for falas in fala1:
                sys.stdout.write(falas)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1)
            main_game_loop()
        if meu_jogador.local == 'b1' and not mapa[meu_jogador.local]['SOLVED']:
            fala2 = 'A força das máscaras por algum motivo impedem de abrir a porta.'
            for falas in fala2:
                sys.stdout.write(falas)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1)
            main_game_loop()
    elif meu_jogador.local == 'a1':
        pergunta = "Avançar em direção ao portão negro? (escreva avançar)\n >>"
    elif meu_jogador.local == 'a2':
        pergunta = '''
O proximo portão se ilumina revelando ser uma escada que leva para os andares inferiores A torre está viva, Observando, Esperando.
E você sente que o verdadeiro inferno... não ficou para trás.
Você deseja descer a escada ou retornar a sala anterior? (escreva: descer ou retornar)\n>>'''
    elif meu_jogador.local in 'b1':
        pergunta = '''
A sua frente está uma porta de madeira, atrás de você está a escada para voltar para a sala anterior.
Deseja abrir a porta e avançar para a próxima sala ou subir a escada? (escreva: avançar ou subir)\n>>'''
    elif meu_jogador.local in 'b2':
        pergunta = '''
A sua frente está uma escada feita de peças mecânicas, ela leva para o próximo andar, atrás de vocé, uma porta de madeira para retornar a sala anterior.
Descer a escada ou retornar a sala anterior? (escreva: descer ou retornar)\n>>'''
    elif meu_jogador.local in 'c1':
        pergunta = "Avançar ou subir a sala anterior? (escreva: avançar ou subir)\n>>"
    elif meu_jogador.local in 'c2':
        pergunta = "Descer as escadas ou retornar a sala anterior? (escreva: descer ou retornar)\n>>"
    
    dest = input(pergunta).lower()
    direcoes_validas = ['subir', 'descer', 'avançar', 'retornar', 'loja']
    if dest in direcoes_validas:
        if dest == 'loja':
            mostrar_loja()
        destino = mapa[meu_jogador.local][dest.upper()]
        if destino:
            movimento_manipulado(destino)
        else:
            print("Você não pode se mover nessa direção.")
    else:
        print("Direção inválida.")

def movimento_manipulado(destino):
    if destino == 'a2':
        meu_jogador.local = destino
        if mapa['a1']['contador'] == 0:  
            mapa['a1']['contador'] += 1  
            passagem = '''
Ao Abrir o portão, Uma nuvem de poeira antiga Cobre o Local. Uma voz, baixa e arrastada, sussurra em sua mente:
"O herdeiro da ruína caminha outra vez... mas será que lembrará antes de se perder?"

.....
Ao Atravessar Para o Proximo comodo, 
a cada passo a dentro o ambiente é iluminado por tochas azuis que você sente que não deviam acender.
'''
            for passagens in passagem:
                sys.stdout.write(passagens)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(2)
        print_local()

    elif destino == 'b1':
        meu_jogador.local = destino 
        if mapa['a2']['contador'] == 0:
            mapa['a2']['contador'] += 1
            passagem2 = '''
Ao entrar, o som desaparece. Nenhum eco. Nenhuma respiração. No lugar, apenas sussurros em sua mente — 
vozes que carregam seu nome, mas ditas por pessoas que você não lembra.
As paredes são cobertas por máscaras penduradas, cada uma diferente — raiva, medo, alegria, loucura.
Quando você se aproxima, uma delas vira lentamente... te observando.'''
            for passagens in passagem2:
                sys.stdout.write(passagens)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(2)
            print_local()
    meu_jogador.local = destino
    print(f"\nVocê se moveu para {destino}.")
    print_local()


def jogador_examinar():
    examinar = mapa[meu_jogador.local]['EXAMINAR']
    if mapa[meu_jogador.local][SOLVED] == True and meu_jogador.local == 'a2':
        examinar2 = '''
Atrás de você, o que restou do trono escurece ainda mais, como se a própria sombra tentasse fugir dali. 
A energia maligna está morrendo... mas algo abaixo desperta.

Você se vira, encarando a única saída: um Portão Negro, que leva a uma proxima sala nas profundezas da torre. 
A estrutura range como um animal faminto, esperando que você se mova.
              '''
        for examina in examinar2:
            sys.stdout.write(examina)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(2)

    elif meu_jogador.local == 'b1' and mapa[meu_jogador.local]['SOLVED'] == True:
        examinar3 = '''
As máscaras param de se mover e o som das vozes desaparece, o poder delas se apagou.
'''
        for examina in examinar3:
            sys.stdout.write(examina)
            sys.stdout.flush()
            time.sleep(0.01)

    elif meu_jogador.local == 'b2' and mapa['b2']['contador2'] == 1:
        examinar4 = '''
Você já pegou o item de dentro do poço.

'''
        for examina in examinar4:
            sys.stdout.write(examina)
            sys.stdout.flush()
            time.sleep(0.01)
    else:
        print('▬'*100)
        for examina in examinar:
            sys.stdout.write(examina)
            sys.stdout.flush()
            time.sleep(0.01)
        
    locais()

##### Fluxo principal #####
def main_game_loop():
    while not meu_jogador.game_over:
        prompt()
    limpar_tela()
    if meu_jogador.local == ['a1','a2','b1','b2','c1','c2']:
        print('''
               ██      ██    ████     ██    ██       ██████    ██████  ████████   ██████
               ██      ██  ██    ██   ██    ██       ██    ██    ██    ██         ██    ██
                 ██  ██    ██    ██   ██    ██       ██    ██    ██    ██████     ██    ██
                   ██      ██    ██   ██    ██       ██    ██    ██    ██         ██    ██
                   ██        ████       ████         ██████    ██████  ████████   ██████


                                        ██████████████████
                                      ██                  ██
                                    ██                      ██
                                  ██                          ██
                                ██                              ██
                                ██                              ██
                                ██    ████              ████    ██
                                ██  ████████          ████████  ██
                                ██  ████████          ████████  ██
                                ██  ████████          ████████  ██
                                ██    ████      ██      ████    ██
                                  ██          ██████          ██
                                    ██████    ██  ██    ██████
                                        ██              ██
                                        ██  ██      ██  ██
                                        ██  ████  ████  ██
                                          ██    ██    ██
      
      
              
              ''')
    sys.exit()

def setup_jogo():
    os.system('clear' if os.name != 'nt' else 'cls')

    pergunta1 = "\n Qual seu nome?\n"
    for caractere in pergunta1:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(0.001)
    meu_jogador.nome = input(">> ")

    pergunta2 = "Qual sua classe?\n(Escolha: guerreiro, mago ou monge)\n"
    for caractere in pergunta2:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(0.001)

    classes_validas = ['guerreiro', 'mago', 'monge']
    jogador_classe = input(">> ").lower()
    while jogador_classe not in classes_validas:
        print("Classe inválida, tente novamente.")
        jogador_classe = input(">> ").lower()
    meu_jogador.classe = jogador_classe
    print(f"Classe selecionada: {meu_jogador.classe.capitalize()}\n")

    if meu_jogador.classe == 'guerreiro':
        pocao_vida_baixa = lista_consumiveis[0]
        pocao_vida_media = lista_consumiveis[1]
        pocao_vida_alta = lista_consumiveis[2]
        arma_padrao = lista_armas[2]
        meu_jogador.vida_base = 100
        meu_jogador.vida = meu_jogador.vida_base
        meu_jogador.vida_max = meu_jogador.vida
        meu_jogador.mana_base = 30
        meu_jogador.mana = meu_jogador.mana_base
        meu_jogador.mana_max = meu_jogador.mana
        meu_jogador.atk_base = 6
        meu_jogador.forca = 2
        meu_jogador.atk = meu_jogador.atk_base
        meu_jogador.item_equipado = Item(arma_padrao['nome'], arma_padrao['atk'], arma_padrao['desc'], True, arma_padrao['consumivel'], arma_padrao['preco'], arma_padrao['especial'])
        meu_jogador.add_item(meu_jogador.item_equipado)
        meu_jogador.atk_final = meu_jogador.atk + meu_jogador.item_equipado.atk
        meu_jogador.add_item(Item(pocao_vida_baixa['nome'], pocao_vida_baixa['atk'], pocao_vida_baixa['desc'], pocao_vida_baixa['equipado'], pocao_vida_baixa['consumivel'], pocao_vida_baixa['preco'], pocao_vida_baixa['especial']))
        meu_jogador.add_item(Item(pocao_vida_media['nome'], pocao_vida_media['atk'], pocao_vida_media['desc'], pocao_vida_media['equipado'], pocao_vida_media['consumivel'], pocao_vida_media['preco'], pocao_vida_media['especial']))
        meu_jogador.add_item(Item(pocao_vida_alta['nome'], pocao_vida_alta['atk'], pocao_vida_alta['desc'], pocao_vida_alta['equipado'], pocao_vida_alta['consumivel'], pocao_vida_alta['preco'], pocao_vida_alta['especial']))
        calcular_atributos(meu_jogador)

    elif meu_jogador.classe == 'mago':
        pocao_mana_baixa = lista_consumiveis[3]
        pocao_mana_media = lista_consumiveis[4]
        pocao_mana_alta = lista_consumiveis[5]
        magia_basica = lista_magias[0]
        magia_basica1 = lista_magias[1]
        efeito = Efeito(lista_efeitos[0]['nome'], lista_efeitos[0]['tipo'], lista_efeitos[0]['tempo'], lista_efeitos[0]['dano'])
        efeito1 = Efeito(lista_efeitos[2]['nome'], lista_efeitos[2]['tipo'], lista_efeitos[2]['tempo'], lista_efeitos[0]['dano'])
        meu_jogador.vida_base = 50
        meu_jogador.vida = meu_jogador.vida_base
        meu_jogador.vida_max = meu_jogador.vida
        meu_jogador.mana_base = 100
        meu_jogador.mana = meu_jogador.mana_base
        meu_jogador.mana_max = meu_jogador.mana
        meu_jogador.atk_base = 5
        meu_jogador.inteligencia = 2
        meu_jogador.atk = meu_jogador.atk_base
        meu_jogador.magias.append(Magia(magia_basica['nome'], magia_basica['dano'], magia_basica['desc'], magia_basica['mana_gasta'], efeito))
        meu_jogador.magias.append(Magia(magia_basica1['nome'], magia_basica1['dano'], magia_basica1['desc'], magia_basica1['mana_gasta'], efeito1))
        meu_jogador.add_item(Item(pocao_mana_baixa['nome'], pocao_mana_baixa['atk'], pocao_mana_baixa['desc'], pocao_mana_baixa['equipado'], pocao_mana_baixa['consumivel'], pocao_mana_baixa['preco'], pocao_mana_baixa['especial']))
        meu_jogador.add_item(Item(pocao_mana_media['nome'], pocao_mana_media['atk'], pocao_mana_media['desc'], pocao_mana_media['equipado'], pocao_mana_media['consumivel'], pocao_mana_media['preco'], pocao_mana_media['especial']))
        meu_jogador.add_item(Item(pocao_mana_alta['nome'], pocao_mana_alta['atk'], pocao_mana_alta['desc'], pocao_mana_alta['equipado'], pocao_mana_alta['consumivel'], pocao_mana_alta['preco'], pocao_mana_alta['especial']))
        calcular_atributos(meu_jogador)

    elif meu_jogador.classe == 'monge':
        meu_jogador.vida_base = 150
        meu_jogador.vida = meu_jogador.vida_base
        meu_jogador.vida_max = meu_jogador.vida
        meu_jogador.mana_base = 0
        meu_jogador.mana = meu_jogador.mana_base
        meu_jogador.mana_max = meu_jogador.mana
        meu_jogador.atk_base = 9
        meu_jogador.forca = 3
        meu_jogador.fortitude = 3
        meu_jogador.atk = meu_jogador.atk_base
        calcular_atributos(meu_jogador)


    fala1 = "Espero que se divirta nessa incrível aventura!\n"
    fala2 = """
    No topo de uma torre esquecida pelos deuses, alguém desperta entre ruínas e cinzas. Sem memória, e com o corpo à beira do colapso, 
    essa figura solitária encontra-se cercada por vestígios de uma batalha apocalíptica – e por um silêncio que pesa como um túmulo.

    Algo terrível aconteceu ali, mas não há ninguém para contar a história.

    Com apenas fragmentos de poder e ecos de um passado perdido, 
    o protagonista precisa descer os andares de uma Torre Misteriosa colossal – 
    uma estrutura viva, repleta de criaturas corrompidas, armadilhas letais e segredos antigos.

    A cada passo, a torre muda. A cada inimigo derrotado, algo esquecido retorna.
    Mas algumas verdades talvez devam permanecer enterradas.

    A jornada para escapar é também uma jornada para descobrir quem você é...
    E por que o mundo parecia ter parado de girar no exato momento em que você caiu.\n"""

    for fala in [fala1, fala2]:
        for caractere in fala:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.001)
    time.sleep(2)

    os.system('clear' if os.name != 'nt' else 'cls')
    print ("▬"*100)
    introducao1 = '''
      O frio das pedras toca sua pele como agulhas. O ar está pesado, carregado de uma magia que pulsa devagar, 
    como um coração moribundo. Ao abrir os olhos, tudo é cinza e vermelho: 
    cinza das cinzas no chão e vermelho do sangue seco pintado em padrões esquecidos no mármore.

      Você se senta com dificuldade. O corpo dói, fraco, como se tivesse atravessado mil batalhas — e talvez tenha. 
      Mas você não se lembra. Do Porque esta aqui ou o Que aconteceu nesse local.\n'''
    for introducao in introducao1:
        sys.stdout.write(introducao)
        sys.stdout.flush()
        time.sleep(0.001)
    ajuda = 'principais comandos: [mover / olhar / mochila / status / mapa]\n'
    for ajuda in ajuda:
        sys.stdout.write(ajuda)
        sys.stdout.flush()
        time.sleep(0.001)

    start_game()
    print_local()

##### Executar #####
tela_titulo()