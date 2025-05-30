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


######## Titulo e afins ########
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
#####################################

######### Setup do jogador ########
class Player:
    def __init__(self):
        self.nome = ''
        self.classe = ''
        self.nivel = 1
        self.xp = 0
        self.xp_max = 100
        self.vida_base = 0
        self.armadura = None
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
        self.ouro = 0
        self.atk_final = self.atk
        self.item_equipado = None
        self.mochila = []
        self.efeitos_status = []
        self.magias = []
        self.local = 'começo'
        self.game_over = False
        self.pular_turno = False
        self.combate = False
        self.dano_magico_final = 0
        self.armadura_vida_max = 0
        self.armadura_vida = 0
        self.armadura_resistencia = 0
    
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
    jogador.dano_magico = jogador.inteligencia * 2
    jogador.dano_magico_final = jogador.dano_magico
    if jogador.item_equipado:
        if jogador.item_equipado.dano_magico:
            jogador.dano_magico_final += jogador.item_equipado.dano_magico
        else:
            jogador.atk_final += jogador.item_equipado.atk
    if jogador.armadura:
        jogador.armadura_vida_max = jogador.armadura.vida_max
        jogador.armadura_vida = jogador.armadura_vida_max
        jogador.armadura_resistencia = jogador.armadura.resistencia
    else:
        jogador.armadura_vida_max = 0
        jogador.armadura_vida = 0
        jogador.armadura_resistencia = 0

def atualizar_atributos(jogador):
    jogador.vida_max = jogador.vida_base + (jogador.fortitude * 10)
    jogador.mana_max = jogador.mana_base + (jogador.inteligencia * 8)
    jogador.atk = jogador.atk_base + (jogador.forca * 2)
    jogador.atk_final = jogador.atk
    jogador.dano_magico = jogador.inteligencia * 2
    jogador.dano_magico_final = jogador.dano_magico
    if jogador.item_equipado:
        if jogador.item_equipado.dano_magico:
            jogador.dano_magico_final += jogador.item_equipado.dano_magico
        else:
            jogador.atk_final += jogador.item_equipado.atk
    if jogador.armadura:
        jogador.armadura_vida_max = jogador.armadura.vida_max
        jogador.armadura_vida = jogador.armadura_vida_max
        jogador.armadura_resistencia = jogador.armadura.resistencia
    else:
        jogador.armadura_vida_max = 0
        jogador.armadura_vida = 0
        jogador.armadura_resistencia = 0

def subi_nivel(jogador):
    pontos = 0
    while jogador.xp >= jogador.xp_max:
        jogador.nivel += 1
        pontos += 3
        resto_xp = jogador.xp - jogador.xp_max
        jogador.xp = resto_xp
        jogador.xp_max +=50
    print(f'{jogador.nome} subiu de nivel para o LVL:'+Fore.GREEN+f'{jogador.nivel}'+Style.RESET_ALL+'!!!')
    while pontos > 0:
        print(f'Pontos restantes: '+Fore.YELLOW+f'{pontos}')
        escolha = input(Fore.GREEN+"Aumentar Forca (for)"+Style.RESET_ALL+", "+Fore.RED+"Fortitude (fort)"+Style.RESET_ALL+" ou "+Fore.BLUE+"Inteligência (int)"+Style.RESET_ALL+": ").lower()
        
        if escolha == 'for':
            escolha1 = int(input('Quantos pontos em força deseja colocar?\n>>'))             
            if escolha1 > pontos:
                print(Fore.RED+'Pontos insuficientes'+Style.RESET_ALL)
                continue
            jogador.forca += escolha1
            pontos -= escolha1
            print(f'for: {jogador.forca}')

        elif escolha == 'fort':
            escolha2 = int(input('Quantos pontos em fortitude deseja colocar?\n>>'))
            if escolha2 > pontos:
                print(Fore.RED+'Pontos insuficientes'+Style.RESET_ALL)
                continue
            jogador.fortitude += escolha2
            pontos -= escolha2
            print(f'fortitude: {jogador.fortitude}')

        elif escolha == 'int':
            escolha3 = int(input('Quantos pontos em inteligência deseja colocar?\n>>'))
            if escolha3 > pontos:
                print(Fore.RED+'Pontos insuficientes'+Style.RESET_ALL)
                continue
            jogador.inteligencia += escolha3
            pontos -= escolha3
            print(f'inteligência: {jogador.inteligencia}')

        else:
            print(Fore.RED+'Comando invádido'+Style.RESET_ALL)
            continue
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
    print('vida:'+Fore.RED+f' {jogador.vida}/{jogador.vida_max}'+Style.RESET_ALL+ ' / MANA: '+Fore.BLUE+f'{jogador.mana}/{jogador.mana_max}'+Style.RESET_ALL+' / ATK: '+Fore.YELLOW+f'{jogador.atk}'+Style.RESET_ALL+' / MAG.ATK: '+Fore.LIGHTBLUE_EX+f'{jogador.dano_magico}'+Style.RESET_ALL)
    if jogador.item_equipado:
        if jogador.item_equipado.dano_magico:
            print(f'arma: {jogador.item_equipado.nome} DANO MÁGICO: {jogador.item_equipado.dano_magico}')
        else:
            print(f'arma: {jogador.item_equipado.nome} ATK: {jogador.item_equipado.atk}')
    else:
        print('arma: Nenhuma arma equipada')
    print(f'forca: '+Fore.GREEN+f'{jogador.forca}'+Style.RESET_ALL+' fortitude: '+Fore.RED+f'{jogador.fortitude}'+Style.RESET_ALL+' inteligência: '+Fore.BLUE+f'{jogador.inteligencia}'+Style.RESET_ALL)
    if jogador.armadura:
        print(f'armadura: {jogador.armadura.nome} DEF: {jogador.armadura.defesa} RES: {jogador.armadura.resistencia}%')
        print('vida da armadura: '+Fore.CYAN+f'{jogador.armadura_vida}'+Style.RESET_ALL+'/'+Fore.CYAN+f'{jogador.armadura_vida_max}'+Style.RESET_ALL)
    else:
        print('armadura: Nenhuma armadura equipada')
    input(Fore.YELLOW+'[Pressione Enter]'+Style.RESET_ALL)
    limpar_tela()
    print_local()
    main_game_loop()


def experiencia(monstro):
    meu_jogador.xp += monstro.xp
    if meu_jogador.xp >= meu_jogador.xp_max:
        subi_nivel(meu_jogador)

################################################################

############## MONSTROS  ##############
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
    if meu_jogador.local not in ['c1', 'h1']:
        print('Você não está em um circulo de invocação!')
        limpar_tela()
        print_local()
        main_game_loop()
    if meu_jogador.local == 'c1':
        print('Um monstro apareceu!')
        luta(robo_aleatorio(), meu_jogador)
    elif meu_jogador.local == 'h1':
        fala = 'Você encosta na estátua e sente os espiritos se movendo em volta de você, logo eles entram na estátua que cria vida e te ataca.'
        for caractere in fala:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.02)
        input(Fore.YELLOW+'[Pressione Enter]'+Style.RESET_ALL)  
        luta(estatua, meu_jogador)

def robo_aleatorio():
    monstro_robo = random.choice(lista_monstros_robo)
    return Monstro(monstro_robo['nome'], monstro_robo['vida'], monstro_robo['nivel'], monstro_robo['atk'], monstro_robo['xp'], monstro_robo['ouro'], monstro_robo['boss'])

def invocacao():
    if meu_jogador.local != 'e1':
        print(Fore.RED+'Comando inválido!'+Style.RESET_ALL)
        limpar_tela()
        print_local()
        main_game_loop()
    fala = 'Um monstro apareceu!'
    for caractere in fala:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(0.02)
    luta(invocacao_aleatoria(), meu_jogador)

def invocacao_aleatoria():
    monstro = random.choice(lista_monstros_invocacoes)
    return Monstro(monstro['nome'], monstro['vida'], monstro['nivel'], monstro['atk'], monstro['xp'], monstro['ouro'], monstro['boss'])

#######################################################################

class Item:
    def __init__(self, nome, atk, desc, equipado, consumivel, preco, especial):
        self.nome = nome
        self.atk = atk
        self.desc = desc
        self.equipado = equipado
        self.consumivel = consumivel
        self.preco = preco
        self.especial = especial
        self.dano_magico = None
    
class Armadura(Item):
    def __init__(self, nome, defesa, vida_max, resistencia, desc, equipado, consumivel, preco, especial):
        # Chama o construtor da classe Item com atk=0 para armaduras
        super().__init__(nome, 0, desc, equipado, consumivel, preco, especial)
        self.defesa = defesa
        self.vida_max = vida_max
        self.resistencia = resistencia
class ArmaMagica(Item):
    def __init__(self, dano_magico, nome, atk, desc, equipado, consumivel, preco, especial):
        super().__init__(nome, atk, desc, equipado, consumivel, preco, especial)
        self.dano_magico = dano_magico
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
        if meu_jogador.local != '':
            print(Fore.RED+'Comando inválido!'+Style.RESET_ALL)
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
                print(Fore.RED + '**ITEM INVÁLIDO**'+Style.RESET_ALL)
                mostrar_loja()
            
            if lista_itens_loja[escolha]['consumivel']:
                print(f"{lista_itens_loja[escolha]['nome']} | Preço: {lista_itens_loja[escolha]['preco']} | Descricao: {lista_itens_loja[escolha]['desc']} {status}\n")
            else:
                print(f"{lista_itens_loja[escolha]['nome']} | ATK: {lista_itens_loja[escolha]['atk']} | Preço: {lista_itens_loja[escolha]['preco']} | Descricao: {lista_itens_loja[escolha]['desc']} {status}\n")
            print('[compra | voltar | fechar]')
            acao = input(Fore.LIGHTYELLOW_EX + '>>'+Style.RESET_ALL)
            if acao not in ['comprar', 'voltar', 'fechar']:
                print(Fore.RED + '**COMANDO INVÁLIDO**'+Style.RESET_ALL)
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
            print(Fore.RED + '**ITEM INVÁLIDO**'+Style.RESET_ALL)
            mostrar_loja()

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
    print (Fore.LIGHTGREEN_EX+"Você bebeu a poção!!!"+Style.RESET_ALL)
def pocao_vida_media():
    meu_jogador.vida += 30
    if meu_jogador.vida > meu_jogador.vida_max:
        meu_jogador.vida = meu_jogador.vida_max
    print (Fore.LIGHTGREEN_EX+"Você bebeu a poção!!!"+Style.RESET_ALL)
def pocao_vida_alta():
    meu_jogador.vida += 60
    if meu_jogador.vida > meu_jogador.vida_max:
        meu_jogador.vida = meu_jogador.vida_max
    print (Fore.LIGHTGREEN_EX+"Você bebeu a poção!!!"+Style.RESET_ALL)
def carne_homunculo():
    meu_jogador.vida += 80
    if meu_jogador.vida > meu_jogador.vida_max:
        meu_jogador.vida = meu_jogador.vida_max
    print (Fore.LIGHTGREEN_EX+"Você comeu a carne do homunculo!!!"+Style.RESET_ALL)

def pocao_mana():
    meu_jogador.mana += 15
    if meu_jogador.mana > meu_jogador.mana_max:
        meu_jogador.mana = meu_jogador.mana_max
    print (Fore.LIGHTGREEN_EX+"Você bebeu a poção!!!"+Style.RESET_ALL)
def pocao_mana_media():
    meu_jogador.mana += 30
    if meu_jogador.mana > meu_jogador.mana_max:
        meu_jogador.mana = meu_jogador.mana_max
    print (Fore.LIGHTGREEN_EX+"Você bebeu a poção!!!"+Style.RESET_ALL)
def pocao_mana_alta():
    meu_jogador.mana += 60
    if meu_jogador.mana > meu_jogador.mana_max:
        meu_jogador.mana = meu_jogador.mana_max
    print (Fore.LIGHTGREEN_EX+"Você bebeu a poção!!!"+Style.RESET_ALL)

def pocao_vida_lendaria():
    meu_jogador.vida += 100
    if meu_jogador.vida > meu_jogador.vida_max:
        meu_jogador.vida = meu_jogador.vida_max
    print(Fore.LIGHTGREEN_EX + "\nVocê bebeu a Poção de Vida Lendária e recuperou 100 de vida!" + Style.RESET_ALL)
    time.sleep(1.5)

def pocao_mana_lendaria():
    meu_jogador.mana += 100
    if meu_jogador.mana > meu_jogador.mana_max:
        meu_jogador.mana = meu_jogador.mana_max
    print(Fore.LIGHTBLUE_EX + "\nVocê bebeu a Poção de Mana Lendária e recuperou 100 de mana!" + Style.RESET_ALL)
    time.sleep(1.5)

def pocao_erva_de_mana():
    meu_jogador.mana += 200
    if meu_jogador.mana > meu_jogador.mana_max:
        meu_jogador.mana = meu_jogador.mana_max
    print(Fore.LIGHTBLUE_EX + "\nVocê fez um chá de ervas e recuperou 200 de mana!" + Style.RESET_ALL)
    time.sleep(1.5)

def flocos_de_tem():
    meu_jogador.vida += 200
    if meu_jogador.vida > meu_jogador.vida_max:
        meu_jogador.vida = meu_jogador.vida_max
    print (Fore.LIGHTGREEN_EX+" Vocé comeu os flocos de tem!!! Tem um gosto meio estranho..."+Style.RESET_ALL)

def usar_pergaminho_apocalipse():
    magia_apocalipse = Magia(
        nome="Apocalipse",
        dano=100,
        desc="Invoca um poder ancestral que causa dano massivo e queima o inimigo por 3 turnos",
        mana_gasta=50,
        efeito=Efeito(
            nome="chamas do fim",
            tipo="dano",
            tempo=3,
            dano= 50
        )
    )
    
    # Adiciona à lista de magias do jogador
    meu_jogador.magias.append(magia_apocalipse)
    
    print(Fore.MAGENTA + "\nAo usar o pergaminho, conhecimento ancestral invade sua mente!" + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "Você aprendeu a magia: APOCALIPSE!" + Style.RESET_ALL)
    input(Fore.YELLOW+'[Pressione Enter]'+Style.RESET_ALL)

def usar_pergaminho_estilhaço_sismico():
    magia_estilhaço = Magia(
        nome="Estilhaço Sísmico",
        dano=200,
        desc="Você invoca um fragmento da terra que explode em estilhaços, lançando pedras afiadas contra seu inimigo.",
        mana_gasta=70,
        efeito=Efeito(
            nome="",
            tipo="skip",
            tempo=0,
        )
    )
    meu_jogador.magias.append(magia_estilhaço)
    
    print(Fore.MAGENTA + "\nAo usar o pergaminho, conhecimento ancestral invade sua mente!" + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "Você aprendeu a magia: Estilhaço Sísmico!" + Style.RESET_ALL)
    input(Fore.YELLOW+'[Pressione Enter]'+Style.RESET_ALL)

def usar_pergaminho_cometa_pedrilhante():
    magia_cometa = Magia(
        nome="Cometa Pedrilhante",
        dano=50,
        desc="O usuário lança um cometa azul que causa dano ao inimigo.",
        mana_gasta=40,
    )
    meu_jogador.magias.append(magia_cometa)
    
    print(Fore.MAGENTA + "\nAo usar o pergaminho, conhecimento ancestral invade sua mente!" + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "Você aprendeu a magia: Cometa Pedrilhante!" + Style.RESET_ALL)
    input(Fore.YELLOW+'[Pressione Enter]'+Style.RESET_ALL)
    
def usar_pergaminho_raizes():
 
    magia_raizes = Magia(
        nome="Raizes da Morte",
        dano=10,
        desc="O usuário invoca raizes do chão que grudão em seu alvo e aplicam efeito de envenenamento.",
        mana_gasta=15,
        efeito=Efeito(
            nome="Envenenado",
            tipo="dano",
            tempo=3,
            dano= 10
        ))
    meu_jogador.magias.append(magia_raizes)
    
    print(Fore.MAGENTA + "\nAo usar o pergaminho, conhecimento ancestral invade sua mente!" + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "Você aprendeu a magia: Raizes da Morte!" + Style.RESET_ALL)
    input(Fore.YELLOW+'[Pressione Enter]'+Style.RESET_ALL)

def usar_pergaminho_absorcao():
    magia_absorção = Magia(
        nome="Absorção de Sangue",
        dano= 30,
        desc="O usuário lança uma magia de sangue que absorve 30 pontos de vida do alvo.",
        mana_gasta=30,
        efeito=Efeito(
            nome="",
            tipo="absorção",
            tempo=0
        )
    )


    meu_jogador.magias.append(magia_absorção)
    
    print(Fore.MAGENTA + "\nAo usar o pergaminho, conhecimento ancestral invade sua mente!" + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "Você aprendeu a magia: Absorção de Sangue!" + Style.RESET_ALL)
    input(Fore.YELLOW+'[Pressione Enter]'+Style.RESET_ALL)

lista_itens_loja = [
    { 
        'nome': 'Poção de Vida Lendária', 
        'atk': 0,
        'preco': 130, 
        'desc': 'Cura 100 pontos de vida', 
        'equipado': False, 
        'consumivel': True, 
        'especial': False
    },
    { 
        'nome': 'Poção de Mana Lendária', 
        'atk': 0,
        'preco': 130, 
        'desc': 'Restaura 100 pontos de mana', 
        'equipado': False, 
        'consumivel': True, 
        'especial': False
    },
    { 
        'nome': 'Espada do Abismo', 
        'atk': 40, 
        'preco': 500, 
        'desc': 'Uma espada que emana energia sombria', 
        'equipado': False, 
        'consumivel': False, 
        'especial': False
    },
    { 
        'nome': 'Armadura do Eclipse', 
        'defesa': 10, 
        'vida_max': 80, 
        'resistencia': 30, 
        'preco': 600, 
        'desc': 'Armadura que absorve parte do dano recebido', 
        'equipado': False, 
        'consumivel': False,
        'especial': False
    },
    { 
        'nome': 'Pergaminho do Apocalipse', 
        'atk': 0,
        'preco': 500, 
        'desc': 'Concede uma magia poderosa temporariamente', 
        'equipado': False, 
        'consumivel': True, 
        'especial': True
    }
    ]
lista_itens_loja_temmie = [
    { 
        'nome': 'Flocos de TEM', 
        'atk': 0,
        'preco': 200, 
        'desc': 'Um cereal crocante e misterioso. Cura 200 HP.', 
        'equipado': False, 
        'consumivel': True, 
        'especial': False
    },
    { 
        'nome': 'Erva de Mana.', 
        'atk': 0,
        'preco': 200, 
        'desc': 'Plantada e colhida por Temmie. Restaura 200 pontos de mana.', 
        'equipado': False, 
        'consumivel': True, 
        'especial': False
    },
    { 
        'nome': 'Espada TEM', 
        'atk': 100, 
        'preco': 999, 
        'desc': 'Uma estranha espada que parece um gato. Quando usada para atacar faz sons de miados.', 
        'equipado': False, 
        'consumivel': False, 
        'especial': False
    },
    { 
        'nome': 'Armadura TEM', 
        'defesa': 30, 
        'vida_max': 100, 
        'resistencia': 60, 
        'preco': 999, 
        'desc': 'Uma armadura super fofa e poderosa!', 
        'equipado': False, 
        'consumivel': False,
        'especial': False
    },
]

lista_itens_loja_g1 = [
    { 
        'nome': 'Pocao de vida baixa', 
        'atk': 0,
        'preco': 25, 
        'desc': 'Uma pocao de vida, cura 15 pontos de vida.', 
        'equipado': False, 
        'consumivel': True, 
        'especial': False},

     { 
        'nome': 'Pocao de vida media', 
        'atk': 0,
        'preco': 45, 
        'desc': 'Uma pocao de vida media, cura 30 pontos de vida.', 
        'comprado': False, 
        'equipado': False, 
        'consumivel': True, 
        'especial': False},

    { 
        'nome': 'Pocao de vida alta', 
        'atk': 0,'preco': 85, 
        'desc': 'Uma pocao de vida alta, cura 60 pontos de vida.', 
        'comprado': False, 
        'equipado': False, 
        'consumivel': True, 
        'especial': False},
     { 
        'nome': 'Pocao de mana baixa', 
        'atk': 0,
        'preco': 25, 
        'desc': 'Uma pocao de mana, cura 15 pontos de mana.', 
        'equipado': False, 
        'consumivel': True,
        'especial': False},

    { 
        'nome': 'Pocao de mana media', 
        'atk': 0,
        'preco': 45, 
        'desc': 'Uma pocao de mana media, cura 30 pontos de mana.', 
        'comprado': False, 
        'equipado': False, 
        'consumivel': True, 
        'especial': False},

    { 
        'nome': 'Pocao de mana alta', 
        'atk': 0,
        'preco': 85, 
        'desc': 'Uma pocao de mana alta, cura 60 pontos de mana.', 
        'comprado': False, 
        'equipado': False, 
        'consumivel': True, 
        'especial': False},

    { 
        'nome': 'Armadura de Couro', 
        'defesa': 2, 
        'vida_max': 25, 
        'resistencia': 0, 
        'desc': 'Armadura leve feita de couro endurecido.', 
        'comprado': False, 
        'equipado': False, 
        'consumivel': False,
        'preco': 50, 
        'especial': False},
    { 
        'nome': 'Armadura de Ferro', 
        'defesa': 3, 
        'vida_max': 30, 
        'resistencia': 10, 
        'preco': 50, 
        'desc': 'Armadura média feita de placas de ferro.', 
        'comprado': False, 
        'equipado': False, 
        'consumivel': False, 
        'especial': False},

    { 
        'nome': 'Pergaminho do Cometa Pedrilhante', 
        'atk': 0,
        'preco': 100, 
        'desc': 'Concede uma magia poderosa chamada Cometa Pedrilhante', 
        'equipado': False, 
        'consumivel': True, 
        'especial': True
    }
]

lista_consumiveis = [
    { 'nome': 'Pocao de vida baixa', 'atk': 0,'preco': 50, 'desc': 'Uma pocao de vida, cura 15 pontos de vida.', 'equipado': False, 'consumivel': True, 'especial': False},
    { 'nome': 'Pocao de vida media', 'atk': 0,'preco': 100, 'desc': 'Uma pocao de vida media, cura 30 pontos de vida.', 'comprado': False, 'equipado': False, 'consumivel': True, 'especial': False},
    { 'nome': 'Pocao de vida alta', 'atk': 0,'preco': 150, 'desc': 'Uma pocao de vida alta, cura 60 pontos de vida.', 'comprado': False, 'equipado': False, 'consumivel': True, 'especial': False},
    { 'nome': 'Pocao de mana baixa', 'atk': 0,'preco': 50, 'desc': 'Uma pocao de mana, cura 15 pontos de mana.', 'equipado': False, 'consumivel': True, 'especial': False},
    { 'nome': 'Pocao de mana media', 'atk': 0,'preco': 100, 'desc': 'Uma pocao de mana media, cura 30 pontos de mana.', 'comprado': False, 'equipado': False, 'consumivel': True, 'especial': False},
    { 'nome': 'Pocao de mana alta', 'atk': 0,'preco': 150, 'desc': 'Uma pocao de mana alta, cura 60 pontos de mana.', 'comprado': False, 'equipado': False, 'consumivel': True, 'especial': False},
]

lista_arma_ik = [
    {'nome': 'Devoradora de estrelas', 'atk': 10000, 'preco': 999999, 'desc': 'Você não deveria ter acesso a isso.', 'equipado': False, 'consumivel': False, 'especial': False}
]

lista_armas = [
    {'nome': 'Adaga enferrujada', 'atk': 3, 'preco': 100, 'desc': 'Parece ser bem antiga', 'equipado': False, 'consumivel': False, 'especial': False},
    {'nome': 'Espada longa', 'atk': 4, 'preco': 100, 'desc': 'A espada de todo guerreiro.', 'equipado': False, 'consumivel': False, 'especial': False},
]
lista_armas_magicas = [
    {'nome': 'Varinha capenga', 'dano_magico': 2,'atk': 0, 'preco': 100, 'desc': 'É nova, mas bem barata', 'equipado': False, 'consumivel': False, 'especial': False},
    {'nome': 'Grimório ', 'dano_magico': 4,'atk': 2, 'preco': 100, 'desc': 'O grimório de um mago, o local de sua sabedoria.', 'equipado': False, 'consumivel': False, 'especial': False},

]
lista_armas_especiais = [
    {'nome': 'Manoplas de ferro', 'atk': 20, 'preco': 150, 'desc': 'Usada a muito tempo por um exímio monge, as manoplas de ferro são uma das mais fortes armas de um monge', 'equipado': False, 'consumivel': False, 'especial': False},
    {'nome': 'Espada do guerreiro impetuoso', 'atk': 12, 'preco': 150, 'desc': 'espada usada por um guerreiro impetuoso, ela tem um grande poder de ataque', 'equipado': False, 'consumivel': False, 'especial': False},
    {'nome': 'Grimório Morbius', 'atk': 0, 'preco': 150, 'desc': 'Um grimório desconhecido e com um grande potencial', 'equipado': False, 'consumivel': False, 'especial': False},    
]
lista_armaduras = [
    { 
    'nome': 'Armadura de Iniciante', 
    'defesa': 1, 
    'vida_max': 20, 
    'resistencia': 0, 
    'desc': 'Armadura básica para guerreiros iniciantes',
    'equipado': False, 
    'consumivel': False, 
    'preco': 20, 
    'especial': False
    },

    { 
        'nome': 'Armadura de Couro', 
        'defesa': 2, 
        'vida_max': 25, 
        'resistencia': 0, 
        'desc': 'Armadura leve feita de couro endurecido.', 
        'comprado': False, 
        'equipado': False, 
        'consumivel': False,
        'preco': 30, 
        'especial': False},

    { 
        'nome': 'Armadura de Ferro', 
        'defesa': 3, 
        'vida_max': 30, 
        'resistencia': 0, 
        'preco': 50, 
        'desc': 'Armadura média feita de placas de ferro.', 
        'comprado': False, 
        'equipado': False, 
        'consumivel': False, 
        'especial': False},

    { 
        'nome': 'Armadura de Aço', 
        'defesa': 4, 
        'vida_max': 45, 
        'resistencia': 0, 
        'preco': 70, 
        'desc': 'Armadura pesada feita de aço temperado.', 
        'comprado': False, 
        'equipado': False, 
        'consumivel': False, 
        'especial': False},
]

lista_itens_especiais = [
    {'nome': 'Anel Desconhecido', 'atk': 0, 'preco': 00, 'desc': 'Um anel feito de ouro. Sua origem é desconhecida.', 'equipado': False, 'consumivel': False, 'especial': True},
    {'nome': 'Máscara da Raiva', 'atk': 0, 'preco': 00, 'desc': 'Máscara pega no Salão das Vozes Vazias. O uso da mesma é desconhecido.', 'equipado': False, 'consumivel': False, 'especial': True},
    {'nome': 'Máscara do Medo', 'atk': 0, 'preco': 00, 'desc': 'Máscara pega no Salão das Vozes Vazias. O uso da mesma é desconhecido.', 'equipado': False, 'consumivel': False, 'especial': True},
    {'nome': 'Máscara da Alegria', 'atk': 0, 'preco': 00, 'desc': 'Máscara pega no Salão das Vozes Vazias. O uso da mesma é desconhecido.', 'equipado': False, 'consumivel': False, 'especial': True},
    {'nome': 'Máscara da Loucura', 'atk': 0, 'preco': 00, 'desc': 'Máscara pega no Salão das Vozes Vazias. O uso da mesma é desconhecido.', 'equipado': False, 'consumivel': False, 'especial': True},
    {'nome': 'Núcleo de Robo', 'atk': 0, 'preco': 00, 'desc': 'Pode ser usado para dar vida a um robo', 'equipado': False, 'consumivel': False, 'especial': True},
]  

lista_nucleo = [
    {'nome': 'Núcleo de Robo', 'atk': 0, 'preco': 00, 'desc': 'Pode ser usado para dar vida a um robo', 'equipado': False, 'consumivel': False, 'especial': True},
]

lista_itens_bosses = [
    { 'nome': 'Pocao de vida baixa', 'atk': 0,'preco': 50, 'desc': 'Uma pocao de vida, cura 15 pontos de vida.', 'equipado': False, 'consumivel': True, 'especial': False},#0
    { 'nome': 'Pocao de mana baixa', 'atk': 0,'preco': 50, 'desc': 'Uma pocao de mana, cura 15 pontos de mana.', 'equipado': False, 'consumivel': True, 'especial': False},#1
    { 'nome': 'Carne de Homunculo', 'atk': 0,'preco': 60, 'desc': 'Carne do Homunculo, cura 80 pontos de vida.', 'equipado': False, 'consumivel': True, 'especial': False},#2
        { 
        'nome': 'Armadura de Homunculo', 
        'defesa': 5, 
        'vida_max': 20, 
        'resistencia': 10, 
        'desc': 'Armadura leve feita do couro do Homunculo.', 
        'comprado': False, 
        'equipado': False, 
        'consumivel': False,
        'preco': 100, 
        'especial': False}, #3
        { 
        'nome': 'Armadura do Cavaleiro Caido', 
        'defesa': 2, 
        'vida_max': 50, 
        'resistencia': 30, 
        'desc': 'Armadura pesada feita de aço temperado. Armadura usada pelo Cavaleiro Caido.', 
        'comprado': False, 
        'equipado': False, 
        'consumivel': False,
        'preco': 200, 
        'especial': False}, #4

        {'nome': 'Espada do Cavaleiro Caido', 
         'atk': 20, 
         'preco': 150, 
         'desc': 'Espada usada pelo Cavaleiro Caido.', 
         'equipado': False,
         'consumivel': False, 
         'especial': False}, #5

        {'nome': 'Manoplas do Cavaleiro Caido', 
         'atk': 25, 
         'preco': 150, 
         'desc': 'Manoplas usadas pelo Cavaleiro Caido.', 
         'equipado': False,
         'consumivel': False, 
         'especial': False}, #6

        {'nome': 'Martelo de Guerra', 
         'atk': 40, 
         'preco': 300, 
         'desc': 'Martelo usado pela Forjadora.', 
         'equipado': False,
         'consumivel': False, 
         'especial': False}, #7

        { 
        'nome': 'Armadura de Ossos', 
        'defesa': 5, 
        'vida_max': 50, 
        'resistencia': 40, 
        'desc': 'Armadura pesada feita de aço temperado. Armadura usada pelo Cavaleiro Caido.', 
        'comprado': False, 
        'equipado': False, 
        'consumivel': False,
        'preco': 200, 
        'especial': False}, #8

            { 
        'nome': 'Pergaminho do Estilhaço Sísmico', 
        'atk': 0,
        'preco': 0, 
        'desc': 'Concede uma magia poderosa chamado Estilhaço Sísmico.', 
        'equipado': False, 
        'consumivel': True, 
        'especial': True}, #9
            { 
        'nome': 'Pergaminho das Raizes da Morte', 
        'atk': 0,
        'preco': 0, 
        'desc': 'Concede uma magia poderosa chamado Raizes da morte.', 
        'equipado': False, 
        'consumivel': True, 
        'especial': True}, #10
            { 
        'nome': 'Pergaminho da Absorção de Sangue', 
        'atk': 0,
        'preco': 0, 
        'desc': 'Concede uma magia poderosa chamado Absorção de Sangue.', 
        'equipado': False, 
        'consumivel': True, 
        'especial': True}, #11

        {'nome': 'Cajado do Sábio', 
         'dano_magico': 40,
         'atk': 0, 
         'preco': 350, 
         'desc': 'Cajado feito de pedras de mana, emana uma energia estranha.', 
         'equipado': False, 
         'consumivel': False, 
         'especial': False}, #12

        {'nome': 'Zweihander', 
         'atk': 50, 
         'preco': 350, 
         'desc': 'A arma fiel de todos os jogadores de SoulsLike.', 
         'equipado': False,
         'consumivel': False, 
         'especial': False}, #13

        {'nome': 'Punhos de Shiva', 
         'atk': 65, 
         'preco': 350, 
         'desc': 'As mãos de Shiva lhe concede poder para bater em todos os monstros.', 
         'equipado': False,
         'consumivel': False, 
         'especial': False}, #14

        { 
        'nome': 'Armadura de Escamas de Dragão', 
        'defesa': 10, 
        'vida_max': 100, 
        'resistencia': 50, 
        'desc': 'Uma armadura dígna de um heroi.', 
        'comprado': False, 
        'equipado': False, 
        'consumivel': False,
        'preco': 200, 
        'especial': False}, #15

]

lista_magias = [
    {'nome': 'Bola de fogo', 'dano': 20, 'desc':'A magia mais forte de um mago', 'mana_gasta': 30},
    {'nome': 'Rajada de Gelo', 'dano': 10, 'desc':'Esfrio né', 'mana_gasta': 35},
]

lista_efeitos = [
    {'nome': 'queimação', 'tipo': 'dano', 'tempo': 2, 'dano': 5},
    {'nome': 'envenamento', 'tipo': 'dano', 'tempo': 2, 'dano': 4},
    {'nome': 'congelamento', 'tipo': 'pular', 'tempo': 3},
    {'nome': 'atordoamento', 'tipo': 'skip', 'tempo': 1},
]

lista_monstros_normais = [
    {'nome': 'slime', 'vida': 10, 'nivel': 1, 'atk': 2, 'xp': 150, 'ouro': 100, 'boss': False}, #0
    {'nome': 'goblin', 'vida': 20, 'nivel': 2, 'atk': 4, 'xp': 100, 'ouro': 200, 'boss': False}, #1
    {'nome': 'lobo selvagem', 'vida': 25, 'nivel': 3, 'atk': 5, 'xp': 15, 'ouro': 100, 'boss': False}, #2
    {'nome': 'esqueleto', 'vida': 30, 'nivel': 4, 'atk': 6, 'xp': 20, 'ouro': 200, 'boss': False}, #3
    {'nome': 'zumbi', 'vida': 35, 'nivel': 4, 'atk': 4, 'xp': 18, 'ouro': 100, 'boss': False}, #4
    {'nome': 'morcego gigante', 'vida': 28, 'nivel': 3, 'atk': 6, 'xp': 12, 'ouro': 200, 'boss': False}, #5
    {'nome': 'aranha venenosa', 'vida': 22, 'nivel': 2, 'atk': 7, 'xp': 14, 'ouro': 100, 'boss': False}, #6
    {'nome': 'orc', 'vida': 40, 'nivel': 5, 'atk': 8, 'xp': 25, 'ouro': 200, 'boss': False}, #7
    {'nome': 'troll da caverna', 'vida': 50, 'nivel': 6, 'atk': 10, 'xp': 30, 'ouro': 300, 'boss': False}, #8
    {'nome': 'estatua', 'vida': 25, 'nivel': 35, 'atk': 20, 'xp': 2000, 'ouro': 100, 'boss': False}, #9
    {'nome': 'Robô Gigante', 'vida': 25, 'nivel': 7, 'atk': 10, 'xp': 200, 'ouro': 70, 'boss': True}, #10
]

lista_monstros_robo = [
    {'nome': 'Autômato', 'vida': 20, 'nivel': 1, 'atk': 5, 'xp': 50, 'ouro': 2, 'boss': False},
    {'nome': 'Autômato', 'vida': 20, 'nivel': 2, 'atk': 6, 'xp': 60, 'ouro': 4, 'boss': False},
    {'nome': 'Autômato', 'vida': 20, 'nivel': 3, 'atk': 7, 'xp': 80, 'ouro': 6, 'boss': False},
    {'nome': 'Autômato', 'vida': 20, 'nivel': 4, 'atk': 8, 'xp': 100, 'ouro': 8, 'boss': False},
    {'nome': 'Autômato', 'vida': 20, 'nivel': 5, 'atk': 9, 'xp': 130, 'ouro': 10,'boss': False},
]

lista_monstros_invocacoes = [
    {'nome': 'Tieflíngs', 'vida': 15, 'nivel': 8, 'atk': 8, 'xp': 100, 'ouro': 10, 'boss': False},
    {'nome': 'Tieflíngs', 'vida': 15, 'nivel': 9, 'atk': 9, 'xp': 150, 'ouro': 15, 'boss': False},
    {'nome': 'Demônio Inferior', 'vida': 15, 'nivel': 10, 'atk': 7, 'xp': 170, 'ouro': 20, 'boss': False},
    {'nome': 'Demônio Inferior', 'vida': 15, 'nivel': 11, 'atk': 8, 'xp': 190, 'ouro': 25, 'boss': False},
    {'nome': 'Demoníaco', 'vida': 15, 'nivel': 7, 'atk': 12, 'xp': 210, 'ouro': 30, 'boss': False},
    {'nome': 'Demoníaco', 'vida': 15, 'nivel': 8, 'atk': 13, 'xp': 230, 'ouro': 35, 'boss': False},
]
lista_monstros_fixos = [
    {'nome': 'Guardião Enraizado', 'vida': 25, 'nivel': 4, 'atk': 7, 'xp': 150, 'ouro': 100, 'boss': True},
    {'nome': 'Homunculo Grotesco', 'vida': 50, 'nivel': 10, 'atk': 14, 'xp': 350, 'ouro': 200, 'boss': True},
    {'nome': 'A Forjadora', 'vida': 50, 'nivel': 30, 'atk': 30, 'xp': 3000, 'ouro': 600, 'boss': True},
]
lista_monstros_semi_boss = [
    {'nome': 'Cavaleiro Caido', 'vida': 25, 'nivel': 20, 'atk': 10, 'xp': 1000, 'ouro': 150, 'boss': True},
    {'nome': 'Mímico', 'vida': 40, 'nivel': 40, 'atk': 35, 'xp': 3500, 'ouro': 700, 'boss': True},
    {'nome': 'Crow Mauler', 'vida': 30, 'nivel': 40, 'atk': 40, 'xp': 4000, 'ouro': 700, 'boss': True},
]
lista_monstros_mascara = [
    {'nome': 'Krothar, o Espectro da Carnificina', 'vida': 30, 'nivel': 50, 'atk': 60, 'xp': 4500, 'ouro': 700, 'boss': True},#1
    {'nome': 'Nyxthar, o Devorador de Almas', 'vida': 50, 'nivel': 50, 'atk': 35, 'xp': 4500, 'ouro': 700, 'boss': True},#2
    {'nome': 'Maelis, o Cômico Macabro', 'vida': 40, 'nivel': 50, 'atk': 40, 'xp': 4500, 'ouro': 700, 'boss': True},#3
    {'nome': 'Zalgoth, o Abismo Sem Rumo', 'vida': 50, 'nivel': 50, 'atk': 60, 'xp': 4500, 'ouro': 700, 'boss': True},#4
                        ]

mapa_mascaras_bosses = {
    "Máscara da Raiva": lista_monstros_mascara[0],
    "Máscara do Medo": lista_monstros_mascara[1],
    "Máscara da Alegria": lista_monstros_mascara[2],
    "Máscara da Loucura": lista_monstros_mascara[3],
}

def raiva():
    if meu_jogador.local == 'b1' and mapa[meu_jogador.local]['SOLVED'] == False:
        fala1 = '\nMáscara da raiva adicionada ao seu inventário!\n'
        for falas in fala1:
            sys.stdout.write(falas)
            sys.stdout.flush()
            time.sleep(0.02)
        input(Fore.YELLOW+'\n[Pressione Enter]\n'+Style.RESET_ALL)
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
        fala2 = Fore.YELLOW +'\nMáscara do medo adicionada ao seu inventário!\n'+ Style.RESET_ALL
        for falas in fala2:
            sys.stdout.write(falas)
            sys.stdout.flush()
            time.sleep(0.02)
        input(Fore.YELLOW+'\n[Pressione Enter]\n'+Style.RESET_ALL)
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
        fala3 = Fore.YELLOW +'\nMáscara da alegria adicionada ao seu inventário!\n' + Style.RESET_ALL
        for falas in fala3:
            sys.stdout.write(falas)
            sys.stdout.flush()
            time.sleep(0.02)
        input(Fore.YELLOW+'\n[Pressione Enter]\n'+Style.RESET_ALL)
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
        fala3 = Fore.YELLOW +'\nMáscara da loucura adicionada ao seu inventário!\n'+Style.RESET_ALL
        for falas in fala3:
            sys.stdout.write(falas)
            sys.stdout.flush()
            time.sleep(0.02)
        input(Fore.YELLOW+'\n[Pressione Enter]\n'+Style.RESET_ALL)
        item4 = lista_itens_especiais[4]
        meu_jogador.add_item(Item(item4['nome'], item4['atk'], item4['desc'], item4['equipado'], item4['consumivel'], item4['preco'], item4['especial']))
        mapa[meu_jogador.local]['SOLVED'] = True
        limpar_tela()
        print_local()
        main_game_loop()
    else:
        print(Fore.RED +'Comando inválido.'+Style.RESET_ALL)
        locais()

######### cada monstro recebe seus atributos #########
monstro = lista_monstros_fixos[0]
monstro2 = lista_monstros_normais[1]
automato = lista_monstros_normais[10]
monstro1 = lista_monstros_fixos[1]
forjadora = lista_monstros_fixos[2]
cavaleiro = lista_monstros_semi_boss[0]
estatua_ossuario = lista_monstros_normais[9]
monstro_mimico = lista_monstros_semi_boss[1]
corvo = lista_monstros_semi_boss[2]
boss_raiva = lista_monstros_mascara[0]
boss_medo = lista_monstros_mascara[1]
boss_alegria = lista_monstros_mascara[2]
boss_loucura = lista_monstros_mascara[3]

efeito_boss = Efeito(lista_efeitos[1]['nome'], lista_efeitos[1]['tipo'], lista_efeitos[1]['tempo'], lista_efeitos[1]['dano'])
efeito_alegria = Efeito(lista_efeitos[0]['nome'], lista_efeitos[0]['tipo'], lista_efeitos[0]['tempo'], lista_efeitos[0]['dano'])
#######################################################

######################### NORMAIS #####################

estatua = Monstro(estatua_ossuario['nome'], estatua_ossuario['vida'], estatua_ossuario['nivel'], estatua_ossuario['atk'], estatua_ossuario['xp'], estatua_ossuario['ouro'], estatua_ossuario['boss'])
monstro_exemplo2 = Monstro(monstro2['nome'], monstro2['vida'], monstro2['nivel'], monstro2['atk'], monstro2['xp'], monstro2['ouro'], monstro2['boss'])
robot = Monstro(automato['nome'], automato['vida'], automato['nivel'], automato['atk'], automato['xp'], automato['ouro'], automato['boss'])

####################### SEMI BOSS ######################

cavaleiro_caido = Monstro(cavaleiro['nome'], cavaleiro['vida'], cavaleiro['nivel'], cavaleiro['atk'], cavaleiro['xp'], cavaleiro['ouro'], cavaleiro['boss'])
mimico = Monstro(monstro_mimico['nome'], monstro_mimico['vida'], monstro_mimico['nivel'], monstro_mimico['atk'], monstro_mimico['xp'], monstro_mimico['ouro'], monstro_mimico['boss'])
Crow_Mauler = Monstro(corvo['nome'], corvo['vida'], corvo['nivel'], corvo['atk'], corvo['xp'], corvo['ouro'], corvo['boss'])

########################################################

####################### BOSSES  ########################

forjadora_de_ossos = Monstro(forjadora['nome'], forjadora['vida'], forjadora['nivel'], forjadora['atk'], forjadora['xp'], forjadora['ouro'], forjadora['boss'])
guardiao_enraizado = Monstro(monstro['nome'], monstro['vida'], monstro['nivel'], monstro['atk'], monstro['xp'], monstro['ouro'], monstro['boss'], efeito_boss)
homunculo = Monstro(monstro1['nome'], monstro1['vida'], monstro1['nivel'], monstro1['atk'], monstro1['xp'], monstro1['ouro'], monstro1['boss'], efeito_boss)
Raiva = Monstro(boss_raiva['nome'], boss_raiva['vida'], boss_raiva['nivel'], boss_raiva['atk'], boss_raiva['xp'], boss_raiva['ouro'], boss_raiva['boss'], efeito_boss)
Medo = Monstro(boss_medo['nome'], boss_medo['vida'], boss_medo['nivel'], boss_medo['atk'], boss_medo['xp'], boss_medo['ouro'], boss_medo['boss'], efeito_boss)
Alegria = Monstro(boss_alegria['nome'], boss_alegria['vida'], boss_alegria['nivel'], boss_alegria['atk'], boss_alegria['xp'], boss_alegria['ouro'], boss_alegria['boss'], efeito_alegria)
Loucura = Monstro(boss_loucura['nome'], boss_loucura['vida'], boss_loucura['nivel'], boss_loucura['atk'], boss_loucura['xp'], boss_loucura['ouro'], boss_loucura['boss'], efeito_boss)

########################################################

####################### DROPS ##########################

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
    {'item': Item(lista_itens_bosses[10]['nome'], lista_itens_bosses[10]['atk'],
                 lista_itens_bosses[10]['desc'], lista_itens_bosses[10]['equipado'],
                 lista_itens_bosses[10]['consumivel'], lista_itens_bosses[10]['preco'],
                 lista_itens_bosses[10]['especial']),
     'chance': 0.6},   

]

homunculo.drops = [
    {'item': Item(lista_itens_bosses[2]['nome'], lista_itens_bosses[2]['atk'],
                 lista_itens_bosses[2]['desc'], lista_itens_bosses[2]['equipado'],
                 lista_itens_bosses[2]['consumivel'], lista_itens_bosses[2]['preco'],
                 lista_itens_bosses[2]['especial']),
     'chance': 1},  
    {'item': Item(lista_itens_bosses[11]['nome'], lista_itens_bosses[11]['atk'],
                 lista_itens_bosses[11]['desc'], lista_itens_bosses[11]['equipado'],
                 lista_itens_bosses[11]['consumivel'], lista_itens_bosses[11]['preco'],
                 lista_itens_bosses[11]['especial']),
     'chance': 0.6},  
     
    {'item': Armadura(lista_itens_bosses[3]['nome'], lista_itens_bosses[3]['defesa'],
                 lista_itens_bosses[3]['vida_max'], lista_itens_bosses[3]['resistencia'],
                 lista_itens_bosses[3]['desc'], False,
                 lista_itens_bosses[3]['consumivel'], lista_itens_bosses[3]['preco'],
                 lista_itens_bosses[3]['especial']),
     'chance': 0.3}, 
]

cavaleiro_caido.drops = [
    {'item': Armadura(lista_itens_bosses[4]['nome'], lista_itens_bosses[4]['defesa'],
                 lista_itens_bosses[4]['vida_max'], lista_itens_bosses[4]['resistencia'],
                 lista_itens_bosses[4]['desc'], False,
                 lista_itens_bosses[4]['consumivel'], lista_itens_bosses[4]['preco'],
                 lista_itens_bosses[4]['especial']),
     'chance': 0.5},

    {'item': Item(lista_itens_bosses[5]['nome'], lista_itens_bosses[5]['atk'],
                 lista_itens_bosses[5]['desc'], lista_itens_bosses[5]['equipado'],
                 lista_itens_bosses[5]['consumivel'], lista_itens_bosses[5]['preco'],
                 lista_itens_bosses[5]['especial']),
     'chance': 0.4},

    {'item': Item(lista_itens_bosses[6]['nome'], lista_itens_bosses[6]['atk'],
                 lista_itens_bosses[6]['desc'], lista_itens_bosses[6]['equipado'],
                 lista_itens_bosses[6]['consumivel'], lista_itens_bosses[6]['preco'],
                 lista_itens_bosses[6]['especial']),
     'chance': 0.3},
]

forjadora_de_ossos.drops = [
    {'item': Item(lista_itens_bosses[7]['nome'], lista_itens_bosses[7]['atk'],
                 lista_itens_bosses[7]['desc'], lista_itens_bosses[7]['equipado'],
                 lista_itens_bosses[7]['consumivel'], lista_itens_bosses[7]['preco'],
                 lista_itens_bosses[7]['especial']),
     'chance': 0.3},

    {'item': Armadura(lista_itens_bosses[8]['nome'], lista_itens_bosses[8]['defesa'],
                 lista_itens_bosses[8]['vida_max'], lista_itens_bosses[8]['resistencia'],
                 lista_itens_bosses[8]['desc'], False,
                 lista_itens_bosses[8]['consumivel'], lista_itens_bosses[8]['preco'],
                 lista_itens_bosses[8]['especial']),
     'chance': 0.3},

    {'item': Item(lista_itens_bosses[9]['nome'], lista_itens_bosses[9]['atk'],
                 lista_itens_bosses[9]['desc'], lista_itens_bosses[9]['equipado'],
                 lista_itens_bosses[9]['consumivel'], lista_itens_bosses[9]['preco'],
                 lista_itens_bosses[9]['especial']),
     'chance': 0.3},

]

mimico.drops = [

]

estatua.drops = [
    {'item': ArmaMagica(lista_itens_bosses[12]['dano_magico'], lista_itens_bosses[12]['nome'], 
                        lista_itens_bosses[12]['atk'], lista_itens_bosses[12]['desc'], 
                        lista_itens_bosses[12]['equipado'], lista_itens_bosses[12]['consumivel'],
                        lista_itens_bosses[12]['preco'], lista_itens_bosses[12]['especial']),
     'chance': 0.5},

    {'item': Item(lista_itens_bosses[13]['nome'], lista_itens_bosses[13]['atk'],
                 lista_itens_bosses[13]['desc'], lista_itens_bosses[13]['equipado'],
                 lista_itens_bosses[13]['consumivel'], lista_itens_bosses[13]['preco'],
                 lista_itens_bosses[13]['especial']),
     'chance': 0.5},
    {'item': Item(lista_itens_bosses[14]['nome'], lista_itens_bosses[14]['atk'],
                 lista_itens_bosses[14]['desc'], lista_itens_bosses[14]['equipado'],
                 lista_itens_bosses[14]['consumivel'], lista_itens_bosses[14]['preco'],
                 lista_itens_bosses[14]['especial']),
     'chance': 0.5},
     {'item': Armadura(lista_itens_bosses[15]['nome'], lista_itens_bosses[15]['defesa'],
                 lista_itens_bosses[15]['vida_max'], lista_itens_bosses[15]['resistencia'],
                 lista_itens_bosses[15]['desc'], False,
                 lista_itens_bosses[15]['consumivel'], lista_itens_bosses[15]['preco'],
                 lista_itens_bosses[15]['especial']),
     'chance': 0.5},

]

########################################################

######### navegção da Tela de título #########
def navegação_tela_titulo():
    opção = input(">>").lower()
    while opção not in ['jogar', 'ajuda', 'sair']:
        print(Fore.RED +"Por favor, utilize um comando válido."+Style.RESET_ALL)
        opção = input(Fore.LIGHTYELLOW_EX + ">>"+Style.RESET_ALL).lower()
    if opção == "jogar":
        setup_jogo()
    elif opção == "ajuda":
        ajuda_menu()
    elif opção == "sair":
        sair()


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
    'e1': False, 'e2': False,
    'f1': False, 'f2': False,
    'h1': False, 'h2': False,
    'i1': False, 'i2': False,
    'j1': False, 'j2': False,
}

mapa = {
    'a1': {
        'NOME_LOCAL': 'Sala do Trono ',
        'DESCRICAO': '''
Uma ampla e suntuosa sala se estende sob um teto alto ornamentado, onde lustres de cristal lançam brilhos dourados pelas paredes de mármore. 
      Ao centro, uma imponente mesa de ébano se ergue, polida como espelho, ladeada por cadeiras esculpidas com riqueza de detalhes. 
       Dominando o ambiente, um trono majestoso repousa ao fundo, elevado sobre degraus, símbolo absoluto de poder e autoridade..''',
        'EXAMINAR': '''
                          Tudo ao seu redor parece morto.
        Porem voce nota um brilho fraco vindo de frente de um trono destruido.
 Você tambem nota que consegue dormir naquele chão, não parece tão desconfortável assim.

(Para examinar o trono digite "trono". Digite "dormir" para recuperar vida e mana. Para sair de perto do trono digite "sair". digite dormir para descansar).
                    \n''',
        'SOLVED': False,
        'SUBIR': '',
        'DESCER': '',
        'AVANÇAR': 'a2',
        'RETORNAR': '',
        'MONSTRO': '',
        'LOCAIS': 'trono',
        'contador' : 0,
        'descansar': False
    },
    'a2': {
        'NOME_LOCAL': "Salão das Raízes Eternas",
        'DESCRICAO': '''
                            Um odor de terra úmida e carne podre invade seus sentidos. A sala adiante parece
                             uma antiga estufa esquecida, onde raízes negras tomaram os pilares de pedra...''',
        'EXAMINAR': '''
        No centro do local, uma árvore retorcida cresce a partir de um altar quebrado. 
        Seus galhos têm formas humanoides penduradas, como se absorvessem ecos de vida.
             Uma criatura feita de metade carne e metade madeira jaz ajoelhada, 
                    presa por correntes de prata, seus olhos fechados.

(para enfrentar o Guardião Enraizado, digite "enfrentar". Para sair de perto do Guardião digite "sair").
        \n''',
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
                    Ao entrar, o som desaparece. Nenhum eco. Nenhuma respiração. No lugar, apenas sussurros em sua mente
                                 vozes que carregam seu nome, mas ditas por pessoas que você não lembra.
''',
        'EXAMINAR': '''
                     As paredes são cobertas por máscaras penduradas, 
        cada uma com uma representação diferente sendo elas raiva, medo, alegria, loucura.
             Quando você se aproxima, elas viram lentamente... te observando.

(Digite raiva, medo, alegria ou loucura para ir até a máscara correspondente. Para sair de perto das máscaras digite "sair")\n''',
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
                                            Um poço escuro sussurra memórias esquecidas. 
                            Símbolos antigos cobrem as paredes úmidas, e o ar é carregado de nostalgia.
''',
        'EXAMINAR': '''
                        No centro de um salão de pedra úmida, há um poço negro como breu. 
        Correntes quebradas o rodeiam, e marcas de garras riscam o chão como se algo tivesse sido arrastado para fora.
                      Ao se aproximar, imagens distorcidas começam a surgir na água parada
                        são lembranças suas, mas... distorcidas, erradas, talvez falsas.
                                       No fundo do poço você vê um item. 

(Para pegar o item digite "pegar". Para sair de perto do poço digite "sair")\n''',
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
        'NOME_LOCAL': "O Corredor dos Autômatos Esquecidos",
        'DESCRICAO': '''
                                    O ar é denso, impregnado de poeira antiga que paira imóvel sob a penumbra. 
                    Ao longe, o rangido sutil de engrenagens abandonadas ressoa, como um sussurro mecânico perdido no tempo. 
                       Cada som parece ecoar na vastidão silenciosa, acentuando a sensação de desolação e esquecimento.
        \n''',
        'EXAMINAR': '''
                 Um corredor estreito com paredes de ferro corroído abriga autômatos enferrujados e imóveis. 
                              O ambiente é marcado por um enorme símbolo de uma engrenagem.
        Uma mensagem é escrita na parede "Derrame sangue no símbolo e acorde aqueles que não deveriam ser acordados."
                                    Deseja acordar um autômato? (Digite invocar)
                                    \n''',
        'SOLVED': True,
        'SUBIR': 'b2',
        'DESCER': '',
        'AVANÇAR': 'c2',
        'RETORNAR': '',
        'MONSTRO': '',
        'LOCAIS': 'invocar',
        'contador' : 0
    },
    'c2': {
        'NOME_LOCAL': "Oficina do Relógio Parado",
        'DESCRICAO': '''
                   Uma oficina vasta e esquecida se estende sob a penumbra, onde o metal frio domina cada canto. 
        Engrenagens enferrujadas, teimosas em sua função, ainda giram lentamente, rangendo como ecos de um passado industrial. 
                                O ar é espesso, saturado pelo odor de óleo velho e ferrugem.''',
        'EXAMINAR': '''
            Pêndulos partidos oscilam no teto, e no centro da sala há uma grande máquina quebrada com um rosto esculpido nela. 
                 O som das engrenagens forma palavras quase humanas. Um relógio gigante ao fundo gira ao contrário.
                     Um constructo quase completo permanesce a sua frente, apenas o seu núcleo está faltando.
        Ao olhar para a sua direita, há um corredor com paredes de ferro corroído e autômatos enferrujados, aparentemente desligados.
                                    Ao final deste corredor aparenta ter um báu de madeira.
                                    Deseja ir ao corredor ou Robo? (Digite corredor ou robo)
                                    \n''',
        'SOLVED': False,
        'SUBIR': '',
        'DESCER': 'd1',
        'AVANÇAR': '',
        'RETORNAR': 'c1',
        'MONSTRO': '',
        'LOCAIS': ['corredor', 'robo'],
        'contador' : 0,
        'contador2' : 0,
        'passagem' : True
    },
    'd1': {
        'NOME_LOCAL': "Câmara do Berço ao Abismo",
        'DESCRICAO': '''
           A sala pulsa com uma energia inquietante, como se o tempo ali fluísse ao contrário, desfazendo cada instante. 
        O ar vibra com uma força antinatural, dando a impressão de que algo invisível regressa incessantemente ao seu início. 
             Cada detalhe parece distorcido, como reflexo de uma realidade que se desfaz e se recompõe sem cessar.''',
        'EXAMINAR': '''
                         Uma gigantesca placenta fossilizada ocupa o centro. 
           Cordões umbilicais petrificados se ligam a pequenos altares dispostos em círculo.
Um círculo de sangue fresco é visível no chão, como se alguém tivesse realizado um ritual há pouco tempo.
              Deseja completar o ritual? (Digite completar ou sair para voltar)\n''',
        'SOLVED': True,
        'SUBIR': 'c2',
        'DESCER': '',
        'AVANÇAR': 'd2',
        'RETORNAR': '',
        'MONSTRO': '',
        'LOCAIS': 'completar',
        'contador' : 0,
        'contador2' : 0
    },
    'd2': {
        'NOME_LOCAL': "Laboratório dos Deformados",
        'DESCRICAO': '''
        Um fétido odor de carne putrefata e sangue seco impregna o ambiente, tornando o ar quase irrespirável. 
                  Cada respiração carrega consigo a promessa de decadência e morte iminente. 
              As paredes parecem absorver esse cheiro, como cicatrizes vivas de horrores passados.''',
        'EXAMINAR': '''
                            Frascos, fórmulas e instrumentos cirúrgicos cobrem as mesas. 
            No fundo da sala, tanques de vidro contêm corpos em decomposição. Alguns... ainda se movem.
             Um dos tanques de vidro é destruido e o cadaver dentro dele começa a se regenerar, é como 
                se a torre o tivesse despertado — um Homúnculo grotesco parado ao centro da sala.
                                    Digite atacar para atacar o Homúnculo.\n''',
        'SOLVED': False,
        'SUBIR': '',
        'DESCER': 'e1',
        'AVANÇAR': '',
        'RETORNAR': 'd1',
        'MONSTRO': '',
        'LOCAIS': 'atacar',
        'contador' : 0
    },
    'e1': {
        'NOME_LOCAL': "O Nódulo Desperto",
        'DESCRICAO': '''
         O ambiente pulsa, quente e úmido, enquanto sussurros quase imperceptíveis serpenteiam pelo ar denso. 
        Cada parede parece respirar lentamente, transmitindo a inquietante sensação de uma consciência oculta. 
                       Tudo ali vibra com uma vida própria, desconcertante e silenciosa.''',
        'EXAMINAR': '''
Um globo carnoso e pulsante, acorrentado ao teto por ganchos de prata. Ele murmura em uma voz múltiplàs vezes sussurrando, às vezes gritando.
                                                        "Você não devia ter voltado."
                        As paredes mostram símbolos pintados com sangue antigo. Você os reconhece… mas não sabe de onde. 
                                Deseja derramar sangue no simbolo e invocar um monstro? (Digite derramar)\n''',
        'SOLVED': True,
        'SUBIR': 'd1',
        'DESCER': '',
        'AVANÇAR': 'e2',
        'RETORNAR': '',
        'MONSTRO': '',
        'LOCAIS': 'invocar',
        'contador' : 0
    },
    'e2': {
        'NOME_LOCAL': "Loja dos Esquecidos",
        'DESCRICAO': '''
        Uma pequena loja escondida no fundo da torre. O vendedor, uma figura encapuzada, parece não se surpreender com sua presença.
                                   Nas prateleiras, itens estranhos brilham com energia mágica.
''',
        'EXAMINAR': '''
O vendedor sussurra: "Encontrei alguns tesouros nos corpos dos que falharam... interesse em algum?"
                        (Digite 'loja' para ver os itens à venda)\n''',
        'SOLVED': True,
        'SUBIR': '',
        'DESCER': 'f1',
        'AVANÇAR': '',
        'RETORNAR': 'e1',
        'MONSTRO': '',
        'LOCAIS': 'loja',
        'contador' : 0
    },
    'f1': {
        'NOME_LOCAL': "Galeria dos Pactos Perdidos",
        'DESCRICAO': '''
            Um corredor amplo se estende em silêncio, conduzindo até três quadros dispostos ao fundo como sentinelas silenciosas. 
        De cada moldura emana uma sombra pulsante, densa e irregular, que parece acompanhar com um olhar invisível quem ousa atravessar. 
                        A atmosfera é opressiva, como se o próprio espaço estivesse atento aos passos dados.''',
        'EXAMINAR': '''
                   Você se aproxima dos quadros, sentindo as sombras pulsantes intensificarem seus sussurros. Cada quadro exala uma presença distinta:
             O quadro da esquerda retrata uma figura musculosa, coberta de cicatrizes e erguendo uma espada quebrada. A sombra ao redor pulsa forte e agressiva.
            O quadro do centro mostra um ser encapuzado, de olhar enigmático, rodeado por símbolos arcanos indecifráveis. Sua sombra emana uma calma perturbadora.
O quadro da direita revela um guerreiro com o corpo perfurado por lanças, mas que ainda permanece de pé, encarando o horizonte com olhar inabalável. Sua sombra vibra com resistência.
                                        Deseja tocar em um dos quadros? (digite sim para tocar e não para voltar)\n''',
        'SOLVED': True,
        'SUBIR': 'e2',
        'DESCER': '',
        'AVANÇAR': 'f2',
        'RETORNAR': '',
        'MONSTRO': '',
        'LOCAIS': 'sim',
        'contador' : 0,
        'quadro' : False
    },
    'f2': {
        'NOME_LOCAL': "Salão da Coroa Quebrada",
        'DESCRICAO': '''
         Você adentra um salão vasto e silencioso, onde as colunas de pedra rachadas sustentam um teto coberto por raízes secas e pendentes como garras mortas.
No centro, um trono destroçado jaz tombado, e diante dele, uma figura permanece ajoelhada um cavaleiro envolto em uma armadura corroída e marcada por cicatrizes de batalhas antigas.
                        A lâmina ao seu lado está quebrada, mas sua presença exala uma fúria adormecida, como uma fogueira sufocada por cinzas.
                                             O ar é frio, pesado... e cada passo ecoa como um desafio lançado ao vazio.
''',
        'EXAMINAR': '''
                                          Você se aproxima cautelosamente da figura caída. 
Quando seus olhos se fixam na fenda do elmo, percebe um brilho espectral pulsando ali dentro, como um fragmento de alma incapaz de descansar.
           Antes que possa recuar, o cavaleiro ergue lentamente a cabeça, o metal rangendo com um som que mistura dor e ira. 
                                A mão se fecha com força sobre a empunhadura da lâmina quebrada.
                            Sem necessidade de palavras, você entende: não há como evitar a batalha.
                    A sombra do Cavaleiro Caído se ergue à sua frente, pronto para medir forças até o fim.

                                             Digite lutar para inicar o '''+Fore.RED+'''combate.'''+Style.RESET_ALL+'''\n''',
        'SOLVED': False,
        'SUBIR': '',
        'DESCER': 'g1',
        'AVANÇAR': '',
        'RETORNAR': 'f1',
        'MONSTRO': '',
        'LOCAIS': 'lutar',
        'contador' : 0
    },
    'g1': {
        'NOME_LOCAL': "Loja dos mercenários",
        'DESCRICAO': '''
            Uma pequena loja escondida no fundo da torre. O vendedor, uma figura encapuzada, parece não se surpreender com sua presença.
                                    Nas prateleiras, itens estranhos, espolios de guerras e dentre outros itens.
''',
        'EXAMINAR': '''
        O vendedor sussurra: "Encontrei alguns tesouros nos corpos dos que falharam... interesse em algum?"
                           (Digite 'loja' para ver os itens à venda)\n''',
        'SOLVED': True,
        'SUBIR': 'f2',
        'DESCER': '',
        'AVANÇAR': 'g2',
        'RETORNAR': '',
        'MONSTRO': '',
        'LOCAIS': 'loja',
        'contador' : 0
    },
    'g2': {
        'NOME_LOCAL': "O Coliseu dos Ecos Caídos",
        'DESCRICAO': '''
                Um coliseu em ruínas, com pilares estilhaçados e o chão enegrecido por cinzas, ossos e aço corroído.
        Cada pedra carrega o peso de batalhas esquecidas, enquanto o ar denso sussurra a memória de uma guerra que nunca terminou.
                                    O silêncio opressivo torna-se o prelúdio para o próximo massacre.
''',
        'EXAMINAR': '''
 Das sombras surge A Forjadora de Ossos, uma imensa guerreira vestida com a armadura dos mortos, erguendo sua marreta grotesca feita de ferro e ossos.
                                      Seus passos fazem o chão tremer, enquanto o eco metálico anuncia:
                                                    "Venha… e seja parte da minha forja!"
                                    Ela avança sem piedade, o olhar vazio e frio como a morte que carrega.''',

        'SOLVED': False,
        'SUBIR': '',
        'DESCER': 'h1',
        'AVANÇAR': '',
        'RETORNAR': 'g1',
        'MONSTRO': '',
        'LOCAIS': 'loja',
        'contador' : 0
    },
    'h1': {
        'NOME_LOCAL': "Ossuário",
        'DESCRICAO': '''
        Um salão onde milhares de ossos estão cuidadosamente empilhados, formando paredes e esculturas grotescas. 
                             O silêncio aqui não é natural; abafa até os pensamentos. \n''',
        'EXAMINAR': '''
    Ao seguir pelo Ossuário você vê uma estátua feita inteiramente de crânios parece segui-lo com o olhar.
             (Digite "invocar" para despertar o espírito do ossuário ou "sair" para recuar.) \n''',
        'SOLVED': True,
        'SUBIR': 'g2',
        'DESCER': '',
        'AVANÇAR': 'h2',
        'RETORNAR': '',
        'MONSTRO': '',
        'LOCAIS': 'invocar',
        'contador' : 0
    },
    'h2': {
        'NOME_LOCAL': "Câmara do Arquivista",
        'DESCRICAO': '''
                       Uma enorme biblioteca afundada, com livros podres e pergaminhos fossilizados. 
        No centro, uma figura esquelética presa a uma cadeira, seus olhos ainda vivos, lendo um livro interminável. ''',
        'EXAMINAR': '''
Olhando a sala você vê muitos livros empoerados e velhos, ao centro da sala jas um homem esquelético presa a uma cadeira.
                           Seus olhos ainda vivos, lendo um livro interminável.
                                Aquela figura olha para você e pergunta:
                            "Oh, caro aventureiro, deseja ouvir uma historia?"

                (Digite "ouvir" para ouvir a historia ou "sair" para continuar sua jornada)\n''',

        'SOLVED': True,
        'SUBIR': '',
        'DESCER': 'i1',
        'AVANÇAR': '',
        'RETORNAR': 'h1',
        'MONSTRO': '',
        'LOCAIS': 'ouvir',
        'contador' : 0,
        'historia' : False
    },
    'i1': {
        'NOME_LOCAL': "Salão Sintilante",
        'DESCRICAO': '''
 Um vasto espaço de pedras frias e lisas, onde nenhum som ecoa. As paredes são cobertas por tapeçarias antigas, desbotadas pelo tempo, 
          e uma névoa tênue paira constantemente sobre o chão. No centro, um único candelabro apagado balança levemente,
                                          como se movido por um vento que não existe. 
                  A atmosfera é opressora, fazendo com que quem entra sinta o peso do silêncio absoluto. ''',
        'EXAMINAR': ''' 
No centro da sala tem um baú com marcas de arranhões e algumas lascas de madeira pelo chão.
          Se aproximando do báu, você percebe que ele parece conter algo.
          
      (Digite "abrir" para abrir o báu ou "sair" para continuar sua jornada)\n''',

        'SOLVED': True,
        'SUBIR': 'h2',
        'DESCER': '',
        'AVANÇAR': 'i2',
        'RETORNAR': '',
        'MONSTRO': '',
        'LOCAIS': 'loja',
        'contador' : 0,
        'mimico' : False
    },
    'i2': {
        'NOME_LOCAL': "Salão do Descanso",
        'DESCRICAO': ''' 
        Um refúgio acolhedor, onde o tempo parece desacelerar e a atmosfera respira tranquilidade. 
             O salão é amplo, mas intimista, com luzes suaves que emitem um brilho âmbar, 
                 como se fossem velas tremulantes refletidas em cristais antigos.''',
        'EXAMINAR': ''' 
Os móveis são convidativos: poltronas e sofás macios, quase como nuvens, estofados em tecidos que variam entre veludo e linho, 
                              em cores que lembram café com leite e pêssegos maduros. 
                     Almofadas estrategicamente espalhadas completam o convite ao relaxamento, 
                     algumas com bordados delicados, outras em padrões geométricos discretos.

                (Digite "descansar" para curar toda a sua vida e mana, só pode ser usado uma vez)\n''',

        'SOLVED': True,
        'SUBIR': '',
        'DESCER': 'j1',
        'AVANÇAR': '',
        'RETORNAR': 'i1',
        'MONSTRO': '',
        'LOCAIS': 'descansar',
        'contador' : 0,
        'descansar' : False
    },
    'j1': {
        'NOME_LOCAL': "Whaterfall",
        'DESCRICAO': '''
                     Uma caverna imponente se abre em meio às trevas, formada por pedras negras que absorvem a luz e 
                    pequenas gemas brancas cintilantes incrustadas nas paredes. A combinação cria um espetáculo etéreo, 
        fazendo com que o teto da caverna se assemelhe a um céu noturno salpicado de estrelas. Cada passo ecoa sob essa abóbada silenciosa, 
                                            como se caminhando sob um firmamento subterrâneo.''',
        'EXAMINAR': '''
                                    hOI!
                               boas-vinds a...
                                LOJA TEM!!!

                    (Digite "loja" pa comprar com TEM!!!)
"''',

        'SOLVED': True,
        'SUBIR': 'i2',
        'DESCER': '',
        'AVANÇAR': 'j2',
        'RETORNAR': '',
        'MONSTRO': '',
        'LOCAIS': 'loja',
        'contador' : 0
    },
    'j2': {
        'NOME_LOCAL': "O Começo",
        'DESCRICAO': '''
        O primeiro andar é uma sala ampla de pedra negra, iluminada apenas por raios de luz fraca que atravessam frestas nas paredes.
                  O ar é pesado, com cheiro de mofo e metal enferrujado. Marcas de garras profundas riscam as paredes, 
                             e fragmentos de uma armadura quebrada estão espalhados pelo chão.''',

        'EXAMINAR': ''' 
        No centro, uma imponente estátua de pedra ergue-se, com um semblante enigmático.
             No rosto dela, há um encaixe perfeitamente moldado para uma máscara.
                    Ao se aproximar, uma voz sussurra na sua mente:
                         "Você deseja encaixar a máscara?"

            (Para encaixar a máscara digite encaixar, para sair digite sair)\n''',

        'SOLVED': False,
        'SUBIR': '',
        'DESCER': '',
        'AVANÇAR': '',
        'RETORNAR': 'j1',
        'MONSTRO': '',
        'LOCAIS': 'encaixar',
        'contador' : 0,
        'contador2': 0,
        'boss_final' : False
    },
}

def mostrar_mapa():
    if meu_jogador.local == 'a1':
        limpar_tela()
        print('▬'*100)
        print('Mapa:')
        print(r''' 
                    ██
                  ██████
                ████  ████
              ████      ████
            ████          ████
            ██████████████████
            ██  \●/ ██      ██
            ██   |  ██      ██  Você está na primeira sala do 10º andar.
            ██  / \ ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
''')
    elif meu_jogador.local == 'a2':
        limpar_tela()
        print('Mapa:')
        print(r''' 
                    ██
                  ██████
                ████  ████
              ████      ████
            ████          ████
            ██████████████████
            ██      ██ \●/  ██
            ██      ██  |   ██  Você está na segunda sala do 10º andar.
            ██      ██ / \  ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
''')
    elif meu_jogador.local == 'b1':
        limpar_tela()
        print('Mapa:')
        print(r''' 
                    ██
                  ██████
                ████  ████
              ████      ████
            ████          ████
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██  \●/ ██      ██
            ██   |  ██      ██  Você está na primeira sala do 9º andar.
            ██  / \ ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
''')
    elif meu_jogador.local == 'b2':
        limpar_tela()
        print('Mapa:')
        print(r''' 
                    ██
                  ██████
                ████  ████
              ████      ████
            ████          ████
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██ \●/  ██
            ██      ██  |   ██  Você está na segunda sala do 9º andar.
            ██      ██ / \  ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
''')
    elif meu_jogador.local == 'c1':
        limpar_tela()
        print('Mapa:')
        print(r''' 
                    ██
                  ██████
                ████  ████
              ████      ████
            ████          ████
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██  \●/ ██      ██
            ██   |  ██      ██  Você está na primeira sala do 8º andar.
            ██  / \ ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
''')
    elif meu_jogador.local == 'c2':
        limpar_tela()
        print('Mapa:')
        print(r''' 
                    ██
                  ██████
                ████  ████
              ████      ████
            ████          ████
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██ \●/  ██
            ██      ██  |   ██  Você está na segunda sala do 8º andar.
            ██      ██ / \  ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
''')
    elif meu_jogador.local == 'd1':
        limpar_tela()
        print('Mapa:')
        print(r''' 
                    ██
                  ██████
                ████  ████
              ████      ████
            ████          ████
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██  \●/ ██      ██
            ██   |  ██      ██  Voce está na primeira sala do 7º andar.
            ██  / \ ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
''')
    elif meu_jogador.local == 'd2':
        limpar_tela()
        print('Mapa:')
        print(r''' 
                    ██
                  ██████
                ████  ████
              ████      ████
            ████          ████
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██ \●/  ██
            ██      ██  |   ██  Voce está na segunda sala do 7º andar.
            ██      ██ / \  ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
''')
    elif meu_jogador.local == 'e1':
        limpar_tela()
        print('Mapa:')
        print(r''' 
                    ██
                  ██████
                ████  ████
              ████      ████
            ████          ████
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██  \●/ ██      ██
            ██   |  ██      ██  Voce está na primeira sala do 6º andar.
            ██  / \ ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
''')
    elif meu_jogador.local == 'e2':
        limpar_tela()
        print('Mapa:')
        print(r''' 
                    ██
                  ██████
                ████  ████
              ████      ████
            ████          ████
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██ \●/  ██
            ██      ██  |   ██  Voce está na segunda sala do 6º andar.
            ██      ██ / \  ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
''')
    elif meu_jogador.local == 'f1':
        limpar_tela()
        print('Mapa:')
        print(r''' 
                    ██
                  ██████
                ████  ████
              ████      ████
            ████          ████
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██  \●/ ██      ██
            ██   |  ██      ██  Voce está na primeira sala do 5º andar.
            ██  / \ ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
              ''')
    elif meu_jogador.local == 'f2':
        limpar_tela()
        print('Mapa:')
        print(r''' 
                    ██
                  ██████
                ████  ████
              ████      ████
            ████          ████
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██ \●/  ██
            ██      ██  |   ██  Voce está na segunda sala do 5º andar.
            ██      ██ / \  ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
''')
    elif meu_jogador.local == 'g1':
        limpar_tela()
        print('Mapa:')
        print(r''' 
                    ██
                  ██████
                ████  ████
              ████      ████
            ████          ████
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██  \●/ ██      ██
            ██   |  ██      ██  Voce está na primeira sala do 4º andar.
            ██  / \ ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
              ''')
    elif meu_jogador.local == 'g2':
        limpar_tela()
        print('Mapa:')
        print(r''' 
                    ██
                  ██████
                ████  ████
              ████      ████
            ████          ████
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██ \●/  ██
            ██      ██  |   ██  Voce está na segunda sala do 4º andar.
            ██      ██ / \  ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
''')
    elif meu_jogador.local == 'h1':
        limpar_tela()
        print('Mapa:')
        print(r''' 
                    ██
                  ██████
                ████  ████
              ████      ████
            ████          ████
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██  \●/ ██      ██
            ██   |  ██      ██   Voce está na primeira sala do 3º andar.
            ██  / \ ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
              ''')
    elif meu_jogador.local == 'h2':
        limpar_tela()
        print('Mapa:')
        print(r''' 
                    ██
                  ██████
                ████  ████
              ████      ████
            ████          ████
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██ \●/  ██
            ██      ██  |   ██  Voce está na segunda sala do 3º andar.
            ██      ██ / \  ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
''')
    elif meu_jogador.local == 'i1':
        limpar_tela()
        print('Mapa:')
        print(r''' 
                    ██
                  ██████
                ████  ████
              ████      ████
            ████          ████
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██  \●/ ██      ██
            ██   |  ██      ██  Voce está na primeira sala do 2º andar.
            ██  / \ ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
              ''')
    elif meu_jogador.local == 'i2':
        limpar_tela()
        print('Mapa:')
        print(r''' 
                    ██
                  ██████
                ████  ████
              ████      ████
            ████          ████
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██ \●/  ██
            ██      ██  |   ██  Voce está na segunda sala do 2º andar.
            ██      ██ / \  ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
''')
    elif meu_jogador.local == 'j1':
        limpar_tela()
        print('Mapa:')
        print(r''' 
                    ██
                  ██████
                ████  ████
              ████      ████
            ████          ████
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██  \●/ ██      ██
            ██   |  ██      ██  Voce está na primeira sala do 1º andar.
            ██  / \ ██      ██
            ██████████████████
              ''')
    elif meu_jogador.local == 'j2':
        limpar_tela()
        print('Mapa:')
        print(r''' 
                    ██
                  ██████
                ████  ████
              ████      ████
            ████          ████
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██      ██
            ██      ██      ██
            ██      ██      ██
            ██████████████████
            ██      ██ \●/  ██
            ██      ██  |   ██  Voce está na segunda sala do 1º andar.
            ██      ██ / \  ██
            ██████████████████
''')

##### Interações em jogo #####
def print_local():
    limpar_tela()
    local_nome = mapa[meu_jogador.local]['NOME_LOCAL']
    local_desc = mapa[meu_jogador.local]['DESCRICAO']
    print('\n' + '▄'*130 + Fore.MAGENTA + f''' 
                       
                                                        {local_nome.upper()}

                                {local_desc}'''+ '\n' + Style.RESET_ALL+ Fore.CYAN+'''
Principais Comandos: [mover / olhar / mochila / status / mapa]\n'''+Style.RESET_ALL)

    print('▄' * 130)

    mostrar_status(meu_jogador)
    if mapa[meu_jogador.local]['MONSTRO'] != '':
        print(f"há um" + Fore.RED + f" {mapa[meu_jogador.local]['MONSTRO'].nome}" + Style.RESET_ALL + " na sala. O que deseja fazer?" + Fore.YELLOW + "\n[lutar / fugir]")
        escolha = input(Fore.YELLOW + ">>"+Style.RESET_ALL).lower()
        if escolha not in ['lutar', 'fugir']:
            print_local()
        acao_luta(escolha, mapa[meu_jogador.local]['MONSTRO'])
    main_game_loop()

def prompt():
    print("\n" + "▬"*100)
    print(Fore.LIGHTYELLOW_EX + "O que deseja fazer?"+Style.RESET_ALL)
    acao = input(Fore.LIGHTYELLOW_EX +">>"+Style.RESET_ALL).lower()
    acoes_aceitas = ['status', 'mover', 'loja', 'sair', 'ajuda', 'olhar', 'inspecionar', 'teleportar', 'dormir', 'mochila', 'mapa']
    while acao not in acoes_aceitas:
        print(Fore.RED + "Ação inválida, tente novamente.\n")
        acao = input(Fore.YELLOW +">> "+Style.RESET_ALL).lower()
    if acao == 'sair':
        sair()
    if acao == 'mover':
        jogador_mover()
    elif acao == 'teleportar':
        meu_jogador.local = 'j2'
        arma_bolada = lista_arma_ik[0]
        meu_jogador.add_item(Item(
            arma_bolada['nome'], 
            arma_bolada['atk'], 
            arma_bolada['desc'], 
            False, 
            arma_bolada['consumivel'], 
            arma_bolada['preco'], 
            arma_bolada['especial']
        ))
        print_local()
        main_game_loop()
    elif acao == 'ajuda':
        ajuda_menu()
    elif acao in ['olhar', 'inspecionar']:
        jogador_examinar()
    elif acao == 'dormir':
        jogador_dormir()
    elif acao == 'mochila' and acao != 'sair':
        abrir_mochila()
    elif acao == 'status':
        exibir_status(meu_jogador)
    elif acao == 'mapa':
        mostrar_mapa()
        input(Fore.LIGHTYELLOW_EX +'[Pressione enter]'+Style.RESET_ALL).lower()
        limpar_tela()
        print_local()

def locais():
    print(Fore.LIGHTYELLOW_EX + 'O que deseja fazer?' + Style.RESET_ALL)
    acao = input(Fore.LIGHTYELLOW_EX +'>>'+Style.RESET_ALL).lower()
    acoes_aceitas = mapa[meu_jogador.local]['LOCAIS'],'encaixar','dormir', 'derramar','raiva','medo','alegria','loucura', 'sair', 'pegar', 'invocar', 'robo', 'corredor', 'completar', 'atacar', 'loja', 'sim', 'lutar', 'ouvir', 'abrir', 'descansar', 'encaixar'
    
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
    elif acao == 'invocar':
        encontro_aleatorio()
    elif acao == 'robo':
        robo()
    elif acao == 'corredor':
        corredor()       
    elif acao == 'completar':
        ritual()
    elif acao == 'atacar' :
        boss_homunculo()
    elif acao == 'derramar':
        invocacao()
    elif acao == 'sim':
        quadros()
    elif acao == 'ouvir':
        historia()
    elif meu_jogador.local in ['e2', 'g1'] and acao == 'loja':
        loja_e2()
    elif acao == 'lutar':
        semi_boss_cavaleiro()
    elif acao == 'abrir':
        mimico_monstro()
    elif acao == 'descansar':
        descansar()
    elif acao == 'dormir':
        descansar_a1()
    elif acao == 'encaixar':
        ultimo_boss()
    else:
        print('Acao inválida, tente novamente.')
        locais()



### Objetos interativos dos andares ###

def trono():
    print('▬'*100)
    if meu_jogador.local == 'a1' and mapa[meu_jogador.local]['SOLVED'] == False:
        fala1 ='''
                            Você vai até o brilho e vê um anel dourado.
                           ao toca-lo um frio intenso percorre seu braço.
        Seu dedo o aceita sem resistência, como se ele sentisse que voce era o seu Dono.\n'''
        for fala in fala1:
            sys.stdout.write(fala)
            sys.stdout.flush()
            time.sleep(0.01)
        item = lista_itens_especiais[0]
        meu_jogador.add_item(Item(item['nome'], item['atk'], item['desc'], item['equipado'], item['consumivel'], item['preco'], item['especial']))
        fala2 = Fore.YELLOW + '\nAnel desconhecido adicionado ao seu inventario!\n' + Style.RESET_ALL
        for fala in fala2:
            sys.stdout.write(fala)
            sys.stdout.flush()
            time.sleep(0.01)
        input(Fore.YELLOW+'[Pressione Enter]'+Style.RESET_ALL)
        print('\n', '▬'*100)
        mapa[meu_jogador.local]['SOLVED'] = True
        limpar_tela()
        print_local()
        main_game_loop()
    elif meu_jogador.local == 'a1' and mapa[meu_jogador.local]['SOLVED'] == True:
        fala3 = 'Não há mais nada no trono.'
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
            lutar = 'Quando você se aproxima…'+Fore.RED+' ela desperta.\n'+Style.RESET_ALL
            for fala in lutar:
                sys.stdout.write(fala)
                sys.stdout.flush()
                time.sleep(0.01)
            input(Fore.YELLOW+'[Pressione Enter]'+Style.RESET_ALL)
            limpar_tela()
            luta(guardiao_enraizado, meu_jogador)        
    elif meu_jogador.local == 'a2' and mapa[meu_jogador.local]['SOLVED'] == True:
        fala1 = Fore.LIGHTYELLOW_EX+'O monstro está caido morto bem a sua frente.\n'+Style.RESET_ALL
        for fala in fala1:
            sys.stdout.write(fala)
            sys.stdout.flush()
            time.sleep(0.01)
        input(Fore.YELLOW+'[Pressione Enter]'+Style.RESET_ALL)
        limpar_tela()
        main_game_loop()
    else:
        print(Fore.RED + 'Comando inválido.'+Style.RESET_ALL)
        main_game_loop()

def boss_homunculo():
    if meu_jogador.local == 'd2':
        if mapa[meu_jogador.local]['SOLVED'] == False:
            lutar = 'Você ataca o homunculo e inicia um combate'
            for fala in lutar:
                sys.stdout.write(fala)
                sys.stdout.flush()
                time.sleep(0.01)
            input(Fore.YELLOW+'[Pressione Enter]'+Style.RESET_ALL)
            limpar_tela()
            luta(homunculo, meu_jogador) 
    elif meu_jogador.local == 'd2' and mapa['d2']['SOLVED'] == True:
        fala1 = Fore.LIGHTYELLOW_EX+'O Homunculo parou de se mexer.'+Style.RESET_ALL
        for fala in fala1:
            sys.stdout.write(fala)
            sys.stdout.flush()
            time.sleep(0.01)
        input(Fore.YELLOW+'[Pressione Enter]'+Style.RESET_ALL)
        limpar_tela()
        main_game_loop()
    else:
        print(Fore.RED + 'Comando inválido.'+Style.RESET_ALL)
        main_game_loop()

def semi_boss_cavaleiro():
    if meu_jogador.local == 'f2':
        if mapa[meu_jogador.local]['SOLVED'] == False:
            lutar = 'Você encara o cavaleiro de frente e inicia um combate.'
            for fala in lutar:
                sys.stdout.write(fala)
                sys.stdout.flush()
                time.sleep(0.01)
            input(Fore.YELLOW+'[Pressione Enter]'+Style.RESET_ALL)
            limpar_tela()
            luta(cavaleiro_caido, meu_jogador)
    elif meu_jogador.local == 'f2' and mapa['f2']['SOLVED'] == True:
        fala1 = Fore.LIGHTYELLOW_EX+'O Cavaleiro está no chão, nenhum sinal de vida é encontrado no corpo.'+Style.RESET_ALL
        for fala in fala1:
            sys.stdout.write(fala)
            sys.stdout.flush()
            time.sleep(0.01)
        input(Fore.YELLOW+'[Pressione Enter]'+Style.RESET_ALL)
        limpar_tela()
        main_game_loop()
    else:
        print(Fore.RED + 'Comando inválido.'+Style.RESET_ALL)
        main_game_loop()

def robo():
    """
    Função que lida com a interação com o robô no local 'c2'.
    """
    # Verificação inicial da mochila
    if not hasattr(meu_jogador, 'mochila') or not isinstance(meu_jogador.mochila, list):
        print(Fore.RED + "Erro: Mochila inválida!" + Style.RESET_ALL)
        time.sleep(1)
        return

    nucleo_no_inventario = None
    
    # Procura pelo núcleo no inventário de forma segura
    for item in meu_jogador.mochila:
        try:
            # Comparação case-insensitive e removendo espaços extras
            if hasattr(item, 'nome') and item.nome.lower().strip() == 'núcleo de robo':
                nucleo_no_inventario = item
                break
        except Exception:
            continue  # Ignora itens problemáticos

    if nucleo_no_inventario:
        try:
            mapa['c2']['SOLVED'] = True
            
            # Animação de texto
            fala = 'Você usa o Núcleo de Robo para tentar restaurar o robô.'
            for char in fala:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.02)
            
            # Remove o núcleo do inventário
            meu_jogador.mochila.remove(nucleo_no_inventario)
            
            aleatorio = random.randint(1, 100)
            if aleatorio >= 0:  # Sucesso na restauração
                # Animação de texto
                fala2 = '\nO robô se restaura com um brilho azul nos olhos.'
                for char in fala2:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.02)
                
                time.sleep(1.5)
                
                fala3 = '\nEle emite sons mecânicos e abre um compartimento, oferecendo um item.'
                for char in fala3:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.02)
                
                time.sleep(1.5)
                
                # Lista de possíveis itens que o robô pode dar
                itens_robo = [
                    lista_armaduras[1],  # Armadura média
                    lista_consumiveis[3],  # Poção de mana
                    lista_itens_especiais[5],  # Núcleo de Robô (para reparar outro)
                    lista_armas[1]  # Espada longa
                ]
                
                # Escolhe um item aleatório
                item_data = random.choice(itens_robo)
                
                # Cria o objeto apropriado
                if 'defesa' in item_data:  # Se for armadura
                    item = Armadura(
                        item_data['nome'], 
                        item_data['defesa'],
                        item_data['vida_max'],
                        item_data['resistencia'],
                        item_data['desc'],
                        False,  # Não equipado automaticamente
                        item_data['consumivel'],
                        item_data['preco'],
                        item_data['especial']
                    )
                else:  # Se for item normal
                    item = Item(
                        item_data['nome'],
                        item_data.get('atk', 0),
                        item_data['desc'],
                        False,  # Não equipado
                        item_data['consumivel'],
                        item_data['preco'],
                        item_data['especial']
                    )
                
                print(f'\n\nO robô te dá: {Fore.YELLOW}{item.nome}{Style.RESET_ALL}!')
                print(f'Descrição: {item.desc}')
                
                # Adiciona o item à mochila
                meu_jogador.add_item(item)
                
                print('\n[equipar | guardar]')
                escolha = input(Fore.YELLOW+'>> '+Style.RESET_ALL).lower()
                
                if escolha == 'equipar':
                    if isinstance(item, Armadura):
                        # Desequipa armadura atual se houver
                        if meu_jogador.armadura:
                            meu_jogador.armadura.equipado = False
                        # Equipa a nova
                        meu_jogador.armadura = item
                        item.equipado = True
                        print(f'Você equipou a armadura {item.nome}!')
                    elif hasattr(item, 'atk'):  # Se for arma
                        # Desequipa arma atual se houver
                        if meu_jogador.item_equipado:
                            meu_jogador.item_equipado.equipado = False
                        # Equipa a nova
                        meu_jogador.item_equipado = item
                        item.equipado = True
                        print(f'Você equipou {item.nome}!')
                    else:
                        print('Este item não pode ser equipado.')
                
                time.sleep(1.5)
                
            else:  # Falha na restauração
                fala4 = '\nO robô se restaura, mas com olhos vermelhos!'
                for char in fala4:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.02)
                
                time.sleep(1.5)
                
                fala5 = Fore.RED+'\nSinais de alerta piscam e ele te ataca!'+Style.RESET_ALL
                for char in fala5:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.02)
                
                input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)
                luta(robot, meu_jogador)
                
        except Exception as e:
            print(Fore.RED + f"\nErro ao interagir com o robô: {e}" + Style.RESET_ALL)
            time.sleep(2)
    else:
        print(Fore.RED + '\nVocê não tem o Núcleo de Robo no inventário.' + Style.RESET_ALL)
    
    time.sleep(1.5)
    limpar_tela()
    print_local()
    main_game_loop()
    
def corredor():
    if meu_jogador.local == 'c2':
        item = lista_itens_especiais[5]
        if mapa['c2']['passagem'] == True:
            if mapa['c2']['contador2'] == 0:
                fala1 = 'Você adentra o corredor e passa por vários automatos desligados, '+Fore.RED+'porém um deles aparenta se mexer e te ataca.'+Style.RESET_ALL
                for fala in fala1:
                    sys.stdout.write(fala)
                    sys.stdout.flush()
                    time.sleep(0.02)
                input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)
                limpar_tela()
                luta(robot, meu_jogador)
            elif meu_jogador.vida > 0:
                fala2 = '''
                Você derrotou o automato e continua pelo corredor.
                Você chega no final do corredor e encontra um baú.'''
                for fala in fala2:
                    sys.stdout.write(fala)
                    sys.stdout.flush()
                    time.sleep(0.02)
                escolha = input('Deseja abrir o baú? [s/n]\n>> ')
                if escolha == 's':
                    fala3 = 'O baú abre e revela um '+Fore.GREEN+'item.'+Style.RESET_ALL
                    for fala in fala3:
                        sys.stdout.write(fala)
                        sys.stdout.flush()
                        time.sleep(0.02)
                    mapa['c2']['passagem'] = False
                    meu_jogador.add_item(Item(item['nome'], item['atk'], item['desc'], item['equipado'], item['consumivel'], item['preco'], item['especial']))
                    input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)
                    limpar_tela()
                    print_local()
                    main_game_loop()          
                if escolha == 'n':
                    fala4 = 'Você volta para o centro da sala.'
                    for fala in fala4:
                        sys.stdout.write(fala)
                        sys.stdout.flush()
                        time.sleep(0.02)
                    input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)
                    limpar_tela()
                    print_local()
                    main_game_loop()
        elif mapa['c2']['passagem'] == False:
            fala5 ='Voce ja pegou o que estava no bau.'
            for fala in fala5:
                sys.stdout.write(fala)
                sys.stdout.flush()
                time.sleep(0.02)
            time.sleep(1.5)
            limpar_tela()
            print_local()
            main_game_loop()
    else:
        print(Fore.RED+'Comando inválido.'+Style.RESET_ALL)
        time.sleep(1.5)
        limpar_tela()
        print_local()
        main_game_loop()

def pegar():
    item = lista_armas_especiais[0]
    item2 = lista_armas_especiais[1]
    item3 = lista_armas_especiais[2]
    if meu_jogador.local == 'b2' and mapa['b2']['contador2'] == 0:
        if meu_jogador.classe == 'monge':
            meu_jogador.add_item(Item(item['nome'], item['atk'], item['desc'], item['equipado'], item['consumivel'], item['preco'], item['especial']))
            mapa['b2']['contador2'] += 1
            fala_monge = "Você se lembra da arma que usava antes, colocando a mão dentro do poço você a pega e agora ela está na sua mao.\n"+Fore.YELLOW+f"\n{item['nome']} Adicionado ao seu inventário.\n"+Style.RESET_ALL
            for fala in fala_monge:
                sys.stdout.write(fala)
                sys.stdout.flush()
                time.sleep(0.01)
            input(Fore.YELLOW+'[Pressione Enter]'+Style.RESET_ALL)
            limpar_tela()
            print_local()
            main_game_loop()
        elif meu_jogador.classe == 'guerreiro':
            meu_jogador.add_item(Item(item2['nome'], item2['atk'], item2['desc'], item2['equipado'], item2['consumivel'], item2['preco'], item2['especial']))
            mapa['b2']['contador2'] += 1
            fala_guerreiro = Fore.YELLOW+"Você se lembra da arma que usava antes, colocando a mão dentro do poço você a pega e agora ela está na sua mao.\n"+Fore.YELLOW+f"\n{item2['nome']} Adicionado ao seu inventário."+Style.RESET_ALL
            for fala in fala_guerreiro:
                sys.stdout.write(fala)
                sys.stdout.flush()
                time.sleep(0.01)
            input(Fore.YELLOW+'[Pressione Enter]'+Style.RESET_ALL)
            limpar_tela()
            print_local()
            main_game_loop()
        elif meu_jogador.classe == 'mago':
            meu_jogador.add_item(Item(item3['nome'], item3['atk'], item3['desc'], item3['equipado'], item3['consumivel'], item3['preco'], item3['especial']))
            mapa['b2']['contador2'] += 1
            fala_mago = Fore.YELLOW+"Você se lembra da arma que usava antes, colocando a mão dentro do poço você a pega e agora ela está na sua mao.\n"+Fore.YELLOW+f"\n{item3['nome']} Adicionado ao seu inventário."+Style.RESET_ALL
            for fala in fala_mago:
                sys.stdout.write(fala)
                sys.stdout.flush()
                time.sleep(0.01)
            input(Fore.YELLOW+'[Pressione Enter]'+Style.RESET_ALL)
            limpar_tela()
            print_local()
            main_game_loop()
    else:
        print(Fore.RED+'Comando inválido.'+Style.RESET_ALL)
        locais()

def ritual():
    if meu_jogador.local == 'd1' and mapa['d1']['contador2'] < 3:
        aleatorio = random.randint(1,3)
        if aleatorio == 1:
            mapa['d1']['contador2'] += 1
            fala1 = 'Você executa o ritual com sucesso e ganha '+Fore.GREEN+'1 lvl'+Style.RESET_ALL
            meu_jogador.xp += meu_jogador.xp_max
            subi_nivel(meu_jogador)
            time.sleep(1.5)
            limpar_tela()
            print_local()
            main_game_loop()
        else:
            mapa['d1']['contador2'] += 1
            fal2 = 'O ritual falhou e você perdeu '+Fore.RED+'10 de vida.'+Style.RESET_ALL
            for fala in fal2:
                sys.stdout.write(fala)
                sys.stdout.flush()
                time.sleep(0.02)
            meu_jogador.vida -= 10
            if meu_jogador.vida <= 0:
                meu_jogador.game_over = True
            input(Fore.YELLOW+'[Pressione Enter]'+Style.RESET_ALL)
            limpar_tela()
            print_local()
            main_game_loop()
    elif meu_jogador.local == 'd1' and mapa['d1']['contador2'] >= 3:
        fala3 ='Você exedeu o número de rituais que pode executar.'
        for fala in fala3:
            sys.stdout.write(fala)
            sys.stdout.flush()
            time.sleep(0.02)
        input(Fore.YELLOW+'[Pressione Enter]'+Style.RESET_ALL)
        limpar_tela()
        print_local()
        main_game_loop()
    else:
        print(Fore.RED+'Comando inválido.'+Style.RESET_ALL)
        locais()

def quadros():
    if mapa[meu_jogador.local]['quadro'] == False and meu_jogador.local == 'f1':
        escolha = input('''
                        Em qual quadro deseja tocar?

    [1] quadro da esquerda.
    [2] quadro do centro.
    [3] quadro da direita.
    '''+Fore.YELLOW+'''\n>>'''+Style.RESET_ALL)
        for caractere in escolha:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.001)
        if escolha == '1':
            forca = 'Ao tocar a figura musculosa, sente uma descarga de energia percorrer seus braços. Sua '+Fore.GREEN+'Força'+Style.RESET_ALL+' aumenta.'
            meu_jogador.forca += 2
            for caractere in forca:
                sys.stdout.write(caractere)
                sys.stdout.flush()
                time.sleep(0.02)
            input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)
            mapa['f1']['quadro'] = True
            atualizar_atributos(meu_jogador)
            limpar_tela()
            print_local()
            main_game_loop()
        elif escolha == '2':
            inteligencia = ' Ao repousar a mão sobre os símbolos arcanos, uma onda de compreensão obscurecida atravessa sua mente. Sua '+Fore.BLUE+'Inteligência'+Style.RESET_ALL+' aumenta.'
            meu_jogador.inteligencia += 2
            for caractere in inteligencia:
                sys.stdout.write(caractere)
                sys.stdout.flush()
                time.sleep(0.02)
            input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)
            mapa['f1']['quadro'] = True
            atualizar_atributos(meu_jogador)
            limpar_tela()
            print_local()
            main_game_loop()
        elif escolha == '3':
            fortitude = 'Ao encostar na imagem do guerreiro ferido, um frio cortante envolve seu corpo, seguido de uma resistência silenciosa. Sua '+Fore.RED+'Fortitude'+Style.RESET_ALL+' aumenta.'
            meu_jogador.fortitude += 2
            for caractere in fortitude:
                sys.stdout.write(caractere)
                sys.stdout.flush()
                time.sleep(0.02)
            input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)
            mapa['f1']['quadro'] = True
            atualizar_atributos(meu_jogador)
            limpar_tela()
            print_local()
            main_game_loop()
    elif mapa[meu_jogador.local]['quadro'] == True and meu_jogador.local == 'f1':
        quadro = 'Você já escolheu um quadro.'
        for caractere in quadro:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.02)
        input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)
        limpar_tela()
        print_local()
        main_game_loop()
    else:
        print(Fore.RED+'Comando inválido.'+Style.RESET_ALL)
        locais()

def historia():
    if meu_jogador.local == 'h2' and mapa['h2']['historia'] == False:
        historia = ''' 
(Em voz rouca e pausada, o velho sábio começa a contar:)

     “Há muito, muito tempo… erguia-se uma torre de dez andares, mais alta que qualquer montanha, mais antiga que qualquer reino.
        No topo dessa torre, reinava um Lorde sombrio, mestre e carcereiro de criaturas que nem os pesadelos ousavam desenhar.
 Mas então… um herói apareceu. Corajoso, puro… e forte. Subiu andar por andar, espada em punho, varrendo a escuridão com a luz de sua alma.
                                  Monstros caíram, horrores se desfizeram… até restar apenas ele: o Lorde.
  Ah… mas o Lorde era astuto. No seu suspiro final, proferiu um feitiço terrível: apagou a memória do herói e arrancou-lhe todos os dons.
    Agora… perdido, frágil e sem nome… o herói desperta no topo da torre, olhando para o abismo de onde veio, sem saber sequer quem é. 
            E para recuperar sua identidade… ele terá que descer, enfrentar novamente as criaturas que esqueceu ter vencido… 
                                         e, quem sabe, lembrar… quem foi… e quem ainda pode ser.”

(O velho sorri, fecha os olhos… o velho senhor não se mexe mais, após o conto o senhor faleceu concluindo seu objetivo, deixando a história pairar no ar.)
'''

        for caractere in historia:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.1)
        input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)
        limpar_tela()
        print_local()
        main_game_loop()
    elif meu_jogador.local == 'h2' and mapa['h2']['historia'] == True:
        fala = 'O velho sábio está morto.'
        for caractere in fala:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.02)
        input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)
        limpar_tela()
        print_local()
        main_game_loop()
    else:
        print(Fore.RED+'Comando inválido.'+Style.RESET_ALL)
        locais()

def mimico_monstro():
    if meu_jogador.local == 'i1' and mapa['i1']['mimico'] == False:
        mapa['i1']['mimico'] = True
        fala = 'Você encosta no baú para abrilo e ele se revela sendo um mímico. A criatura de morde causando '+Fore.RED+'20 de dano.'+Style.RESET_ALL
        meu_jogador.vida -= 20
        for caractere in fala:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.02)
        time.sleep(1.5)
        print(Fore.RED+r'''

                        ############                                                        
                    #####+++##############                                                
                   ####++#-+++#+##################                                        
                  ####++++#+###+##+###+##+##################                              
                 ####+++###--#+##+#+#+######++########+++##########                       
                ####+-+# ##+--+######+##-###+##+#+###++#+####################             
                ###+-#   ###+-+################+###++#++###+#++++#+##########             
             ####+-+#     ###--+#######################++#+##+#+##+##########             
            #######        ##+-++################+++#####+++##++##+##+###++##             
           ########         #####+#######################+#++##+++##+++###++#             
          ##+#####          ##++#++################################++++####++             
         ##++-##           #####---+##############################+-+#######+             
        ##+--+#           ######+++-+############+################+++#######++            
       ##++--+#          #######++#+++####+#####++++#############+++########+#            
     ####+-.--##        ###########++#####+####++###++#########++++####### ##+#           
    #####+++#--#       +#################+#####+###++##########++######### ###+#          
  #######.-  #-+      ###+#+#+###########+######+++++##########++########   ##++          
 ###++##+-  ##+       #####+#+##+++######+####+##++++###################     #+##         
 ###++ #-+####       ####################+####+#++++#+##################    ##+++##       
 ++###  ##             ##################++###++++++#+###+#++#+##+#######  ####+--+#      
 #####   ##             #################++###-+++#+###+#####+#+#++######+ ###+++-+#+     
    ##    ##              ###############++###++++#+############+###### ## #-+###+--++    
     #                       #############++##-+++####################           #+#+#+   
                                    ######+###+++++###################           #++++#   
                                    ######+####++++#################             ####+#   
                                    ######+###+++######  ##########               #+    
                                     #####+###+++#                                  
                                     #####+###+++#                               
                                     #####+##+++#                                    
                                     #####++#+++#                                  
                                     #####+++++##                                  
                                     ######++++#                                  
                                     ###+#+-++##                                 
                                    ###+##+-+##                               
                                   ####+#++-##                              
                                   ###+#+--##                             
                                  ###+++--+#                                  
                                 ###+#+--##                          
                                ###+++-+#                            
                                ####++#                           
                                  ####           
                   '''+Style.RESET_ALL)
        input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)
        limpar_tela()
        luta(mimico, meu_jogador)
    else:
        print(Fore.RED+'Comando inválido.'+Style.RESET_ALL)
        locais()

def descansar():
    if meu_jogador.local == 'i2' and mapa['i2']['descansar'] == False:
        aleatorio = random.randint(1, 100)
        if aleatorio <= 20:
            fala2 = 'Enquanto você dormia, um homem com cabeça de corvo e uma arma no lugar de seu braço te ataca.'
            meu_jogador.vida -= 100
            for caractere in fala2:
                sys.stdout.write(caractere)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1.5)
            print(r'''\n
                ########        ########                                        
               #######++++################                                      
                  #########+++##############                                    
                       #########+###+-+######                                   
                          #################                                     
                            #####+##########                                    
                          ######++###########                                   
                         ######++###########                                    
                         ####+###############                                   
                       #+######+-+##########++##                                
                      #+#+##+++--##########+--+##                               
                    ######+---++##########++-+++####                            
                         +-------+++++++#--++----+-##                           
                        #+---------------+-+++---++++#                          
                        #++++------------++++++---+--+                          
                        #-++-----------+++####+-+-+++#                          
                        --+#+-----------++-++##++++--++                         
                        --++#+----++--+-++++####------+                         
                       ++-+++-----+++++-+++### #+---+-+#                        
                      ##-++++-++--++++++-++#    #+--++++#                       
                      #++#+------------++##      #+--+#+#                       
                     #+--+--------++++++####      #+++++##                      
                    ##+--+++++---+++++++###        ########                     
                   +---++##+--+--++++-+#++###       #########                   
                   ----+###+-----+++###++####       ######+##                   
                  #----+###+++++++##++-+++####      #####+++##                  
                  +--++###+-----+++---+++++###         #+#++####                
                  +--+####+----------+++#######       #####++++#                
                 #+-+####++-------++++##+++####          ###++##                
                 #+++####+--------+###++++#####           ##+++#++#             
                ##--+###+-----+-----+++++++###             ##+++###             
               ##+---+##+--++-+++++++++++++###             ##++#+####           
              #+--++-+#+++-++-++++++++++++++####           ####+#++###          
              #+++##++#+++++++++++++++++++++###               #++#+#####        
              ##++##+++++++++++++++++++++++++##              #++###+++#         
              ##++##+++++++++++++++++##++++#####                ###++##         
               ######+++++++++++#++++##+++++####                #+##+++##       
                 ####+++++++++++#+++++##++++#####                ##++++##       
                   ##+++++++++++##++++##+++++#####               #++++++###     
                  ##++++++++++++##+++++#++++++####               ####+++++#     
                  ##++++-+++-+++##+++++##++#+++#####               ##+++++#     
                  #+++++-+++-+++##+++++##++##++######               #++#++###   
                  #++++--+++++++#++++++##++##+++######            ##++##+++##   
                 ##++++--++++++##+++++++#+++##+++######            ######+++##  
                 ##++++-+++++++#++++++++++++##++++#####                #++####  
                 ##++++-+++++++##+#+++++++++###+++#####                #+##+##  
                 ##++#+-++++++++++#++++++++++###+++####                #######  
                  #++#+++++++++++###+++++#+++####++++##                         
                   +++++###++++++###+++++##+++####+++-+#                        
                   #-+-++##++##+#####+++++########----+#                        
                   #++--###          ##          #+----+#                       
               #   #++++###         ######         +--++##                      
                 ##++++##############################+-+####                    
            +++++------++############################+---++######               
          ###++--+++###+#############################+-+--+++#####              
          ###############         #############################       ''')
            input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)
            limpar_tela()
            luta(Crow_Mauler, meu_jogador)
        fala = 'Você se deitou no sofá e recuperou toda a sua vida e mana.'
        meu_jogador.vida = meu_jogador.vida_max
        meu_jogador.mana = meu_jogador.mana_max
        for caractere in fala:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.01)
        input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)
        limpar_tela()
        print_local()
        main_game_loop()
    else:
        print(Fore.RED+'Comando inválido.'+Style.RESET_ALL)
        locais()
def descansar_a1():
    if meu_jogador.local == 'a1' and mapa['a1']['descansar'] == False:
        aleatorio = random.randint(1, 100)
        if aleatorio <= 3:
            fala2 = 'Enquanto você descansava, um homem com cabeça de corvo e uma arma no lugar de seu braço te ataca.'
            meu_jogador.vida -= 100
            for caractere in fala2:
                sys.stdout.write(caractere)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1.5)
            print(r'''\n
                ########        ########                                        
               #######++++################                                      
                  #########+++##############                                    
                       #########+###+-+######                                   
                          #################                                     
                            #####+##########                                    
                          ######++###########                                   
                         ######++###########                                    
                         ####+###############                                   
                       #+######+-+##########++##                                
                      #+#+##+++--##########+--+##                               
                    ######+---++##########++-+++####                            
                         +-------+++++++#--++----+-##                           
                        #+---------------+-+++---++++#                          
                        #++++------------++++++---+--+                          
                        #-++-----------+++####+-+-+++#                          
                        --+#+-----------++-++##++++--++                         
                        --++#+----++--+-++++####------+                         
                       ++-+++-----+++++-+++### #+---+-+#                        
                      ##-++++-++--++++++-++#    #+--++++#                       
                      #++#+------------++##      #+--+#+#                       
                     #+--+--------++++++####      #+++++##                      
                    ##+--+++++---+++++++###        ########                     
                   +---++##+--+--++++-+#++###       #########                   
                   ----+###+-----+++###++####       ######+##                   
                  #----+###+++++++##++-+++####      #####+++##                  
                  +--++###+-----+++---+++++###         #+#++####                
                  +--+####+----------+++#######       #####++++#                
                 #+-+####++-------++++##+++####          ###++##                
                 #+++####+--------+###++++#####           ##+++#++#             
                ##--+###+-----+-----+++++++###             ##+++###             
               ##+---+##+--++-+++++++++++++###             ##++#+####           
              #+--++-+#+++-++-++++++++++++++####           ####+#++###          
              #+++##++#+++++++++++++++++++++###               #++#+#####        
              ##++##+++++++++++++++++++++++++##              #++###+++#         
              ##++##+++++++++++++++++##++++#####                ###++##         
               ######+++++++++++#++++##+++++####                #+##+++##       
                 ####+++++++++++#+++++##++++#####                ##++++##       
                   ##+++++++++++##++++##+++++#####               #++++++###     
                  ##++++++++++++##+++++#++++++####               ####+++++#     
                  ##++++-+++-+++##+++++##++#+++#####               ##+++++#     
                  #+++++-+++-+++##+++++##++##++######               #++#++###   
                  #++++--+++++++#++++++##++##+++######            ##++##+++##   
                 ##++++--++++++##+++++++#+++##+++######            ######+++##  
                 ##++++-+++++++#++++++++++++##++++#####                #++####  
                 ##++++-+++++++##+#+++++++++###+++#####                #+##+##  
                 ##++#+-++++++++++#++++++++++###+++####                #######  
                  #++#+++++++++++###+++++#+++####++++##                         
                   +++++###++++++###+++++##+++####+++-+#                        
                   #-+-++##++##+#####+++++########----+#                        
                   #++--###          ##          #+----+#                       
               #   #++++###         ######         +--++##                      
                 ##++++##############################+-+####                    
            +++++------++############################+---++######               
          ###++--+++###+#############################+-+--+++#####              
          ###############         #############################       ''')
            input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)
            limpar_tela()
            luta(Crow_Mauler, meu_jogador)
        fala = 'Você se deitou no chão e descansou bastante, vida e mana recuperados.'
        meu_jogador.vida = meu_jogador.vida_max
        meu_jogador.mana = meu_jogador.mana_max
        for caractere in fala:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.01)
        input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)
        limpar_tela()
        print_local()
        main_game_loop()
    else:
        print(Fore.RED+'Comando inválido.'+Style.RESET_ALL)
        locais()

def ultimo_boss():
    if meu_jogador.local == 'j2' and not mapa['j2']['boss_final']:
        mapa['j2']['contador2'] = 1
        
        # Verifica se o jogador tem alguma máscara no inventário de forma segura
        mascaras_no_inventario = []
        for item in meu_jogador.mochila:
            try:
                if hasattr(item, 'nome') and item.nome in ["Máscara da Raiva", "Máscara do Medo", 
                                                        "Máscara da Alegria", "Máscara da Loucura"]:
                    mascaras_no_inventario.append(item)
            except AttributeError:
                continue  # Ignora itens que não têm o atributo 'nome'

        if not mascaras_no_inventario:
            fala = "Você não possui nenhuma máscara para encaixar."
            for caractere in fala:
                sys.stdout.write(caractere)
                sys.stdout.flush()
                time.sleep(0.02)
            input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)
            limpar_tela()
            print_local()
            main_game_loop()
            return
            
        # Mostra as máscaras disponíveis
        fala2 = "Qual máscara você deseja encaixar?"
        for caractere in fala2:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.02)
            
        for i, mascara in enumerate(mascaras_no_inventario, 1):
            print(Fore.YELLOW+f"[{i}]"+Style.RESET_ALL+f" {mascara.nome}")
            
        escolha = input(Fore.YELLOW+"\n>> "+Style.RESET_ALL)
        
        try:
            escolha = int(escolha) - 1
            if escolha < 0 or escolha >= len(mascaras_no_inventario):
                raise ValueError
                
            mascara_escolhida = mascaras_no_inventario[escolha]
            
            # Remove a máscara do inventário com verificação
            try:
                meu_jogador.mochila.remove(mascara_escolhida)
            except ValueError:
                print("Erro: Máscara não encontrada na mochila!")
                time.sleep(1)
                limpar_tela()
                print_local()
                main_game_loop()
                return
            
            # Determina qual boss enfrentar baseado na máscara
            if mascara_escolhida.nome == "Máscara da Raiva":
                monstro = Raiva
            elif mascara_escolhida.nome == "Máscara do Medo":
                monstro = Medo
            elif mascara_escolhida.nome == "Máscara da Alegria":
                monstro = Alegria
            else:  # Máscara da Loucura
                monstro = Loucura
            
            # Animação de ativação
            fala3 = f"\nVocê encaixa a {mascara_escolhida.nome} na estátua..."
            for caractere in fala3:
                sys.stdout.write(caractere)
                sys.stdout.flush()
                time.sleep(0.02)
            
            time.sleep(1.5)
            
            fala4 = "A estátua começa a tremer e se transforma em uma criatura horrível!"
            for caractere in fala4:
                sys.stdout.write(caractere)
                sys.stdout.flush()
                time.sleep(0.02)
            
            input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)
            limpar_tela()
            
            # Inicia a batalha
            luta(monstro, meu_jogador)
            
            # Marca como resolvido se o jogador vencer
            mapa['j2']['boss_final'] = True
            
        except (ValueError, IndexError):
            print("Escolha inválida.")
            time.sleep(1)
            limpar_tela()
            print_local()
            main_game_loop()
            
    elif meu_jogador.local == 'j2' and mapa['j2']['boss_final']:
        print("A estátua está inerte, você já enfrentou o desafio aqui.")
        time.sleep(1.5)
        limpar_tela()
        print_local()
        main_game_loop()
    else:
        print(Fore.RED + 'Comando inválido.' + Style.RESET_ALL)
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
        limpar_tela()
        sys.exit()
    else:
        if meu_jogador.nome == '':
            tela_titulo()
        main_game_loop()

def acao_luta(escolha, monstro):
    if escolha == 'lutar':
        luta(monstro, meu_jogador)
    elif escolha == 'fugir':
        fugir()

def abrir_mochila():
    if meu_jogador.game_over:
        main_game_loop()
    
    if not meu_jogador.mochila:
        print(Fore.RED + "Mochila vazia" + Style.RESET_ALL)
        input(Fore.LIGHTYELLOW_EX + "\n[Pressione enter para voltar]" + Style.RESET_ALL)
        print_local()
        main_game_loop()
    
    limpar_tela()
    print("▬" * 50)
    print(Fore.YELLOW + "                   MOCHILA" + Style.RESET_ALL)
    print("▬" * 50)
    
    # Mostra ouro
    print(f'Ouro: {Fore.YELLOW}{meu_jogador.ouro}{Style.RESET_ALL}\n')
    
    # Lista para manter a ordem dos itens exibidos
    itens_exibidos = []
    contador_global = 1
    
    # Organiza itens por tipo
    armas = []
    armaduras = []
    consumiveis = []
    especiais = []
    
    for item in meu_jogador.mochila:
        if not hasattr(item, 'consumivel') or not hasattr(item, 'especial'):
            print(f"Item inválido na mochila: {item}")
            continue  # Pula para o próximo item
    
        if item.consumivel:
            consumiveis.append(item)
        elif item.especial:
            especiais.append(item)
        elif isinstance(item, Armadura):
            armaduras.append(item)
        else:
            armas.append(item)
    
    # Mostra seção de armas
    if armas:
        print(Fore.LIGHTRED_EX + "ARMAS:" + Style.RESET_ALL)
        for arma in armas:
            equipado = "(EQUIPADO)" if arma.equipado else ""
            if arma.dano_magico:
                print(f'{Fore.YELLOW}[{contador_global}]{Style.RESET_ALL} {arma.nome} | DANO MÁGICO: {arma.dano_magico} | {arma.desc} {equipado}')
            else:
                print(f'{Fore.YELLOW}[{contador_global}]{Style.RESET_ALL} {arma.nome} | ATK: {arma.atk} | {arma.desc} {equipado}')
            itens_exibidos.append(arma)
            contador_global += 1
        print()
    
    # Mostra seção de armaduras
    if armaduras:
        print(Fore.LIGHTBLUE_EX + "ARMADURAS:" + Style.RESET_ALL)
        for armadura in armaduras:
            equipado = "(EQUIPADO)" if armadura.equipado else ""
            print(f'{Fore.YELLOW}[{contador_global}]{Style.RESET_ALL} {armadura.nome} | DEF: {armadura.defesa} | VIDA: {armadura.vida_max} | RES: {armadura.resistencia}% | {armadura.desc} {equipado}')
            itens_exibidos.append(armadura)
            contador_global += 1
        print()
    
    # Mostra seção de consumíveis
    if consumiveis:
        print(Fore.LIGHTGREEN_EX + "CONSUMÍVEIS:" + Style.RESET_ALL)
        for consumivel in consumiveis:
            print(f'{Fore.YELLOW}[{contador_global}]{Style.RESET_ALL} {consumivel.nome} | {consumivel.desc}')
            itens_exibidos.append(consumivel)
            contador_global += 1
        print()
    
    # Mostra seção de itens especiais
    if especiais:
        print(Fore.MAGENTA + "ITENS ESPECIAIS:" + Style.RESET_ALL)
        for especial in especiais:
            print(f'{Fore.YELLOW}[{contador_global}]{Style.RESET_ALL} {especial.nome} | {especial.desc}')
            itens_exibidos.append(especial)
            contador_global += 1
        print()
    
    print("▬" * 50)
    print("Use os números para selecionar um item ou digite:")
    print(Fore.LIGHTYELLOW_EX + "[fechar]" + Style.RESET_ALL + " - Voltar ao jogo")
    print(Fore.LIGHTYELLOW_EX + "[organizar]" + Style.RESET_ALL + " - Reorganizar mochila")
    print(Fore.LIGHTYELLOW_EX + "[loja]" + Style.RESET_ALL + " - Vender itens")
    
    escolha = input(Fore.LIGHTYELLOW_EX + "\n>> " + Style.RESET_ALL).lower()
    
    if escolha == "fechar":
        limpar_tela()
        print_local()
        main_game_loop()
    elif escolha == "organizar":
        reorganizar_mochila()
    elif escolha == "loja":
        vender_item()
    else:
        try:
            escolha = int(escolha) - 1
            if escolha < 0 or escolha >= len(itens_exibidos):
                print(Fore.RED + "Item inválido!" + Style.RESET_ALL)
                time.sleep(1)
                abrir_mochila()
            
            item_selecionado = itens_exibidos[escolha]
            limpar_tela()
            print("▬" * 50)
            
            # Mostra informações detalhadas do item
            if isinstance(item_selecionado, Armadura):
                print(f"{Fore.LIGHTBLUE_EX}ARMADURA SELECIONADA:{Style.RESET_ALL}")
                print(f"Nome: {item_selecionado.nome}")
                print(f"Defesa: {item_selecionado.defesa}")
                print(f"Vida: {item_selecionado.vida_max}")
                print(f"Resistência: {item_selecionado.resistencia}%")
                print(f"Descrição: {item_selecionado.desc}")
                
                if item_selecionado.equipado:
                    print("\nEsta armadura está equipada")
                    print(Fore.LIGHTYELLOW_EX + "\n[desequipar] " + Style.RESET_ALL + "- Desequipar esta armadura")
                else:
                    if meu_jogador.armadura:
                        print(f"\nVocê já está equipado com: {meu_jogador.armadura.nome}")
                        print(Fore.LIGHTYELLOW_EX + "[equipar] " + Style.RESET_ALL + "- Substituir armadura atual")
                    else:
                        print(Fore.LIGHTYELLOW_EX + "\n[equipar] " + Style.RESET_ALL + "- Equipar esta armadura")
                
                print(Fore.LIGHTYELLOW_EX + "[voltar] " + Style.RESET_ALL + "- Voltar para a mochila")
                print(Fore.RED + "[descarte] " + Style.RESET_ALL + "- Descartar item permanentemente")
                
            elif item_selecionado.consumivel:
                print(f"{Fore.LIGHTGREEN_EX}CONSUMÍVEL SELECIONADO:{Style.RESET_ALL}")
                print(f"Nome: {item_selecionado.nome}")
                print(f"Descrição: {item_selecionado.desc}")
                
                print(Fore.LIGHTYELLOW_EX + "\n[usar] " + Style.RESET_ALL + "- Usar item agora")
                print(Fore.LIGHTYELLOW_EX + "[voltar] " + Style.RESET_ALL + "- Voltar para a mochila")
                print(Fore.RED + "[descarte] " + Style.RESET_ALL + "- Descartar item permanentemente")
            
            elif item_selecionado.especial:
                print(f"{Fore.MAGENTA}ITEM ESPECIAL SELECIONADO:{Style.RESET_ALL}")
                print(f"Nome: {item_selecionado.nome}")
                print(f"Descrição: {item_selecionado.desc}")
                
                print(Fore.LIGHTYELLOW_EX + "\n[voltar] " + Style.RESET_ALL + "- Voltar para a mochila")
                # Itens especiais não podem ser descartados
                
            else:  # Assume que é arma
                print(f"{Fore.LIGHTRED_EX}ARMA SELECIONADA:{Style.RESET_ALL}")
                print(f"Nome: {item_selecionado.nome}")
                print(f"Ataque: {item_selecionado.atk}")
                print(f"Descrição: {item_selecionado.desc}")
                
                if item_selecionado.equipado:
                    print("\nEsta arma está equipada")
                    print(Fore.LIGHTYELLOW_EX + "\n[desequipar] " + Style.RESET_ALL + "- Desequipar esta arma")
                else:
                    if meu_jogador.item_equipado:
                        print(f"\nVocê já está equipado com: {meu_jogador.item_equipado.nome}")
                        print(Fore.LIGHTYELLOW_EX + "[equipar] " + Style.RESET_ALL + "- Substituir arma atual")
                    else:
                        print(Fore.LIGHTYELLOW_EX + "\n[equipar] " + Style.RESET_ALL + "- Equipar esta arma")
                
                print(Fore.LIGHTYELLOW_EX + "[voltar] " + Style.RESET_ALL + "- Voltar para a mochila")
                print(Fore.RED + "[descarte] " + Style.RESET_ALL + "- Descartar item permanentemente")
            
            print("▬" * 50)
            acao = input(Fore.LIGHTYELLOW_EX + ">> " + Style.RESET_ALL).lower()
            
            # Processa a ação selecionada
            if acao == "voltar":
                abrir_mochila()
            
            elif acao == "equipar" and (not item_selecionado.consumivel and not item_selecionado.especial):
                if isinstance(item_selecionado, Armadura):
                    # Desequipa armadura atual se houver
                    if meu_jogador.armadura:
                        meu_jogador.armadura.equipado = False
                    
                    # Equipa nova armadura
                    meu_jogador.armadura = item_selecionado
                    item_selecionado.equipado = True
                    atualizar_atributos(meu_jogador)
                    print(f"\n{Fore.GREEN}Você equipou {item_selecionado.nome}!{Style.RESET_ALL}")
                    time.sleep(1)
                
                else:  # Equipar arma
                    # Desequipa arma atual se houver
                    if meu_jogador.item_equipado:
                        meu_jogador.item_equipado.equipado = False
                    
                    # Equipa nova arma
                    meu_jogador.item_equipado = item_selecionado
                    item_selecionado.equipado = True
                    atualizar_atributos(meu_jogador)
                    print(f"\n{Fore.GREEN}Você equipou {item_selecionado.nome}!{Style.RESET_ALL}")
                    time.sleep(1)
                
                abrir_mochila()
            
            elif acao == "desequipar" and (not item_selecionado.consumivel or not item_selecionado.especial) and (meu_jogador.item_equipado or meu_jogador.armadura):
                if isinstance(item_selecionado, Armadura):
                    if meu_jogador.armadura and (item_selecionado.nome == meu_jogador.armadura.nome):
                        meu_jogador.armadura = None
                elif isinstance(item_selecionado, Item):
                    if meu_jogador.item_equipado and (item_selecionado.nome == meu_jogador.item_equipado.nome):
                        meu_jogador.item_equipado = None
                else:
                    print('ação inválida')
                
                item_selecionado.equipado = False
                atualizar_atributos(meu_jogador)
                print(f"\n{Fore.YELLOW}Você desequipou {item_selecionado.nome}!{Style.RESET_ALL}")
                time.sleep(1)
                abrir_mochila()
            
            elif acao == "usar" and item_selecionado.consumivel:
                if item_selecionado.nome == 'Poção de Vida Lendária':
                    pocao_vida_lendaria()
                elif item_selecionado.nome == 'Poção de Mana Lendária':
                    pocao_mana_lendaria()

                elif item_selecionado.nome == 'Pocao de vida baixa':
                    pocao_vida()
                elif item_selecionado.nome == 'Pocao de vida media':
                    pocao_vida_media()
                elif item_selecionado.nome == 'Pocao de vida alta':
                    pocao_vida_alta()
                elif item_selecionado.nome == 'Pocao de mana baixa':
                    pocao_mana()
                elif item_selecionado.nome == 'Pocao de mana media':
                    pocao_mana_media()
                elif item_selecionado.nome == 'Pocao de mana alta':
                    pocao_mana_alta()
                elif item_selecionado.nome == 'Carne de Homunculo':
                    carne_homunculo()
                elif item_selecionado.nome == 'Flocos de TEM':
                    flocos_de_tem()
                elif item_selecionado.nome == 'Erva de Mana':
                    pocao_erva_de_mana()
                elif item_selecionado.nome == 'Pergaminho do Apocalipse':
                    usar_pergaminho_apocalipse()
                elif item_selecionado.nome == 'Pergaminho do Estilhaço Sísmico':
                    usar_pergaminho_estilhaço_sismico()
                elif item_selecionado.nome == 'Pergaminho da Absorção de Sangue':
                    usar_pergaminho_absorcao()
                elif item_selecionado.nome == 'Pergaminho das Raizes da Morte':
                    usar_pergaminho_raizes()
                elif item_selecionado.nome == 'Pergaminho do Cometa Pedrilhante':
                    usar_pergaminho_cometa_pedrilhante()
                # Remove o item usado
                meu_jogador.mochila.remove(item_selecionado)
                time.sleep(1)
                abrir_mochila()
            
            elif acao == "descarte" and not item_selecionado.especial:
                confirmar = input(f"\nTem certeza que deseja descartar {item_selecionado.nome}? (s/n): ").lower()
                if confirmar == 's':
                    if item_selecionado.equipado:
                        if isinstance(item_selecionado, Armadura):
                            meu_jogador.armadura = None
                        else:
                            meu_jogador.item_equipado = None
                    
                    meu_jogador.mochila.remove(item_selecionado)
                    print(f"\n{Fore.RED}Você descartou {item_selecionado.nome}!{Style.RESET_ALL}")
                    time.sleep(1)
                abrir_mochila()
            
            else:
                print(Fore.RED + "\nAção inválida!" + Style.RESET_ALL)
                time.sleep(1)
                abrir_mochila()
        
        except ValueError:
            print(Fore.RED + "\nEntrada inválida!" + Style.RESET_ALL)
            time.sleep(1)
            abrir_mochila()

def reorganizar_mochila():
    limpar_tela()
    print("▬" * 50)
    print(Fore.YELLOW + "   REORGANIZAR MOCHILA" + Style.RESET_ALL)
    print("▬" * 50)
    print("Escolha como organizar seus itens:")
    print(Fore.LIGHTYELLOW_EX + "[1]" + Style.RESET_ALL + " - Por tipo (armas, armaduras, consumíveis)")
    print(Fore.LIGHTYELLOW_EX + "[2]" + Style.RESET_ALL + " - Por nome (A-Z)")
    print(Fore.LIGHTYELLOW_EX + "[3]" + Style.RESET_ALL + " - Por valor (mais caro primeiro)")
    print(Fore.LIGHTYELLOW_EX + "[voltar]" + Style.RESET_ALL + " - Voltar para a mochila")
    
    opcao = input(Fore.LIGHTYELLOW_EX + "\n>> " + Style.RESET_ALL).lower()
    
    if opcao == "voltar":
        abrir_mochila()
    elif opcao == "1":
        # Já está organizado por tipo por padrão
        print("\n" + Fore.GREEN + "Itens organizados por tipo!" + Style.RESET_ALL)
        time.sleep(1)
        abrir_mochila()
    elif opcao == "2":
        meu_jogador.mochila.sort(key=lambda x: x.nome)
        print("\n" + Fore.GREEN + "Itens organizados por nome (A-Z)!" + Style.RESET_ALL)
        time.sleep(1)
        abrir_mochila()
    elif opcao == "3":
        meu_jogador.mochila.sort(key=lambda x: x.preco, reverse=True)
        print("\n" + Fore.GREEN + "Itens organizados por valor (mais caro primeiro)!" + Style.RESET_ALL)
        time.sleep(1)
        abrir_mochila()
    else:
        print(Fore.RED + "\nOpção inválida!" + Style.RESET_ALL)
        time.sleep(1)
        reorganizar_mochila()

def vender_item():
    limpar_tela()
    print("▬" * 50)
    print(Fore.YELLOW + "   VENDER ITENS" + Style.RESET_ALL)
    print("▬" * 50)
    
    # Filtra itens que podem ser vendidos (não especiais e não equipados)
    itens_vendaveis = [item for item in meu_jogador.mochila 
                      if not item.especial and not item.equipado]
    
    if not itens_vendaveis:
        print(Fore.RED + "Nenhum item vendável na mochila!" + Style.RESET_ALL)
        print("Itens equipados ou especiais não podem ser vendidos.")
        print("\n" + "▬" * 50)
        input(Fore.LIGHTYELLOW_EX + "\n[Pressione enter para voltar]" + Style.RESET_ALL)
        abrir_mochila()
    
    # Mostra itens vendáveis
    for i, item in enumerate(itens_vendaveis, 1):
        print(f'{Fore.YELLOW}[{i}]{Style.RESET_ALL} {item.nome} | Valor: {item.preco} | {item.desc}')
    
    print("\n" + "▬" * 50)
    print("Use os números para selecionar um item para vender ou digite:")
    print(Fore.LIGHTYELLOW_EX + "[voltar]" + Style.RESET_ALL + " - Voltar para a mochila")
    print(Fore.LIGHTYELLOW_EX + "[vender tudo]" + Style.RESET_ALL + " - Vender todos os itens vendáveis")
    
    escolha = input(Fore.LIGHTYELLOW_EX + "\n>> " + Style.RESET_ALL).lower()
    
    if escolha == "voltar":
        abrir_mochila()
    elif escolha == "vender tudo":
        total = sum(item.preco for item in itens_vendaveis)
        confirmar = input(f"\nVender TODOS os itens por {total} de ouro? (s/n): ").lower()
        if confirmar == 's':
            for item in itens_vendaveis:
                meu_jogador.mochila.remove(item)
            meu_jogador.ouro += total
            print(f"\n{Fore.GREEN}Você vendeu todos os itens por {total} de ouro!{Style.RESET_ALL}")
            time.sleep(1.5)
        vender_item()
    else:
        try:
            escolha = int(escolha) - 1
            if escolha < 0 or escolha >= len(itens_vendaveis):
                print(Fore.RED + "Item inválido!" + Style.RESET_ALL)
                time.sleep(1)
                vender_item()
            
            item_selecionado = itens_vendaveis[escolha]
            confirmar = input(f"\nVender {item_selecionado.nome} por {item_selecionado.preco} de ouro? (s/n): ").lower()
            
            if confirmar == 's':
                meu_jogador.mochila.remove(item_selecionado)
                meu_jogador.ouro += item_selecionado.preco
                print(f"\n{Fore.GREEN}Você vendeu {item_selecionado.nome} por {item_selecionado.preco} de ouro!{Style.RESET_ALL}")
                time.sleep(1)
            vender_item()
        
        except ValueError:
            print(Fore.RED + "\nEntrada inválida!" + Style.RESET_ALL)
            time.sleep(1)
            vender_item()

def loja_e2():
    if meu_jogador.local not in ['e2', 'g1', 'j1']:
        print(Fore.RED+'Comando inválido.'+Style.RESET_ALL)
        return
    lista = None
    limpar_tela()
    print('▬'*50)
    if meu_jogador.local == 'e2':
        print(Fore.YELLOW + '          LOJA DOS ESQUECIDOS' + Style.RESET_ALL)
        lista = lista_itens_loja
    elif meu_jogador.local == 'g1':
        print(Fore.YELLOW + '          LOJA DOS MERCENÁRIOS' + Style.RESET_ALL)
        lista = lista_itens_loja_g1
    elif meu_jogador.local == 'j1':
        print(Fore.YELLOW + '          !!!!!LOJA TEM!!!!!' + Style.RESET_ALL)
        lista = lista_itens_loja_temmie
    print('▬'*50)
    print('"Tudo tem um preço... até mesmo a salvação."\n')
    
    # Mostra itens disponíveis
    for i, item in enumerate(lista, 1):
        if 'defesa' in item:  # Se for armadura
            print(f"{i}. {item['nome']} | DEF: {item['defesa']} | VIDA: {item['vida_max']} | RES: {item['resistencia']}% | Preço: {item['preco']}")
            print(f"   {item['desc']}\n")
        else:  # Outros itens
            if item['atk'] > 0:
                print(f"{i}. {item['nome']} | ATK: {item['atk']} | Preço: {item['preco']}")
            else:
                print(f"{i}. {item['nome']} | Preço: {item['preco']}")
            print(f"   {item['desc']}\n")
    
    print(f'Seu ouro: {Fore.YELLOW}{meu_jogador.ouro}{Style.RESET_ALL}')
    print('\nDigite o número do item para comprar ou "sair" para deixar a loja')
    
    while True:
        escolha = input(Fore.LIGHTYELLOW_EX + '>> ' + Style.RESET_ALL).lower()
        
        if escolha == 'sair':
            print('\n"Volte quando tiver mais ouro..."')
            time.sleep(1)
            print_local()
            main_game_loop()
            break
        
        try:
            escolha = int(escolha) - 1
            if escolha < 0 or escolha >= len(lista):
                print(Fore.RED + 'Item inválido!' + Style.RESET_ALL)
                continue
                
            item = lista[escolha]
            
            if meu_jogador.ouro < item['preco']:
                print(Fore.RED + '\n"Você não tem ouro suficiente para isso."' + Style.RESET_ALL)
                time.sleep(1)
                continue
                
            # Confirmação de compra
            print(f'\nDeseja comprar {item["nome"]} por {item["preco"]} de ouro? (s/n)')
            confirmacao = input('>> ').lower()
            
            if confirmacao == 's':
                meu_jogador.ouro -= item['preco']
                
                # Cria o objeto apropriado
                if 'defesa' in item:  # Armadura
                    novo_item = Armadura(
                        item['nome'],
                        item['defesa'],
                        item['vida_max'],
                        item['resistencia'],
                        item['desc'],
                        False,
                        item['consumivel'],
                        item['preco'],
                        item['especial']
                    )
                else:  # Item normal
                    novo_item = Item(
                        item['nome'],
                        item.get('atk', 0),
                        item['desc'],
                        False,
                        item['consumivel'],
                        item['preco'],
                        item['especial']
                    )
                
                meu_jogador.add_item(novo_item)
                print(Fore.GREEN + f'\nVocê comprou {item["nome"]}!' + Style.RESET_ALL)
                time.sleep(1)
                
                # Se for o pergaminho, ativa efeito especial
                if item['nome'] == 'Pergaminho do Apocalipse':
                    usar_pergaminho_apocalipse()
                
                # Pergunta se quer equipar imediatamente (para não consumíveis)
                elif not item['consumivel'] and not item['especial']:
                    print('\nDeseja equipar agora? (s/n)')
                    equipar = input('>> ').lower()
                    if equipar == 's':
                        if isinstance(novo_item, Armadura):
                            if meu_jogador.armadura:
                                meu_jogador.armadura.equipado = False
                            meu_jogador.armadura = novo_item
                        else:
                            if meu_jogador.item_equipado:
                                meu_jogador.item_equipado.equipado = False
                            meu_jogador.item_equipado = novo_item
                        novo_item.equipado = True
                        atualizar_atributos(meu_jogador)
                        print(Fore.GREEN + f'{item["nome"]} equipado!' + Style.RESET_ALL)
                        time.sleep(1)
            
            loja_e2()  # Mostra a loja novamente
            break
            
        except ValueError:
            print(Fore.RED + 'Digite um número válido ou "sair"' + Style.RESET_ALL)

def luta(monstro, meu_jogador):
        # Jogador morre
    if meu_jogador.vida <= 0:
        meu_jogador.game_over = True
        main_game_loop()
        
    print('▀█'+'▀'*50+'█▀')
    efeitos = ''
    for efeito in monstro.efeitos_status:
        efeitos += ("" + efeito.nome + " ")
    print(f'''                {monstro.nome}
                LVL: {monstro.nivel}''')
    print('''                vida:'''+Fore.RED+f' {monstro.vida}'+Style.RESET_ALL+'/'+Fore.RED+f'{monstro.vida_max}'+Style.RESET_ALL)
    print(f'''        Efeitos negativos aplicados: {efeitos}''')
    print('▃█'+'▃'*50+'█▃'+ '\n')
    if meu_jogador.efeitos_status:
        aplicar_efeito(meu_jogador)
        print('')
        if meu_jogador.vida <= 0:
            meu_jogador.game_over = True
            main_game_loop()
    
    mostrar_status(meu_jogador)
    print('       '+'▃'*36)
    print('       █' + Fore.LIGHTYELLOW_EX +' atacar'+Style.RESET_ALL+' █'+Fore.BLUE+' magia '+Style.RESET_ALL+'█ '+Fore.GREEN+'mochila '+Style.RESET_ALL+'█ '+Fore.RED+'fugir '+Style.RESET_ALL+'''█''')
    print('       '+'▀'*36)

    acao = input(Fore.YELLOW + ">>"+Style.RESET_ALL).lower()
    if acao not in ['atacar', 'magia', 'mochila', 'fugir']:
        limpar_tela()
        print(Fore.RED +"comando invádido".upper() + Style.RESET_ALL)
        time.sleep(1.5)
        limpar_tela()
        luta(monstro, meu_jogador)
    
    # Ação: Atacar
    if acao == 'atacar':
        monstro.vida -= meu_jogador.atk_final
        ataque = f"você ataca {monstro.nome}\n"
        for caractere in ataque:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.02)
        loading()
        intervalo()
        
        if monstro.vida > 0:
            monstro.atk_turnos += 1
            if monstro.efeitos_status:
                aplicar_efeito(monstro)
            if monstro.pular_turno:
                luta(monstro, meu_jogador)

            # verifica ataque especial
            if monstro.atk_turnos >= 3:
                dano_especial = monstro.atk * 2
                if monstro.nome == 'A Forjadora' or monstro.nome == 'Krothar, o Espectro da Carnificina':
                    dano_especial += monstro.atk
                    print(f'{monstro.nome} desfere um golpe avassalador te causando {dano_especial} de dano!')
                elif monstro.nome == 'Nyxthar, o Devorador de Almas':
                    vida_recuperada = meu_jogador.atk_final/2
                    monstro.vida += vida_recuperada
                    print(f'O {monstro.nome} te ataca ferozmente causando {dano_especial} de dano!')
                    print(f'{monstro.nome} reupera {vida_recuperada} de vida')
                else:
                    fala = f'\nO {monstro.nome} te ataca ferozmente causando '+Fore.RED+f'{dano_especial} de dano!'+Style.RESET_ALL
                    for caractere in fala:
                        sys.stdout.write(caractere)
                        sys.stdout.flush()
                        time.sleep(0.02)
                
                # Aplica redução de dano especial
                if meu_jogador.armadura and meu_jogador.armadura_resistencia > 0:
                    dano_especial = max(1, int(dano_especial * (1 - (meu_jogador.armadura_resistencia / 100))))
                    print(f"Dano especial reduzido para: {dano_especial}")
                
                # Aplica dano especial
                if meu_jogador.armadura and meu_jogador.armadura_vida > 0:
                    vida_armadura_antes = meu_jogador.armadura_vida
                    meu_jogador.armadura_vida -= dano_especial
                    
                    if meu_jogador.armadura_vida < 0:
                        dano_excedente = -meu_jogador.armadura_vida
                        meu_jogador.vida -= dano_excedente
                        meu_jogador.armadura_vida = 0
                        fala_armadura = f"\nSua armadura absorveu {vida_armadura_antes} de dano e quebrou! ({dano_excedente} de dano passou)"
                        for caractere in fala_armadura:
                            sys.stdout.write(caractere)
                            sys.stdout.flush()
                            time.sleep(0.02)
                    else:
                        fala_armadura2 = f"\nSua armadura absorveu {dano_especial} de dano especial"
                        for caractere in fala_armadura2:
                            sys.stdout.write(caractere)
                            sys.stdout.flush()
                            time.sleep(0.02)
                else:
                    meu_jogador.vida -= dano_especial
                
                monstro.atk_turnos = 0
                if monstro.atk_efeito:
                    meu_jogador.add_efeito(monstro.atk_efeito)
                input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)
                limpar_tela()
                luta(monstro, meu_jogador)
            
            # Cálculo do dano recebido com sistema de armadura
            dano = monstro.atk
            dano_original = dano  # Guarda o dano original para exibição
            
            if meu_jogador.armadura:
                dano = max(1, dano - meu_jogador.armadura.defesa)  # Redução fixa
                fala_dano = f"Dano reduzido por DEF: {dano_original} -> {dano} (DEF: {meu_jogador.armadura.defesa})"
                for caractere in fala_dano:
                    sys.stdout.write(caractere)
                    sys.stdout.flush()
                    time.sleep(0.02)
            
            # Aplica redução percentual depois
                if meu_jogador.armadura_resistencia > 0:
                    dano_reduzido = max(1, int(dano * (1 - (meu_jogador.armadura_resistencia / 100))))
                    fala_dano2 = f"Dano reduzido por RES: {dano} -> {dano_reduzido} ({meu_jogador.armadura_resistencia}% RES)"
                    for caractere in fala_dano2:
                        sys.stdout.write(caractere)
                        sys.stdout.flush()
                        time.sleep(0.02)
                    dano = dano_reduzido

            # Aplica redução de dano da armadura se existir
            if meu_jogador.armadura and meu_jogador.armadura_resistencia > 0:
                dano = max(1, int(dano * (1 - (meu_jogador.armadura_resistencia / 100))))
                
                # Exibe informações de redução de dano
                fala_dano3 = f"Dano original: {dano_original} | Reduzido para: {dano} ({meu_jogador.armadura_resistencia}% de resistência)"
                for caractere in fala_dano3:
                    sys.stdout.write(caractere)
                    sys.stdout.flush()
                    time.sleep(0.02)
            
            # Aplica dano à armadura primeiro, se houver vida na armadura
            if meu_jogador.armadura and meu_jogador.armadura_vida > 0:
                vida_armadura_antes = meu_jogador.armadura_vida
                meu_jogador.armadura_vida -= dano
                
                # Se a armadura quebrar, o dano excedente vai para a vida
                if meu_jogador.armadura_vida < 0:
                    dano_excedente = -meu_jogador.armadura_vida
                    meu_jogador.vida -= dano_excedente
                    meu_jogador.armadura_vida = 0
                    fala_armadura3 = f"Sua armadura absorveu {vida_armadura_antes} de dano e quebrou! ({dano_excedente} de dano passou)"
                    for caractere in fala_armadura3:
                        sys.stdout.write(caractere)
                        sys.stdout.flush()
                        time.sleep(0.02)
                else:
                    fala_armadura4 = f"Sua armadura absorveu {dano} de dano"
                    for caractere in fala_armadura4:
                        sys.stdout.write(caractere)
                        sys.stdout.flush()
                        time.sleep(0.02)
            else:
                # Sem armadura ou armadura sem vida, todo dano vai para vida
                meu_jogador.vida -= dano
            
            # Ataque especial do monstro a cada 3 turnos
            
            
            # Ataque normal do monstro
            ataque2 = f'\no {monstro.nome} te ataca causando {dano} de dano\n'
            for caractere in ataque2:
                sys.stdout.write(caractere)
                sys.stdout.flush()
                time.sleep(0.02)
            loading()
            input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)
        
        intervalo()
        limpar_tela()
        
    # Ação: Magia (mantido igual ao original)
    elif acao == 'magia':
        if meu_jogador.magias:
            for i in range(len(meu_jogador.magias)):
                magia = meu_jogador.magias[i]
                print(f'{i+1}. {magia.nome} | DANO: {magia.dano} + DANO ADICIONAL: {meu_jogador.dano_magico_final} | custo de mana: {magia.mana_gasta} | desc: {magia.desc}')
            print("Use números para escolher as magias")
            escolha = input(Fore.YELLOW+"\n>>"+Style.RESET_ALL)
            try:
                escolha = int(escolha)-1
                if escolha not in range(0, len(meu_jogador.magias)):
                    print(Fore.RED +'Magia inválida'+Style.RESET_ALL)
                    time.sleep(1.5)
                    limpar_tela()
                    luta(monstro, meu_jogador)

                if meu_jogador.mana < meu_jogador.magias[escolha].mana_gasta:
                    print(Fore.RED+'**MANA INSUFICIENTE**'+Style.RESET_ALL)
                    time.sleep(1.5)
                    limpar_tela()
                    luta(monstro, meu_jogador)
                dano_magia = (meu_jogador.magias[escolha].dano + meu_jogador.dano_magico_final)
                monstro.vida -= dano_magia
                meu_jogador.mana -= meu_jogador.magias[escolha].mana_gasta
                monstro.add_efeito(meu_jogador.magias[escolha].efeito)
                magias = f'Você lança {meu_jogador.magias[escolha].nome} em {monstro.nome}'
                for caractere in magias:
                    sys.stdout.write(caractere)
                    sys.stdout.flush()
                    time.sleep(0.02)
                loading()
                intervalo()

                if monstro.vida > 0:
                    monstro.atk_turnos += 1
                    if monstro.efeitos_status:
                        aplicar_efeito(monstro)
                    if monstro.pular_turno:
                        limpar_tela()
                        luta(monstro, meu_jogador)

                    # verifica ataque especial
                    if monstro.atk_turnos >= 3:
                        dano_especial = monstro.atk * 2
                        if monstro.nome == 'A Forjadora':
                            dano_especial = monstro.atk * 2
                            dano_especial += monstro.atk
                            print(f'{monstro.nome} desfere um golpe avassalador te causando {dano_especial} de dano!')
                        elif monstro.nome == 'Nyxthar, o Devorador de Almas':
                            vida_recuperada = meu_jogador.atk_final/2
                            monstro.vida += vida_recuperada
                            print(f'O {monstro.nome} te ataca ferozmente causando {dano_especial} de dano!')
                            print(f'{monstro.nome} reupera {vida_recuperada} de vida')
                        else:
                            ataque4 = f'\nO {monstro.nome} te ataca ferozmente causando '+Fore.RED+f'{dano_especial} de dano!'+Style.RESET_ALL
                            for caractere in ataque4:
                                sys.stdout.write(caractere)
                                sys.stdout.flush()
                                time.sleep(0.02)
                        
                        if meu_jogador.armadura and meu_jogador.armadura_resistencia > 0:
                            dano_especial = max(1, int(dano_especial * (1 - (meu_jogador.armadura_resistencia / 100))))
                            dano_reduzido2 = f"Dano especial reduzido para: {dano_especial}"
                            for caractere in dano_reduzido2:
                                sys.stdout.write(caractere)
                                sys.stdout.flush()
                                time.sleep(0.02)

                        if meu_jogador.armadura and meu_jogador.armadura_vida > 0:
                            vida_armadura_antes = meu_jogador.armadura_vida
                            meu_jogador.armadura_vida -= dano_especial
                            
                            if meu_jogador.armadura_vida < 0:
                                dano_excedente = -meu_jogador.armadura_vida
                                meu_jogador.vida -= dano_excedente
                                meu_jogador.armadura_vida = 0
                                fala_armadura5 = f"Sua armadura absorveu {vida_armadura_antes} de dano e quebrou! ({dano_excedente} de dano passou)"
                                for caractere in fala_armadura5:
                                    sys.stdout.write(caractere)
                                    sys.stdout.flush()
                                    time.sleep(0.02)
                            else:
                                fala_armadura6 = f"Sua armadura absorveu {dano_especial} de dano especial"
                                for caractere in fala_armadura6:
                                    sys.stdout.write(caractere)
                                    sys.stdout.flush()
                                    time.sleep(0.02)
                        else:
                            meu_jogador.vida -= dano_especial
                        
                        monstro.atk_turnos = 0
                        if monstro.atk_efeito:
                            meu_jogador.add_efeito(monstro.atk_efeito)
                        input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)
                        limpar_tela()
                        luta(monstro, meu_jogador)
                    
                    # Cálculo do dano recebido após magia (com sistema de armadura)
                    dano = monstro.atk
                    
                    if meu_jogador.armadura and meu_jogador.armadura_resistencia > 0:
                        dano = max(1, int(dano * (1 - (meu_jogador.armadura_resistencia / 100))))
                    
                    if meu_jogador.armadura and meu_jogador.armadura_vida > 0:
                        vida_armadura_antes = meu_jogador.armadura_vida
                        meu_jogador.armadura_vida -= dano
                        
                        if meu_jogador.armadura_vida < 0:
                            dano_excedente = -meu_jogador.armadura_vida
                            meu_jogador.vida -= dano_excedente
                            meu_jogador.armadura_vida = 0
                            fala_armadura7 = f"Sua armadura absorveu {vida_armadura_antes} de dano e quebrou! ({dano_excedente} de dano passou)"
                            for caractere in fala_armadura7:
                                sys.stdout.write(caractere)
                                sys.stdout.flush()
                                time.sleep(0.02)
                        else:
                            fala_armadura8 = f"Sua armadura absorveu {dano} de dano"
                            for caractere in fala_armadura8:
                                sys.stdout.write(caractere)
                                sys.stdout.flush()
                                time.sleep(0.02)
                    else:
                        meu_jogador.vida -= dano
                    
                    
                    ataque_monstro = Fore.RED+f'\no {monstro.nome} te ataca causando {dano} de dano\n'+Style.RESET_ALL
                    for caractere in ataque_monstro:
                        sys.stdout.write(caractere)
                        sys.stdout.flush()
                        time.sleep(0.001)
                    loading()
                intervalo()
                limpar_tela()
            except:
                print(Fore.RED+'\nComando inválido'+Style.RESET_ALL)
                time.sleep(1.5)
                limpar_tela()
                luta(monstro, meu_jogador)
        else:
            print('Você ainda não aprendeu magias')
            loading()
            
            # Dano recebido quando não tem magias (com sistema de armadura)
            dano = monstro.atk
            
            if meu_jogador.armadura and meu_jogador.armadura_resistencia > 0:
                dano = max(1, int(dano * (1 - (meu_jogador.armadura_resistencia / 100))))
            
            if meu_jogador.armadura and meu_jogador.armadura_vida > 0:
                vida_armadura_antes = meu_jogador.armadura_vida
                meu_jogador.armadura_vida -= dano
                
                if meu_jogador.armadura_vida < 0:
                    dano_excedente = -meu_jogador.armadura_vida
                    meu_jogador.vida -= dano_excedente
                    meu_jogador.armadura_vida = 0
                    fala_armadura9 = f"Sua armadura absorveu {vida_armadura_antes} de dano e quebrou! ({dano_excedente} de dano passou)"
                    for caractere in fala_armadura9:
                        sys.stdout.write(caractere)
                        sys.stdout.flush()
                        time.sleep(0.02)
                else:
                    fala_armadura10 = f"Sua armadura absorveu {dano} de dano"
                    for caractere in fala_armadura10:
                        sys.stdout.write(caractere)
                        sys.stdout.flush()
                        time.sleep(0.02)
            else:
                meu_jogador.vida -= dano
            
            ataque5 = f'o {monstro.nome} te ataca'
            for caractere in ataque5:
                sys.stdout.write(caractere)
                sys.stdout.flush()
                time.sleep(0.02)
            intervalo()
            limpar_tela()
    
    # Ação: Mochila (mantido igual ao original)
    elif acao == 'mochila':
        consumiveis = []
        for item in meu_jogador.mochila:
            if not hasattr(item, 'consumivel') or not hasattr(item, 'especial'):
                print(f"Item inválido na mochila: {item}")
                continue  # Pula para o próximo item
        
            if item.consumivel:
                consumiveis.append(item)

        if not consumiveis:
            # print(Fore.RED+'Nenhum item para ser usado'+Style.RESET_ALL)
            time.sleep(1.5)
            limpar_tela()
            luta(monstro, meu_jogador)
            
        for i, consumivel in enumerate(consumiveis, 1):
            print(f'{i}. {consumivel.nome} | {consumivel.desc}')
        print('Use os números para selecionar os itens')
        escolha = input('>>').lower()
        
        try:
            escolha = int(escolha)
            if escolha < 1 or escolha > len(consumiveis):
                print(Fore.RED+'\nComando inválido'+Style.RESET_ALL)
                time.sleep(1.5)
                limpar_tela()
                luta(monstro, meu_jogador)
                
            item_selecionado = consumiveis[escolha-1]
            print(f'{item_selecionado.nome} | {item_selecionado.desc}')
            print('[usar | voltar]')
            acao_item = input('>>').lower()
            
            if acao_item not in ['usar', 'voltar']:
                print(Fore.RED+'\nComando inválido'+Style.RESET_ALL)
                limpar_tela()
                luta(monstro, meu_jogador)
                
            if acao_item == 'usar':
                # Remove o item da mochila principal
                for i, item in enumerate(consumiveis):
                    if item.nome == item_selecionado.nome:
                        meu_jogador.mochila.pop(i)
                        break
                        
                # Aplica o efeito do item
                if item_selecionado.nome == 'Poção de Vida Lendária':
                    pocao_vida_lendaria()
                elif item_selecionado.nome == 'Poção de Mana Lendária':
                    pocao_mana_lendaria()
                elif item_selecionado.nome == 'Pocao de vida baixa':
                    pocao_vida()
                elif item_selecionado.nome == 'Pocao de vida media':
                    pocao_vida_media()
                elif item_selecionado.nome == 'Pocao de vida alta':
                    pocao_vida_alta()
                elif item_selecionado.nome == 'Pocao de mana baixa':
                    pocao_mana()
                elif item_selecionado.nome == 'Pocao de mana media':
                    pocao_mana_media()
                elif item_selecionado.nome == 'Pocao de mana alta':
                    pocao_mana_alta()
                elif item_selecionado.nome == 'Carne de Homunculo':
                    carne_homunculo()
                elif item_selecionado.nome == 'Flocos de TEM':
                    flocos_de_tem()
                elif item_selecionado.nome == 'Erva de Mana':
                    pocao_erva_de_mana()

                    
                limpar_tela()
                luta(monstro, meu_jogador)
            elif acao_item == 'voltar':
                limpar_tela()
                luta(monstro, meu_jogador)
                
        except ValueError:
            print(Fore.RED+'\nComando inválido'+Style.RESET_ALL)
            limpar_tela()
            luta(monstro, meu_jogador)
    
    # Ação: Fugir (mantido igual ao original)
    elif acao == 'fugir':
        aleatorio = random.randint(1, 100)
        if aleatorio <= 60:
            fugir()
        else:
            meu_jogador.vida -= monstro.atk
            fala3 = f'O {monstro.nome} te impediu de fugir e ataca'
            for caractere in fala3:
                sys.stdout.write(caractere)
                sys.stdout.flush()
                time.sleep(0.02)
            limpar_tela()
            luta(monstro, meu_jogador)
    
    # Verifica condições de vitória/derrota
    if meu_jogador.vida > 0 and monstro.vida > 0:
        limpar_tela()
        luta(monstro, meu_jogador)
        
    # Jogador morre
    if meu_jogador.vida <= 0:
        meu_jogador.game_over = True
        main_game_loop()

    # Monstro morre
    elif monstro.vida <= 0:
        if meu_jogador.efeitos_status:
            meu_jogador.efeitos_status.clear()
        if meu_jogador.local == 'c2' and mapa['c2']['contador2'] == 0:
            mapa['c2']['contador2'] += 1
            limpar_tela()
            print(f'VOCÊ DERROTOU {monstro.nome}')
            experiencia(monstro)
            time.sleep(1)
            if monstro.boss == True:
                mapa[meu_jogador.local]['SOLVED'] = True
            drop_monstro(monstro)
            corredor()
        if meu_jogador.local == 'j2' and mapa['j2']['contador2'] == 1:
            limpar_tela()
            fim_de_jogo()
            if monstro.boss == True:
                mapa[meu_jogador.local]['SOLVED'] = True
            drop_monstro(monstro)
        limpar_tela()
        print(f'VOCÊ DERROTOU {monstro.nome}')
        experiencia(monstro)
        time.sleep(1)
        if monstro.boss == True:
            mapa[meu_jogador.local]['SOLVED'] = True
        drop_monstro(monstro)
        print_local()
        main_game_loop()
        
    elif acao == 'magia':
        if meu_jogador.magias:
            for i in range(len(meu_jogador.magias)):
                magia = meu_jogador.magias[i]
                print(f'{i+1}. {magia.nome} | DANO: {magia.dano} + DANO ADICIONAL: {meu_jogador.dano_magico} | custo de mana: {magia.mana_gasta} | desc: {magia.desc}')
            print("Use números para escolher as magias")
            escolha = input(Fore.YELLOW + "\n>>"+Style.RESET_ALL)
            try:
                escolha = int(escolha)-1
                if escolha not in range(0, len(meu_jogador.magias)):
                    print(Fore.RED +'Magia inválida'+Style.RESET_ALL)
                    time.sleep(1.5)
                    limpar_tela()
                    luta(monstro, meu_jogador)

                if meu_jogador.mana < meu_jogador.magias[escolha].mana_gasta:
                    print(Fore.RED+'**MANA INSUFICIENTE**'+Style.RESET_ALL)
                    time.sleep(1.5)
                    limpar_tela()
                    luta(monstro, meu_jogador)

                monstro.vida -= (meu_jogador.magias[escolha].dano + meu_jogador.dano_magico)
                meu_jogador.mana -= meu_jogador.magias[escolha].mana_gasta
                monstro.add_efeito(meu_jogador.magias[escolha].efeito)
                magias = f'Você lança {meu_jogador.magias[escolha].nome} em {monstro.nome}'
                for caractere in magias:
                    sys.stdout.write(caractere)
                    sys.stdout.flush()
                    time.sleep(0.02)
                loading()
                intervalo()

                if monstro.vida > 0:
                    
                    monstro.atk_turnos += 1
                    if monstro.efeitos_status:
                        aplicar_efeito(monstro)
                    if monstro.pular_turno:
                        limpar_tela()
                        luta(monstro, meu_jogador)
                    if monstro.atk_turnos >= 3:
                        meu_jogador.vida -= monstro.atk*2
                        ataque3 = f'\nO {monstro.nome} te ataca ferozmente\n'
                        for caractere in ataque3:
                            sys.stdout.write(caractere)
                            sys.stdout.flush()
                            time.sleep(0.02)
                        input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)
                        monstro.atk_turnos = 0
                        if monstro.atk_efeito:
                            meu_jogador.add_efeito(monstro.atk_efeito)
                        limpar_tela()
                        luta(monstro, meu_jogador)

                    meu_jogador.vida -= monstro.atk
                    ataque_monstro = Fore.RED+f'\no {monstro.nome} te ataca\n'+Style.RESET_ALL
                    for caractere in ataque_monstro:
                        sys.stdout.write(caractere)
                        sys.stdout.flush()
                        time.sleep(0.02)
                    loading()
                intervalo()
                limpar_tela()
            except:
                print(Fore.RED+'\nComando inválido'+Style.RESET_ALL)
                time.sleep(1.5)
                limpar_tela()
                luta(monstro, meu_jogador)
        else:
            print('Você ainda não aprendeu magias')
            loading()
            meu_jogador.vida -= monstro.atk
            fala3 = f'o {monstro.nome} te ataca'
            for caractere in fala3:
                sys.stdout.write(caractere)
                sys.stdout.flush()
                time.sleep(0.02)
            intervalo()
            limpar_tela()
    elif acao == 'mochila':
        consumiveis = []
        for consumivel in meu_jogador.mochila:
            if consumivel.consumivel:
                consumiveis.append(consumivel)
        if not consumivel:
            print(Fore.RED+'Nenhum item para ser usado'+Style.RESET_ALL)
            time.sleep(1.5)
            limpar_tela()
            luta(monstro, meu_jogador)
        for i, consumivel in enumerate(consumiveis):
            print(f'{i+1}. {consumivel.nome} | {consumivel.desc}')
        print('Use os números para selecionar os itens')
        escolha = input(Fore.YELLOW+'\n>>'+Style.RESET_ALL).lower()
        try:
            escolha = int(escolha)-1
            if escolha not in range(0, len(consumiveis)):
                print(Fore.RED+'\nComando inválido'+Style.RESET_ALL)
                limpar_tela()
                luta(monstro, meu_jogador)
            print(f'{consumiveis[escolha].nome} | {consumiveis[escolha].desc}')
            print('[usar | voltar]')
            acao = input(Fore.YELLOW+'\n>>'+Style.RESET_ALL).lower()
            if acao not in ['usar', 'voltar']:
                print(Fore.RED+'\nComando inválido'+Style.RESET_ALL)
                limpar_tela()
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
                elif meu_jogador.mochila[escolha].nome == 'Carne de Homunculo':
                    carne_homunculo()
                elif meu_jogador.mochila[escolha].nome == 'Poção de Vida Lendária':
                    pocao_vida_lendaria()
                elif meu_jogador.mochila[escolha].nome == 'Poção de Mana Lendária':
                    pocao_mana_lendaria()
                elif item_selecionado.nome == 'Flocos de TEM':
                    flocos_de_tem()
                elif item_selecionado.nome == 'Erva de Mana':
                    pocao_erva_de_mana()
                
                for i, item in enumerate(meu_jogador.mochila):
                    if item.nome == consumiveis[escolha].nome:
                        meu_jogador.mochila.pop(i)
                limpar_tela()
                luta(monstro, meu_jogador)
            elif acao == 'voltar':
                limpar_tela()
                luta(monstro, meu_jogador)
        except:
            print(Fore.RED+'\nComando inválido'+Style.RESET_ALL)
            limpar_tela()
            luta(monstro, meu_jogador)
    
    elif acao == 'fugir':
        if aleatorio <= 60:
            fugir()
        else:
            meu_jogador.vida -= monstro.atk
            fala3 = f'O {monstro.nome} te impediu de fugir e ataca'
            for caractere in fala3:
                sys.stdout.write(caractere)
                sys.stdout.flush()
                time.sleep(0.02)
            limpar_tela()
            luta(monstro, meu_jogador)
    
    # fim do turno
    if meu_jogador.vida > 0 and monstro.vida > 0:
        limpar_tela()
        luta(monstro, meu_jogador)
        
    # jogador morre
    if meu_jogador.vida <= 0:
        # meu_jogador.local = 'a1'
        # meu_jogador.vida = meu_jogador.vida_max
        # limpar_tela()
        meu_jogador.game_over = True
        main_game_loop()

    # monstro morre
    elif monstro.vida <= 0:
        if meu_jogador.local == 'c2' and mapa['c2']['contador2'] == 0:
            mapa['c2']['contador2'] += 1
            limpar_tela()
            print(f'VOCÊ DERROTOU {monstro.nome}')
            experiencia(monstro)
            time.sleep(1)
            if monstro.boss == True:
                mapa[meu_jogador.local]['SOLVED'] = True
            drop_monstro(monstro)
            corredor()
        limpar_tela()
        if meu_jogador.local == 'j2' and mapa['j2']['contador2'] == 1:
            limpar_tela()
            fim_de_jogo()
        if monstro.boss == True:
            mapa[meu_jogador.local]['SOLVED'] = True
        drop_monstro(monstro)
        print_local()
        main_game_loop()

def aplicar_efeito(alvo):
    for i, efeito in enumerate(alvo.efeitos_status):
        if efeito.tipo == 'dano':
            alvo.vida -= efeito.dano
            print(f'{alvo.nome} está com {efeito.nome} e sofreu {efeito.dano} de dano')
            alvo.efeitos_status[i].tempo -= 1
            if alvo.efeitos_status[i].tempo == 0:
                alvo.efeitos_status.pop(i)
        elif efeito.tipo == 'pular':
            alvo.pular_turno = True
            if random.random() < 0.5:
                alvo.pular_turno = False
                alvo.efeitos_status.pop(i)
                continue
            congelado = Fore.LIGHTBLUE_EX+f'{alvo.nome} está conglado e não pode atacar\n'+Style.RESET_ALL
            for congelados in congelado:
                sys.stdout.write(congelados)
                sys.stdout.flush()
                time.sleep(0.001)
            input(Fore.LIGHTYELLOW_EX + "\n[Pressione Enter]" + Style.RESET_ALL)

        elif efeito.tipo == 'skip':
            alvo.pular_turno = True
            chance = random.randint(1,100)
            if chance <= 40:
                alvo.efeitos_status[i].tempo -= 1
                if alvo.efeitos_status[i].tempo == 0:
                    alvo.efeitos_status.pop(i)
                alvo.pular_turno = False
            else:
                stunado = Fore.LIGHTBLUE_EX+f'{alvo.nome} está atordoado e não pode atacar'+Style.RESET_ALL
                for caractere in stunado:
                    sys.stdout.write(caractere)
                    sys.stdout.flush()
                    time.sleep(0.001)
                input(Fore.LIGHTYELLOW_EX + "\n[Pressione Enter]" + Style.RESET_ALL)
        elif efeito.tipo == 'absorção':
            meu_jogador.vida += 30
            if meu_jogador.vida > meu_jogador.vida_max:
                meu_jogador.vida = meu_jogador.vida_max
            stunado = Fore.LIGHTBLUE_EX+f'Você absorveu 30 pontos de vida de {alvo.nome}'+Style.RESET_ALL
            for caractere in stunado:
                sys.stdout.write(caractere)
                sys.stdout.flush()
                time.sleep(0.001)
            input(Fore.LIGHTYELLOW_EX + "\n[Pressione Enter]" + Style.RESET_ALL)
                

def drop_monstro(monstro):
    print('Você ganhou '+Fore.YELLOW+f'{monstro.ouro}'+Style.RESET_ALL+' de ouro!')
    meu_jogador.ouro += monstro.ouro
    input(Fore.LIGHTYELLOW_EX + "\n[Pressione Enter]" + Style.RESET_ALL)
    
    itens_que_droparam = []
    
    # Verifica cada item para ver se dropou
    for drop in monstro.drops:
        if random.random() <= drop['chance']:  # Gera um número entre 0 e 1
            itens_que_droparam.append(drop['item'])
    
    if not itens_que_droparam:
        if meu_jogador.local == 'c2' and mapa['c2']['contador2'] == 1:
            print(f"\nO {monstro.nome} não dropou nenhum item.")
            mapa[meu_jogador.local]['MONSTRO'] = ''
            mapa['c2']['contador2'] += 1
            limpar_tela()
            corredor()
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
        print(Fore.RED+'\nComando inválido!'+Style.RESET_ALL)
        drop_monstro(monstro)
    
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
    elif meu_jogador.local == 'a1':
        meu_jogador.local = 'a1'
    elif meu_jogador.local == 'b1':
        meu_jogador.local = 'a2'
    elif meu_jogador.local == 'b2':
        meu_jogador.local = 'b1'
    elif meu_jogador.local == 'c1':
        meu_jogador.local = 'b2'
    elif meu_jogador.local == 'c2':
        meu_jogador.local = 'c1'
    elif meu_jogador.local == 'd1':
        meu_jogador.local = 'c2'
    elif meu_jogador.local == 'd2':
        meu_jogador.local = 'd1'
    elif meu_jogador.local == 'e1':
        meu_jogador.local = 'd2'
    elif meu_jogador.local == 'e2':
        meu_jogador.local = 'e1'
    elif meu_jogador.local == 'f1':
        meu_jogador.local = 'e2'
    elif meu_jogador.local == 'f2':
        meu_jogador.local = 'f1'
    elif meu_jogador.local == 'g1':
        meu_jogador.local = 'f2'
    elif meu_jogador.local == 'g2':
        meu_jogador.local = 'g1'
    elif meu_jogador.local == 'h1':
        meu_jogador.local = 'g2'
    elif meu_jogador.local == 'h2':
        meu_jogador.local = 'h1'
    elif meu_jogador.local == 'i1':
        meu_jogador.local = 'h2'
    elif meu_jogador.local == 'i2':
        meu_jogador.local = 'i1'
    elif meu_jogador.local == 'j1':
        meu_jogador.local = 'i2'
    elif meu_jogador.local == 'j2':
        meu_jogador.local = 'j1'
    fala = 'você voltou para a sala anterior'
    for falas in fala:
        sys.stdout.write(falas)
        sys.stdout.flush()
        time.sleep(0.02)
    print_local()
    

    print('você voltou para a sala anterior')
    main_game_loop()

def mostrar_status(self):
    print('\n'+'█'+'▀'*50+'█')
    print(f'█             Nome: {self.nome} LVL:{self.nivel} XP: {self.xp}/{self.xp_max}            \n█')
    print('''█         Vida: '''+Fore.RED+f'''{self.vida}'''+Style.RESET_ALL+'''/'''+Fore.RED+f'''{self.vida_max}'''+Style.RESET_ALL+'''        ATK: '''+Fore.GREEN+f'''{self.atk}'''+Style.RESET_ALL+''' 
█         Mana: '''+Fore.BLUE+f'''{self.mana}/{self.mana_max}'''+Style.RESET_ALL+'''      MAG.ATK: '''+Fore.LIGHTBLUE_EX+f'''{self.dano_magico}\n'''+Style.RESET_ALL+'█')
    
    # Adiciona informações da armadura
    if self.armadura:
        print(f'█      Armadura: {self.armadura.nome} DEF: {self.armadura.defesa} RES: {self.armadura.resistencia}%')
        print(f'█         Vida Armadura: '+Fore.CYAN+f'{self.armadura_vida}'+Style.RESET_ALL+'/'+Fore.CYAN+f'{self.armadura_vida_max}'+Style.RESET_ALL)
    else:
        print('█         Armadura: Nenhuma equipada')
    
    if self.item_equipado:
        if self.item_equipado.dano_magico:
            print(f'█         arma: {self.item_equipado.nome} DANO MÁGICO: {self.item_equipado.dano_magico}                ')
        else:
            print(f'█         arma: {self.item_equipado.nome} ATK: {self.item_equipado.atk}                ')
        for efeito in self.efeitos_status:
            print(f'█         efeitos de status: {efeito.nome}', end=' ')
            print('')
    else:
        print('█         arma: sem arma equipada                 ')
        for efeito in self.efeitos_status:
            print(f'█         efeitos de status: {efeito.nome}', end=' ')
            print('')
    print('█'+'▃'*50+'█')

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
            time.sleep(1.5)
            main_game_loop()
        elif meu_jogador.local == 'a2' and not mapa[meu_jogador.local]['SOLVED']:
            fala1 = 'Algumas raizes impedem a passagem, aparentemente vem do Enraizado.'
            for falas in fala1:
                sys.stdout.write(falas)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1.5)
            main_game_loop()
        if meu_jogador.local == 'b1' and not mapa[meu_jogador.local]['SOLVED']:
            fala2 = 'A força das máscaras por algum motivo impedem de abrir a porta.'
            for falas in fala2:
                sys.stdout.write(falas)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1.5)
            main_game_loop()
        elif meu_jogador.local == 'd2' and not mapa[meu_jogador.local]['SOLVED']:
            jogador_examinar()
        elif meu_jogador.local == 'c2' and not mapa[meu_jogador.local]['SOLVED']:
            fala3 = 'O robô está na frente da porta, é preciso um núcleo para ativa-lo e remove-lo da frente.'
            for falas in fala3:
                sys.stdout.write(falas)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1.5)
            main_game_loop()
        elif meu_jogador.local == 'f2' and not mapa[meu_jogador.local]['SOLVED']:
            fala4 = 'O cavaleiro impede a sua passagem...'
            for falas in fala4:
                sys.stdout.write(falas)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1.5)
            main_game_loop()
        elif meu_jogador.local == 'g2' and not mapa[meu_jogador.local]['SOLVED']:
            fala5 = '''
    A forjadora impede sua passagem, olha para você e diz:
        "Ah seu covarde, tentando fugir sem uma luta?"'''
            for falas in fala5:
                sys.stdout.write(falas)
                sys.stdout.flush()
                time.sleep(0.01)
            time.sleep(1.5)
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
        pergunta = '''
A sua frente ergue-se uma porta de metal envelhecido, marcada por engrenagens imóveis e ferrugem acumulada. 
O tique-taque ausente paira como um silêncio opressivo, enquanto o enorme relógio acima da entrada permanece eternamente parado, congelado em um momento esquecido.
Avançar pela porta ou retornar subindo à sala anterior? (escreva: avançar ou subir)\n>>'''
    elif meu_jogador.local in 'c2':
        pergunta = '''
À sua frente, uma escadaria espiral desce lentamente, envolta em sombras densas que parecem sussurrar segredos esquecidos. 
No fim do caminho, aguarda a Câmara do Berço do Abismo, onde o desconhecido pulsa silencioso.
Descer as escadas ou retornar à sala anterior? (escreva: descer ou retornar)\n>>'''
    elif meu_jogador.local in 'd1':
        pergunta = """
À sua frente, uma porta pulsante feita de carne e entrelaçada por veios de sangue bloqueia a passagem, exalando um calor úmido e doentio. 
Do outro lado, aguarda o Laboratório dos Deformados, onde a anatomia foi corrompida e a ciência perdeu sua forma.
Deseja avançar, atravessando a porta viva, ou subir as escadas para retornar à sala anterior? (escreva: avançar ou subir)\n>>"""
    elif meu_jogador.local in 'd2':
        pergunta = """
À sua frente, uma escadaria sinuosa mergulha em direção às profundezas, onde pulsa silenciosamente o Nódulo Desperto. 
O ar fica mais denso, carregado de antecipação e repulsa.
Deseja descer as escadas ou retornar à sala anterior? (escreva: descer ou retornar)(escreva: descer ou retornar)\n>>"""
    elif meu_jogador.local in 'e1':
        pergunta = """
À sua frente, uma porta de madeira carcomida pelo tempo se entreabre, deixando escapar um aroma de poeira antiga e objetos esquecidos. 
Do outro lado, repousa a enigmática Loja dos Esquecidos, onde memórias abandonadas aguardam silenciosas entre as prateleiras.
Avançar ou subir à sala anterior? (escreva: avançar ou subir)\n>>"""

    elif meu_jogador.local in 'e2':
        pergunta = """
À sua frente, uma escadaria de pedra gasta desce lentamente, conduzindo à sombria Galeria dos Pactos Perdidos, 
onde antigos juramentos ecoam em silêncio entre os arcos desmoronados. A atmosfera pesa como o fardo de promessas quebradas.
Descer as escadas ou retornar à sala anterior? (escreva: descer ou retornar)\n>>"""

    elif meu_jogador.local in 'f1':
        pergunta = """
À sua frente, imponentes portas entreabertas revelam o Salão da Coroa Quebrada, onde vestígios de glória esquecida jazem sob os escombros e a poeira. 
O trono, vazio e partido, repousa no centro como um símbolo silencioso de ruína e poder perdido.
Avançar ou subir à sala anterior? (escreva: avançar ou subir)\n>>"""

    elif meu_jogador.local in 'f2':
        pergunta = """Descer as escadas ou retornar a sala anterior? (escreva: descer ou retornar)\n>>"""
    elif meu_jogador.local in 'g1':
        pergunta = "Avançar ou subir a sala anterior? (escreva: avançar ou subir)\n>>"
    elif meu_jogador.local in 'g2':
        pergunta = "Descer as escadas ou retornar a sala anterior? (escreva: descer ou retornar)\n>>"
    elif meu_jogador.local in 'h1':
        pergunta = "Avançar ou subir a sala anterior? (escreva: avançar ou subir)\n>>"
    elif meu_jogador.local in 'h2':
        pergunta = "Descer as escadas ou retornar a sala anterior? (escreva: descer ou retornar)\n>>"
    elif meu_jogador.local in 'i1':
        pergunta = "Avançar ou subir a sala anterior? (escreva: avançar ou subir)\n>>"
    elif meu_jogador.local in 'i2':
        pergunta = "Descer as escadas ou retornar a sala anterior? (escreva: descer ou retornar)\n>>"
    elif meu_jogador.local in 'j1':
        pergunta = "Avançar ou subir a sala anterior? (escreva: avançar ou subir)\n>>"
    elif meu_jogador.local in 'j2':
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
            print(Fore.RED+"Você não pode se mover nessa direção."+Style.RESET_ALL)
    else:
        print(Fore.RED+"Direção inválida."+Style.RESET_ALL)

def movimento_manipulado(destino):
    meu_jogador.local = destino
    print(f"\nVocê se moveu para {mapa[destino]['NOME_LOCAL']}.")
    input(Fore.YELLOW+'[Pressione Enter]'+Style.RESET_ALL)
    limpar_tela()
    print_local()


def jogador_examinar():
    examinar = mapa[meu_jogador.local]['EXAMINAR']
    if mapa[meu_jogador.local][SOLVED] == True and meu_jogador.local == 'a1':
        examinar2 = '''
Atrás de você, o que restou do trono escurece ainda mais, como se a própria sombra tentasse fugir dali. 
A energia maligna está morrendo... mas algo abaixo desperta.

Você se vira, encarando a única saída: um Portão Negro, que leva a uma proxima sala nas profundezas da torre. 
A estrutura range como um animal faminto, esperando que você se mova. (Digite "sair" para sair de perto do trono)\n
'''
        for examina in examinar2:
            sys.stdout.write(examina)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(2)

    elif mapa[meu_jogador.local][SOLVED] == True and meu_jogador.local == 'a2':
        examinar5 = """
Você se volta aquela criatura caida no chão, as raizes que antes prendiam a porta se soltam e libera a passagem para você.
(Para sair de perto da criatura digite "sair)\n
"""
        for examina in examinar5:
            sys.stdout.write(examina)
            sys.stdout.flush()
            time.sleep(0.01)

    elif meu_jogador.local == 'b1' and mapa[meu_jogador.local]['SOLVED'] == True:
        examinar3 = '''
As máscaras param de se mover e o som das vozes desaparece, o poder delas se apagou.
'''
        for examina in examinar3:
            sys.stdout.write(examina)
            sys.stdout.flush()
            time.sleep(0.01)
    
    elif meu_jogador.local == 'i1' and mapa['i1']['mimico'] == True:
        examinar4 = '''
A criatua está morta no chão. Você já pegou o item de dentro dela.\n
'''
        for examina in examinar4:
            sys.stdout.write(examina)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1.5)

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
        if meu_jogador.local == 'g2' and mapa['g2']['SOLVED'] == False:
            input(Fore.LIGHTYELLOW_EX + "\n[Pressione Enter]" + Style.RESET_ALL)
            limpar_tela()
            luta(forjadora_de_ossos, meu_jogador)
        
    locais()

##### Fluxo principal #####
def main_game_loop():
    while not meu_jogador.game_over:
        prompt()
    limpar_tela()
    if meu_jogador.game_over == True:
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

    game_over = '''
Você cai de joelhos, exausto. O frio da pedra contra sua pele é a única certeza que resta. 
A cada passo nesta descida, fragmentos de memória voltaram — rostos, batalhas, promessas esquecidas. 
E então, tudo retorna: o duelo contra o Lorde da Torre, a vitória amarga, a maldição lançada com seu último suspiro.
Ele apagou quem você era. Enfraqueceu sua alma. E agora, no fim da jornada, o corpo cede antes da libertação.

Você sorri, amargo. Lembrou... tarde demais.

Seus olhos se fecham. A torre, sentinela silenciosa, guarda mais uma história que ninguém ouvirá. 
Mas por um instante, apenas um... você foi inteiro outra vez
'''
    for caractere in game_over:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(0.001)
    sys.exit()

def fim_de_jogo():
    fala = '''
            O último golpe atravessa a carne etérea daquela criatura, que solta um grito abafado e cai de joelhos, 
           antes de finalmente se desfazer em poeira e silêncio. A torre inteira parece estremecer… mas não desaba. 
              Pelo contrário: o ar torna-se mais leve, como se uma antiga maldição tivesse sido, enfim, quebrada.
                                                Então… o silêncio absoluto.

    É nesse vazio que a verdade começa a emergir, lenta, inexorável, como a luz que penetra pelas frestas de uma porta esquecida. 
 Imagens invadem sua mente: o brilho de uma espada outrora empunhada com destreza; a lembrança de vitórias gravadas em sangue e suor; 
                         os rostos das criaturas que derrotou uma vez… e, sem saber, derrotou de novo.
                               E então, como um sussurro carregado pelo vento, você entende.
                                               Você era o herói. Sempre foi.

           O mesmo que, há muito tempo, escalou a torre, movido por coragem e destino. O mesmo que, no confronto final, 
     foi traído pelo último suspiro do Lorde, condenado a esquecer quem era, despido de sua força, de seu nome, de sua história.
           E agora… após cada degrau descido, cada monstro enfrentado, cada medo revivido… você reconstruiu a si mesmo.
                    A torre, que parecia um cárcere, revelou-se um caminho, não para escapar, mas para lembrar. 
                 Cada criatura que tombou não era apenas um obstáculo, mas um fragmento perdido de sua identidade, 
                            um pedaço da alma que o Lorde da torre de Arkyos tentou apagar... e falhou.

                     De pé, entre os escombros, você contempla os campos verdes através da porta agora aberta.
  Agora, com a memória restaurada e a essência resgatada, o caminho está livre. Não há mais monstros, não há mais medos… apenas você.
                      E enquanto os primeiros raios de um sol antigo atravessam os vitrais partidos da torre, 
                       você dá o primeiro passo… não como um prisioneiro, nem como uma sombra do que foi...
                                        mas como o herói que sempre foi destinado a ser.

Obrigado por jogar!!!'''
    for caractere in fala:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(0.001)
    sys.exit()
def setup_jogo():
    os.system('clear' if os.name != 'nt' else 'cls')

    pergunta1 = "\n Qual seu nome?\n"
    for caractere in pergunta1:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(0.001)
    meu_jogador.nome = input(">> ")

    pergunta2 = "Qual sua classe?\n(Escolha: "+Fore.YELLOW+"guerreiro"+Style.RESET_ALL+", "+Fore.YELLOW+"mago"+Style.RESET_ALL+" ou "+Fore.YELLOW+"monge"+Style.RESET_ALL+")\n"
    for caractere in pergunta2:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(0.001)

    classes_validas = ['guerreiro', 'mago', 'monge']
    jogador_classe = input(">> ").lower()
    while jogador_classe not in classes_validas:
        print(Fore.RED+"Classe inválida, tente novamente."+Style.RESET_ALL)
        jogador_classe = input(">> ").lower()
    meu_jogador.classe = jogador_classe
    classe = f"Classe selecionada: {meu_jogador.classe.capitalize()}\n"
    for caractere in classe:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(0.001)
    time.sleep(1.5)

    if meu_jogador.classe == 'guerreiro':
        # Adicione as poções de vida
        pocao_vida_baixa = lista_consumiveis[0]
        pocao_vida_media = lista_consumiveis[1]
        pocao_vida_alta = lista_consumiveis[2]
        
        # Arma padrão
        arma_padrao = lista_armas[1]
        
        # Armadura inicial para guerreiro
        armadura_inicial = lista_armaduras[0]
        
        # Atributos base
        meu_jogador.vida_base = 100
        meu_jogador.vida = meu_jogador.vida_base
        meu_jogador.vida_max = meu_jogador.vida
        meu_jogador.mana_base = 40
        meu_jogador.mana = meu_jogador.mana_base
        meu_jogador.mana_max = meu_jogador.mana
        meu_jogador.atk_base = 6
        meu_jogador.forca = 2
        
        # Equipar arma
        meu_jogador.item_equipado = Item(
            arma_padrao['nome'], 
            arma_padrao['atk'], 
            arma_padrao['desc'], 
            True, 
            arma_padrao['consumivel'], 
            arma_padrao['preco'], 
            arma_padrao['especial']
        )
        
        # Equipar armadura
        meu_jogador.armadura = Armadura(
            armadura_inicial['nome'],
            armadura_inicial['defesa'],
            armadura_inicial['vida_max'],
            armadura_inicial['resistencia'],
            armadura_inicial['desc'],
            True,  # Já equipada
            armadura_inicial['consumivel'],
            armadura_inicial['preco'],
            armadura_inicial['especial']
        )
        meu_jogador.armadura_vida = meu_jogador.armadura.vida_max
        
        # Adicionar itens à mochila
        meu_jogador.add_item(meu_jogador.item_equipado)
        meu_jogador.add_item(meu_jogador.armadura)
        meu_jogador.add_item(Item(
            pocao_vida_baixa['nome'], 
            pocao_vida_baixa['atk'], 
            pocao_vida_baixa['desc'], 
            pocao_vida_baixa['equipado'], 
            pocao_vida_baixa['consumivel'], 
            pocao_vida_baixa['preco'], 
            pocao_vida_baixa['especial']
        ))
        meu_jogador.add_item(Item(
            pocao_vida_media['nome'], 
            pocao_vida_media['atk'], 
            pocao_vida_media['desc'], 
            pocao_vida_media['equipado'], 
            pocao_vida_media['consumivel'], 
            pocao_vida_media['preco'], 
            pocao_vida_media['especial']
        ))
        meu_jogador.add_item(Item(
            pocao_vida_alta['nome'], 
            pocao_vida_alta['atk'], 
            pocao_vida_alta['desc'], 
            pocao_vida_alta['equipado'], 
            pocao_vida_alta['consumivel'], 
            pocao_vida_alta['preco'], 
            pocao_vida_alta['especial']
        ))
        
        # Calcular atributos finais
        calcular_atributos(meu_jogador)

    elif meu_jogador.classe == 'mago':
        pocao_vida_baixa = lista_consumiveis[0]
        pocao_vida_media = lista_consumiveis[1]
        pocao_mana_baixa = lista_consumiveis[3]
        pocao_mana_media = lista_consumiveis[4]
        arma_basica = lista_armas_magicas[0]
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
        meu_jogador.atk_base = 2
        meu_jogador.inteligencia = 3
        meu_jogador.atk = meu_jogador.atk_base
        meu_jogador.add_item(ArmaMagica(
            arma_basica['dano_magico'], arma_basica['nome'], arma_basica['atk'],
            arma_basica['desc'], arma_basica['equipado'], arma_basica['consumivel'],
            arma_basica['preco'], arma_basica['especial']
        ))
        meu_jogador.magias.append(Magia(magia_basica['nome'], magia_basica['dano'], magia_basica['desc'], magia_basica['mana_gasta'], efeito))
        meu_jogador.magias.append(Magia(magia_basica1['nome'], magia_basica1['dano'], magia_basica1['desc'], magia_basica1['mana_gasta'], efeito1))
        calcular_atributos(meu_jogador)
        meu_jogador.add_item(meu_jogador.item_equipado)
        meu_jogador.add_item(meu_jogador.armadura)
        meu_jogador.add_item(Item(
            pocao_vida_baixa['nome'], 
            pocao_vida_baixa['atk'], 
            pocao_vida_baixa['desc'], 
            pocao_vida_baixa['equipado'], 
            pocao_vida_baixa['consumivel'], 
            pocao_vida_baixa['preco'], 
            pocao_vida_baixa['especial']
        ))
        meu_jogador.add_item(Item(
            pocao_vida_media['nome'], 
            pocao_vida_media['atk'], 
            pocao_vida_media['desc'], 
            pocao_vida_media['equipado'], 
            pocao_vida_media['consumivel'], 
            pocao_vida_media['preco'], 
            pocao_vida_media['especial']
        ))
        meu_jogador.add_item(Item(
            pocao_mana_media['nome'], 
            pocao_mana_media['atk'], 
            pocao_mana_media['desc'], 
            pocao_mana_media['equipado'], 
            pocao_mana_media['consumivel'], 
            pocao_mana_media['preco'], 
            pocao_mana_media['especial']
        ))
        meu_jogador.add_item(Item(
            pocao_mana_baixa['nome'], 
            pocao_mana_baixa['atk'], 
            pocao_mana_baixa['desc'], 
            pocao_mana_baixa['equipado'], 
            pocao_mana_baixa['consumivel'], 
            pocao_mana_baixa['preco'], 
            pocao_mana_baixa['especial']
        ))

    elif meu_jogador.classe == 'monge':
        pocao_vida_baixa = lista_consumiveis[0]
        pocao_vida_media = lista_consumiveis[1]
        pocao_vida_alta = lista_consumiveis[2]
        meu_jogador.add_item(meu_jogador.item_equipado)
        meu_jogador.add_item(meu_jogador.armadura)
        meu_jogador.add_item(Item(
            pocao_vida_baixa['nome'], 
            pocao_vida_baixa['atk'], 
            pocao_vida_baixa['desc'], 
            pocao_vida_baixa['equipado'], 
            pocao_vida_baixa['consumivel'], 
            pocao_vida_baixa['preco'], 
            pocao_vida_baixa['especial']
        ))
        meu_jogador.add_item(Item(
            pocao_vida_media['nome'], 
            pocao_vida_media['atk'], 
            pocao_vida_media['desc'], 
            pocao_vida_media['equipado'], 
            pocao_vida_media['consumivel'], 
            pocao_vida_media['preco'], 
            pocao_vida_media['especial']
        ))
        meu_jogador.add_item(Item(
            pocao_vida_alta['nome'], 
            pocao_vida_alta['atk'], 
            pocao_vida_alta['desc'], 
            pocao_vida_alta['equipado'], 
            pocao_vida_alta['consumivel'], 
            pocao_vida_alta['preco'], 
            pocao_vida_alta['especial']
        ))
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
    fala2 = f"""
No topo de uma torre esquecida pelos deuses, alguém desperta entre ruínas e cinzas.
Sem memória, e com o corpo à beira do colapso, essa figura solitária encontra-se cercada por vestígios de uma batalha 
apocalíptica e por um silêncio que pesa como um túmulo.
Algo terrível aconteceu ali, mas não há ninguém para contar a história.

Com apenas fragmentos de poder e ecos de um passado perdido, {meu_jogador.nome} precisa descer os andares de uma Torre Misteriosa colossal.
A torre está repleta de criaturas corrompidas, armadilhas letais e segredos antigos.

A cada passo, a torre muda. A cada inimigo derrotado, algo esquecido retorna.
Mas algumas verdades talvez devam permanecer enterradas.

A jornada para escapar é também uma jornada para descobrir quem você é...
E por que o mundo parecia ter parado de girar no exato momento em que você caiu.\n"""

    for fala in [fala1, fala2]:
        for caractere in fala:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.001)
    time.sleep(1)
    input(Fore.YELLOW+'\n[Pressione Enter]'+Style.RESET_ALL)

    os.system('clear' if os.name != 'nt' else 'cls')
    print ("▬"*100)

    start_game()
    print_local()

##### Executar #####
tela_titulo()