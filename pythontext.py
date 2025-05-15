import cmd
import textwrap
import sys
import os
import time
import random
from utilitarios import(
    limpar_tela,
    loading,
    intervalo
)

#TO-DO:
'''
sistema de SPAWNAR MOSNTRO POR SALA
sistema de VENDA DE ITENS DA MOCHILA
'''
######### Setup do jogador ########
#ainda to vendo os arquivos

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
    
    def add_item(self, item):
        self.mochila.append(item)
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
    print(f'{jogador.nome} subiu de nivel para #{jogador.nivel}!!!')
    pontos = 0
    while jogador.xp >= jogador.xp_max:
        pontos += 3
        resto_xp = jogador.xp - jogador.xp_max
        jogador.xp = resto_xp
        jogador.xp_max +=50
    while pontos > 0:
        print(f'Pontos restantes: {pontos}')
        escolha = input("Aumentar Forca (for), Fortitude (fort) ou Inteligência (int): ").lower()
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
            print('Comando invádido')
            continue
        pontos -= 1
    atualizar_atributos(meu_jogador)

def exibir_status(jogador):
    limpar_tela()
    print('▬'*60)
    print('STATUS'.upper())
    print(f'{jogador.nome} LVL:{jogador.nivel} XP: {jogador.xp}/{jogador.xp_max}')
    print(f'vida: {jogador.vida}/{jogador.vida_max} ATK: {jogador.atk}/MAG.ATK: {jogador.dano_magico}/ MANA: {jogador.mana}/{jogador.mana_max}')
    if jogador.item_equipado:
        print(f'arma: {jogador.item_equipado.nome} ATK: {jogador.item_equipado.atk}')
    else:
        print('arma: sem arma equipada')
    print(f'forca: {jogador.forca} fortitude: {jogador.fortitude} inteligência: {jogador.inteligencia}')


class Monstro:
    def __init__(self, nome, vida, nivel, atk, xp, ouro):
        self.nome = nome
        self.vida = vida*nivel
        self.vida_max = vida*nivel
        self.nivel = nivel
        self.atk = atk
        self.xp = xp
        self.ouro = ouro
        self.item = arma_aleatoria()

def encontro_aleatorio():
    if meu_jogador.local != 'b1':
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
    return Monstro(monstro_invocacao['nome'], monstro_invocacao['vida'], monstro_invocacao['nivel'], monstro_invocacao['atk'], monstro_invocacao['xp'], monstro_invocacao['ouro'])

def experiencia(monstro):
    meu_jogador.xp += monstro.xp
    if meu_jogador.xp >= meu_jogador.xp_max:
        subi_nivel(meu_jogador)

class Item:
    def __init__(self, nome, atk, desc, equipado, consumivel, preco):
        self.nome = nome
        self.atk = atk
        self.desc = desc
        self.equipado = equipado
        self.consumivel = consumivel
        self.preco = preco
    
class Magia:
    def __init__(self, nome, dano, desc, mana_gasta):
        self.nome = nome
        self.dano = dano
        self.desc = desc
        self.mana_gasta = mana_gasta 

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
        escolha = input('>>').lower()
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
            acao = input('>>')
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
    escolha = input('>>').lower()
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
        acao = input('>>')
        if acao not in ['vender', 'voltar', 'fechar']:
            print('**COMANDO INVÁLIDO**')
            vender_item()
        if acao == 'vender':
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
    { 'nome': 'Espada de ferro', 'atk': 5, 'preco': 100, 'desc': 'Uma espada de ferro, muito forte.', 'item': 'espada de ferro', 'comprado': False, 'equipado': False, 'consumivel': False},
    { 'nome': 'Arco longo', 'atk': 4,'preco': 100, 'desc': 'Um arco longo, muito forte.', 'item': 'arco longo', 'comprado': False, 'equipado': False, 'consumivel': False},
    { 'nome': 'Pocao de vida baixa', 'atk': 0,'preco': 50, 'desc': 'Uma pocao de vida baixa, cura 15 pontos de vida.', 'item': 'pocao de vida baixa', 'comprado': False, 'equipado': False, 'consumivel': True},
    { 'nome': 'Pocao de vida media', 'atk': 0,'preco': 100, 'desc': 'Uma pocao de vida media, cura 30 pontos de vida.', 'item': 'pocao de vida media', 'comprado': False, 'equipado': False, 'consumivel': True},
    { 'nome': 'Pocao de vida alta', 'atk': 0,'preco': 150, 'desc': 'Uma pocao de vida alta, cura 60 pontos de vida.', 'item': 'pocao de vida alta', 'comprado': False, 'equipado': False, 'consumivel': True},
    { 'nome': 'Pocao de mana baixa', 'atk': 0,'preco': 50, 'desc': 'Uma pocao de mana baixa, cura 20 pontos de mana.', 'item': 'pocao de mana baixa', 'comprado': False, 'equipado': False, 'consumivel': True},
    { 'nome': 'Pocao de mana media', 'atk': 0,'preco': 50, 'desc': 'Uma pocao de mana media, cura 20 pontos de mana.', 'item': 'pocao de mana media', 'comprado': False, 'equipado': False, 'consumivel': True},
    { 'nome': 'Pocao de mana alta', 'atk': 0,'preco': 50, 'desc': 'Uma pocao de mana alta, cura 20 pontos de mana.', 'item': 'pocao de mana alta', 'comprado': False, 'equipado': False, 'consumivel': True},
]

lista_consumiveis = [
    { 'nome': 'Pocao de vida baixa', 'atk': 0,'preco': 50, 'desc': 'Uma pocao de vida, cura 15 pontos de vida.', 'equipado': False, 'consumivel': True},
    { 'nome': 'Pocao de vida media', 'atk': 0,'preco': 100, 'desc': 'Uma pocao de vida media, cura 30 pontos de vida.', 'comprado': False, 'equipado': False, 'consumivel': True},
    { 'nome': 'Pocao de vida alta', 'atk': 0,'preco': 150, 'desc': 'Uma pocao de vida alta, cura 60 pontos de vida.', 'comprado': False, 'equipado': False, 'consumivel': True},
    { 'nome': 'Pocao de mana baixa', 'atk': 0,'preco': 50, 'desc': 'Uma pocao de mana, cura 15 pontos de mana.', 'equipado': False, 'consumivel': True},
    { 'nome': 'Pocao de mana media', 'atk': 0,'preco': 100, 'desc': 'Uma pocao de mana media, cura 30 pontos de mana.', 'comprado': False, 'equipado': False, 'consumivel': True},
    { 'nome': 'Pocao de mana alta', 'atk': 0,'preco': 150, 'desc': 'Uma pocao de mana alta, cura 60 pontos de mana.', 'comprado': False, 'equipado': False, 'consumivel': True},
]

lista_armas = [
    {'nome': 'Adaga enferrujada', 'atk': 3, 'preco': 100, 'desc': 'Parece ser bem antiga', 'equipado': False, 'consumivel': False},
    {'nome': 'Varinha capenga', 'atk': 3, 'preco': 100, 'desc': 'É nova, mas bem barata', 'equipado': False, 'consumivel': False},
    {'nome': 'Espada longa', 'atk': 4, 'preco': 100, 'desc': 'A espada de todo guerreiro.', 'equipado': False, 'consumivel': False},
    {'nome': 'Grimório', 'atk': 2, 'preco': 100, 'desc': 'O grimório de um mago, o local de sua sabedoria.', 'equipado': False, 'consumivel': False},
]

lista_itens_especiais = [
    {'nome': 'Anel Desconhecido', 'atk': 0, 'preco': 00, 'desc': 'Um anel feito de ouro. Sua origem é desconhecida.', 'equipado': False, 'consumivel': False},
    
]

lista_magias = [
    {'nome': 'Bola de fogo', 'dano': 20, 'desc':'A magia mais forte de um mago', 'mana_gasta': 30}
]

lista_monstros_normais = [
    {'nome': 'slime', 'vida': 10, 'nivel': 1, 'atk': 2, 'xp': 150, 'ouro': 100},
    {'nome': 'goblin', 'vida': 20, 'nivel': 2, 'atk': 4, 'xp': 100, 'ouro': 200},
    {'nome': 'lobo selvagem', 'vida': 25, 'nivel': 3, 'atk': 5, 'xp': 15, 'ouro': 100},
    {'nome': 'esqueleto', 'vida': 30, 'nivel': 4, 'atk': 6, 'xp': 20, 'ouro': 200},
    {'nome': 'zumbi', 'vida': 35, 'nivel': 4, 'atk': 4, 'xp': 18, 'ouro': 100},
    {'nome': 'morcego gigante', 'vida': 28, 'nivel': 3, 'atk': 6, 'xp': 12, 'ouro': 200},
    {'nome': 'aranha venenosa', 'vida': 22, 'nivel': 2, 'atk': 7, 'xp': 14, 'ouro': 100},
    {'nome': 'orc', 'vida': 40, 'nivel': 5, 'atk': 8, 'xp': 25, 'ouro': 200},
    {'nome': 'troll da caverna', 'vida': 50, 'nivel': 6, 'atk': 10, 'xp': 30, 'ouro': 300},
    {'nome': 'gárgula', 'vida': 45, 'nivel': 5, 'atk': 9, 'xp': 28, 'ouro': 200}
]
lista_monstros_invocacoes = [
    {'nome': 'Tieflíngs', 'vida': 50, 'nivel': 5, 'atk': 5, 'xp': 50, 'ouro': 10},
    {'nome': 'Tieflíngs', 'vida': 50, 'nivel': 6, 'atk': 6, 'xp': 60, 'ouro': 15},
    {'nome': 'Demônio Inferior', 'vida': 50, 'nivel': 7, 'atk': 7, 'xp': 70, 'ouro': 20},
    {'nome': 'Demônio Inferior', 'vida': 50, 'nivel': 8, 'atk': 8, 'xp': 80, 'ouro': 25},
    {'nome': 'Demoníaco', 'vida': 50, 'nivel': 9, 'atk': 9, 'xp': 90, 'ouro': 30},
    {'nome': 'Demoníaco', 'vida': 50, 'nivel': 10, 'atk': 10, 'xp': 100, 'ouro': 35},
    
]

def arma_aleatoria():
    chances = [30, 30, 20, 20]
    arma_random = random.choices(lista_armas, weights=chances, k=1)[0]
    arma = Item(arma_random['nome'], arma_random['atk'], arma_random['desc'], arma_random['equipado'], arma_random['consumivel'], arma_random['preco'])
    return arma

monstro = lista_monstros_normais[0]
monstro2 = lista_monstros_normais[1]
monstro_exemplo = Monstro(monstro['nome'], monstro['vida'], monstro['nivel'], monstro['atk'], monstro['xp'], monstro['ouro'])
monstro_exemplo2 = Monstro(monstro2['nome'], monstro2['vida'], monstro2['nivel'], monstro2['atk'], monstro2['xp'], monstro2['ouro'])


######### Tela de título #########

def navegação_tela_titulo():
    opção = input(">").lower()
    while opção not in ['jogar', 'ajuda', 'sair']:
        print("Por favor, utilize um comando válido.")
        opção = input(">").lower()
    if opção == "jogar":
        setup_jogo()
    elif opção == "ajuda":
        ajuda_menu()
    elif opção == "sair":
        sair()

def tela_titulo():
    limpar_tela()
    titulo ='''
            #########################
            # >Bem vindo ao ARKYOS! #
            #########################
 '''
    opcoes = '''
                   - Jogar -        
                   - Ajuda -        
                   - Sair  -      
            
          '''
    for titulo1 in titulo:
        sys.stdout.write(titulo1)
        sys.stdout.flush()
        time.sleep(0.01)
    for opcao in opcoes:
        sys.stdout.write(opcao)
        sys.stdout.flush()
        time.sleep(0.01)

    navegação_tela_titulo()

def ajuda_menu():
    limpar_tela()
    print('''
          #########################
          # >Bem vindo ao ARKYOS! #
          #########################'
          
  principais comandos: [mover / olhar / mochila / status / mapa]
          
    - Digite mover para se movimentar
    - Digite seus comandos para executá-los
    - Use o comando "olhar" para examinar a área algo
    - Boa sorte e não morra :p
          ''')
    if meu_jogador.nome != '':
        print('Voltar ao game? [s/n]')
        voltar_game = input('>>').lower()
        if voltar_game != 's':
            limpar_tela()
            ajuda_menu()
        print_local()
        main_game_loop()
    print("- voltar ao MENU? [s/n]")
    voltar_menu = input('>>').lower()
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
        'EXAMINAR': 'Tudo ao seu redor parece morto.\n   Porem voce nota um brilho fraco vindo de frente de um trono destruido.\n Digite trono para examinar o trono.',
        'SOLVED': False,
        'SUBIR': '',
        'DESCER': '',
        'AVANÇAR': 'a2',
        'RETORNAR': '',
        'MONSTRO': '',

        'LOCAIS': ['trono', 'bau'],
    },
    'a2': {
        'NOME_LOCAL': "Sala2",
        'DESCRICAO': 'Descrição da sala 2.',
        'EXAMINAR': 'Você observa objetos antigos.',
        'SOLVED': False,
        'SUBIR': '',
        'DESCER': 'b1',
        'AVANÇAR': '',
        'RETORNAR': 'a1',
        'MONSTRO': monstro_exemplo
    },
    'b1': { 
        'NOME_LOCAL': "Sala1 Segundo andar",
        'DESCRICAO': 'Descrição da sala b1.',
        'EXAMINAR': 'Uma escada quebrada e mobília velha.',
        'SOLVED': False,
        'SUBIR': 'a2',
        'DESCER': '',
        'AVANÇAR': 'b2',
        'RETORNAR': '',
        'MONSTRO': monstro_exemplo2
    },
    'b2': {
        'NOME_LOCAL': "LOJA",
        'DESCRICAO': 'Descrição da sala b2.',
        'EXAMINAR': 'Rochas espalhadas pelo chão.',
        'SOLVED': False,
        'SUBIR': '',
        'DESCER': 'c1',
        'AVANÇAR': '',
        'RETORNAR': 'b1',
        'MONSTRO': ''
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
        'MONSTRO': ''
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
        'MONSTRO': ''
    },
}

def mostrar_mapa():
    if meu_jogador.local == 'a1':
        limpar_tela()
        print('▬'*60)
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
    


#mapa mental dos andares:
#|a1|a2|
#|b1|b2|
#|c2|c1|
#Começamos em a1

##### Interações em jogo #####

def print_local():
    if meu_jogador.local != 'a1':
        limpar_tela()
    local_nome = mapa[meu_jogador.local]['NOME_LOCAL']
    local_desc = mapa[meu_jogador.local]['DESCRICAO']
    print('\n' + ('▬' * 60), '\n')
    print(f"{local_nome.upper()}")
    print(f"{local_desc} \n")
    print('▬' * 60)
    mostrar_status(meu_jogador)
    if mapa[meu_jogador.local]['MONSTRO'] != '':
        print(f"há um {mapa[meu_jogador.local]['MONSTRO'].nome} na sala. O que deseja fazer?\n[lutar / fugir / falar]")
        escolha = input(">>").lower()
        if escolha not in ['lutar', 'fugir', 'falar']:
            print_local()
        acao_luta(escolha, mapa[meu_jogador.local]['MONSTRO'])
    main_game_loop()

def prompt():
    print("\n" + "▬"*60)
    print("O que deseja fazer?")
    acao = input(">>").lower()
    acoes_aceitas = ['invocar','status', 'mover', 'loja', 'sair', 'ajuda', 'olhar', 'inspecionar', 'teleportar', 'dormir', 'mochila', 'mapa']
    while acao not in acoes_aceitas:
        print("Ação inválida, tente novamente.\n")
        acao = input(">> ").lower()
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
        acao_loja(input('>>').lower())
    elif acao == 'status':
        exibir_status(meu_jogador)
    elif acao == 'mapa':
        mostrar_mapa()
    elif acao == 'invocar':
        encontro_aleatorio()
    
def acao_loja(escolha):
    if escolha == 'comprar':
        comprar()
    elif escolha == 'vender':
        vender()

def locais():
    print('O que deseja fazer?')
    acao = input('>>').lower()
    acaoes_aceitas = mapa[meu_jogador.local]['LOCAIS']
    while acao not in acaoes_aceitas:
        print('Acao inválida, tente novamente.')
        acao = input('>>').lower()
        if acao == 'trono':
            trono()
        else:
            print('Acao inválida, tente novamente.')
            locais()
            
### Objetos interativos dos andares ###

def trono():
    
    print('▬'*60)
    print('Você vai até o brilho e vê um anel dourado.\n  ao toca-lo um frio intenso percorre seu braço.\n  Seu dedo o aceita sem resistência, como se ele sentisse que voce era o seu Dono.\n')
    item = lista_itens_especiais[0]
    meu_jogador.add_item(item['nome'], item['atk'], item['desc'], item['equipado'], item['consumivel'], item['preco'])
    print('Anel desconhecido adicionado ao seu inventario!')
    mapa[meu_jogador.local]['SOLVED'] = True
    intervalo()
    main_game_loop()

########################################

def comprar(escolha):
        lista_itens_loja[escolha]['comprado'] = True
        item = lista_itens_loja[escolha]
        item_add = Item(item['nome'], item['atk'], item['desc'], item['equipado'], item['consumivel'], item['preco'])
        print(f'**VOCE COMPROU {item_add.nome}**')
        meu_jogador.add_item(item_add)
        meu_jogador.ouro -= lista_itens_loja[escolha]['preco']
        mostrar_loja()
    
def vender(self):
    self.vendido = True

def sair():
    print("Tem certeza que deseja sair? [s/n] ")
    confirmar = input('>>').lower()
    if confirmar not in ['s', 'n']:
        print('\ncomando inválido')
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
        print(f'O {monstro.nome} não te entende e te ataca')
        intervalo()
        meu_jogador.vida -= monstro.atk
        luta(monstro, meu_jogador)

def abrir_mochila():
    if meu_jogador.game_over:
        return
        main_game_loop() 
    if meu_jogador.mochila:
        print (f'Ouro: {meu_jogador.ouro}')
        for i in range(len(meu_jogador.mochila)):
            if meu_jogador.mochila[i].consumivel:
                print(f'{i+1}. {meu_jogador.mochila[i].nome} desc: {meu_jogador.mochila[i].desc}')
                continue
            if meu_jogador.mochila[i].equipado == True:
                print(f'{i+1}. {meu_jogador.mochila[i].nome} ATK: {meu_jogador.mochila[i].atk} desc: {meu_jogador.mochila[i].desc} (EQUIPADO)')
                continue
            print(f'{i+1}. {meu_jogador.mochila[i].nome} ATK: {meu_jogador.mochila[i].atk} desc: {meu_jogador.mochila[i].desc}')
        print('>> Use números para selecionar os itens ou [fechar]')
        escolha = input(">>")
        if escolha == 'fechar':
            print_local()
        try:
            escolha = int(escolha)-1
            if escolha not in range(0, len(meu_jogador.mochila)):
                abrir_mochila()
            print(f'item: {meu_jogador.mochila[escolha].nome} ATK: {meu_jogador.mochila[escolha].atk}')
            # jogador selecionou com item equipao
            if meu_jogador.item_equipado:
                # jogador selecionou item equipado
                if meu_jogador.mochila[escolha].equipado == True:
                    print('[desequipar / remover / fechar]')
                    acao = input('>>').lower()
                    if acao not in ['desequipar', 'remover', 'fechar']:
                        print('\ncomando inválido')
                        abrir_mochila()
                    
                    if acao == 'desequipar':
                        print(f'**VOCÊ DESEQUIPOU {meu_jogador.item_equipado.nome}**')
                        meu_jogador.item_equipado = False
                        meu_jogador.mochila[escolha].equipado = False
                        meu_jogador.atk_final = meu_jogador.atk
                        abrir_mochila()
                    elif acao == 'remover':
                        print(f'**VOCÊ DESEQUIPOU {meu_jogador.item_equipado.nome}**')
                        print(f'**VOCÊ DROPOU {meu_jogador.item_equipado.nome}**')
                        meu_jogador.item_equipado = None
                        meu_jogador.mochila.pop(escolha)
                        meu_jogador.atk_final = meu_jogador.atk
                        abrir_mochila()
                    elif acao == 'fechar':
                        print_local()
                # jogador selecionou item NÂO equipado
                else:
                    if meu_jogador.mochila[escolha].consumivel:
                        print( '[usar / remover / fechar]')
                        acao = input('>>').lower()
                        if acao not in ['usar', 'remover', 'fechar']:
                            print('\ncomando inválido')
                            abrir_mochila()
                        if acao == 'usar':
                            if meu_jogador.mochila[escolha].nome == 'Pocao de vida baixa':
                                pocao_vida()
                                meu_jogador.mochila.pop(escolha)
                                main_game_loop()
                            elif meu_jogador.mochila[escolha].nome == 'Pocao de vida media':
                                pocao_vida_media()
                                meu_jogador.mochila.pop(escolha)
                                main_game_loop()
                            elif meu_jogador.mochila[escolha].nome == 'Pocao de vida alta':
                                pocao_vida_alta()
                                meu_jogador.mochila.pop(escolha)
                                main_game_loop()

                            elif meu_jogador.mochila[escolha].nome == 'Pocao de mana baixa':
                                pocao_mana()
                                meu_jogador.mochila.pop(escolha)
                                main_game_loop()
                            elif meu_jogador.mochila[escolha].nome == 'Pocao de mana media':
                                pocao_mana_media()
                                meu_jogador.mochila.pop(escolha)
                                main_game_loop()
                            elif meu_jogador.mochila[escolha].nome == 'Pocao de mana alta':
                                pocao_mana_alta()
                                meu_jogador.mochila.pop(escolha)
                                main_game_loop()
                            
                    print('[equipar / remover / fechar]')
                    
                    acao = input('>>').lower()
                    if acao not in ['equipar', 'remover', 'fechar']:
                        print('\ncomando inválido')
                        abrir_mochila()

                    if acao == 'equipar':
                        print(f'**VOCÊ DESEQUIPOU {meu_jogador.item_equipado.nome}**')
                        for i in range(len(meu_jogador.mochila)):
                            if meu_jogador.mochila[i].equipado == True:
                                meu_jogador.mochila[i].equipado = False
                                break
                        meu_jogador.item_equipado = meu_jogador.mochila[escolha]
                        meu_jogador.mochila[escolha].equipado = True
                        meu_jogador.atk_final = meu_jogador.atk + meu_jogador.item_equipado.atk
                        print(f'**VOCÊ EQUIPOU {meu_jogador.item_equipado.nome}**')
                        abrir_mochila()
                    elif acao == 'remover':
                        print(f'**VOCÊ DROPOU {meu_jogador.mochila[escolha].nome}')
                        meu_jogador.mochila.pop(escolha)
                        abrir_mochila()
                    elif acao == 'fechar':
                        print_local()
                        main_game_loop()
            # jogador selecionou sem item equipado
            else:
                if meu_jogador.mochila[escolha].consumivel:
                        print( '[usar / remover / fechar]')
                        acao = input('>>').lower()
                        if acao not in ['usar', 'remover', 'fechar']:
                            print('\ncomando inválido')
                            abrir_mochila()
                        if acao == 'usar':
                            if meu_jogador.mochila[escolha].nome == 'Pocao de vida baixa':
                                pocao_vida()
                                meu_jogador.mochila.pop(escolha)
                                main_game_loop()
                            elif meu_jogador.mochila[escolha].nome == 'Pocao de vida media':
                                pocao_vida_media()
                                meu_jogador.mochila.pop(escolha)
                                main_game_loop()
                            elif meu_jogador.mochila[escolha].nome == 'Pocao de vida alta':
                                pocao_vida_alta()
                                meu_jogador.mochila.pop(escolha)
                                main_game_loop()
                            elif meu_jogador.mochila[escolha].nome == 'Pocao de mana baixa':
                                pocao_mana()
                                meu_jogador.mochila.pop(escolha)
                                main_game_loop()
                            elif meu_jogador.mochila[escolha].nome == 'Pocao de mana media':
                                pocao_mana_media()
                                meu_jogador.mochila.pop(escolha)
                                main_game_loop()
                            elif meu_jogador.mochila[escolha].nome == 'Pocao de mana alta':
                                pocao_mana_alta()
                                meu_jogador.mochila.pop(escolha)
                                main_game_loop()
                print('[equipar / remover / fechar]')
                acao = input('>>').lower()
                if acao not in ['equipar', 'remover', 'fechar']:
                    print('\ncomando inválido')
                    abrir_mochila()
                
                if acao == 'equipar':
                    meu_jogador.mochila[escolha].equipado = True
                    meu_jogador.item_equipado = meu_jogador.mochila[escolha]
                    meu_jogador.atk_final = meu_jogador.item_equipado.atk + meu_jogador.atk
                    print(F'**VOCÊ EQUIPOU {meu_jogador.item_equipado.nome}**')
                    abrir_mochila()
                elif acao == 'remover':
                    print(f'**VOCÊ DROPOU {meu_jogador.mochila[escolha].nome}')
                    meu_jogador.mochila.pop(escolha)
                    abrir_mochila()
                elif acao == 'fechar':
                    print_local()
        except:
            abrir_mochila()
    else:
        print("Mochila vazia")

def luta(monstro, meu_jogador):
    print(f'\n{monstro.nome} #{monstro.nivel}')
    print(f'vida: {monstro.vida}/{monstro.vida_max} ATK: {monstro.atk}')
    mostrar_status(meu_jogador)
    print('atacar / magia / fugir')
    acao = input(">>").lower()
    if acao not in ['atacar', 'magia', 'fugir']:
        limpar_tela()
        print("comando invádido".upper())
        luta(monstro, meu_jogador)
    if acao == 'atacar':
        monstro.vida -= meu_jogador.atk_final
        print(f"você ataca {monstro.nome}\n")
        loading()
        intervalo()
        
        if monstro.vida > 0:
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
                print(f'Você lança {meu_jogador.magias[escolha].nome} em {monstro.nome}')
                loading()
                intervalo()

                if monstro.vida > 0:
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
    elif acao == 'fugir':
        fugir()
    
    if meu_jogador.vida > 0 and monstro.vida > 0:
        luta(monstro, meu_jogador)
        
    if meu_jogador.vida <= 0:
        meu_jogador.local = 'a1'
        meu_jogador.vida = meu_jogador.vida_max
        limpar_tela()
        print('Você morreu e acorda na sala inicial')
    elif monstro.vida <= 0:
        limpar_tela()
        print(f'VOCÊ DERROTOU {monstro.nome}')
        experiencia(monstro)
        if random.random() < 0.3:
            drop(monstro)
        mapa[meu_jogador.local]['MONSTRO'] = ''
        print_local()
        main_game_loop()

def drop(monstro):
    print(f'Você ganhou {monstro.ouro} e o {monstro.nome} dropou {monstro.item.nome}')
    meu_jogador.ouro += monstro.ouro
    print('[pegar / ignorar]')
    acao = input('>>').lower()
    if acao not in ['pegar', 'ignorar']:
        print('\ncomando inválido')
        drop(monstro)
    
    if acao == 'pegar':
        mapa[meu_jogador.local]['MONSTRO'] = ''
        meu_jogador.add_item(monstro.item)
        print_local()
        main_game_loop()
    elif acao == 'ignorar':
        mapa[meu_jogador.local]['MONSTRO'] = ''
        print('você ignora o item e segue viagem')
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
    print('▬'*60)
    print(f'{self.nome} LVL:{self.nivel} XP: {self.xp}/{self.xp_max}')
    print(f'vida: {self.vida}/{self.vida_max} ATK: {self.atk} MANA: {self.mana}/{self.mana_max}')
    if self.item_equipado:
        print(f'arma: {self.item_equipado.nome} ATK: {self.item_equipado.atk}')
    else:
        print('arma: sem arma equipada')

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
        fala = 'Você não consegue passar pela porta, alguma energia estranha te impede'
        for falas in fala:
            sys.stdout.write(falas)
            sys.stdout.flush()
            time.sleep(0.01)
        time.sleep(1)
        main_game_loop()
    elif meu_jogador.local == 'a1':
        pergunta = "Avançar para a próxima sala? (escreva avançar)\n >>"
    elif meu_jogador.local in ['b1', 'c1']:
        pergunta = "Avançar para a próxima sala ou subir as escadas e voltar a sala anterior? (escreva: avançar ou subir)\n>>"
    elif meu_jogador.local in ['a2', 'c2']:
        pergunta = "Descer as escadas ou retornar a sala anterior? (escreva: descer ou retornar)\n>>"
    elif meu_jogador.local in ['b2']:
        pergunta = "Há uma loja no andar. para onde deseja se mover? (escreva: loja, descer ou retornar)\n>>"
    
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
    print(f"\nVocê se moveu para {destino}.")
    meu_jogador.local = destino
    print_local()

def jogador_examinar():
    print(mapa[meu_jogador.local]['EXAMINAR'])
    mapa[meu_jogador.local]['SOLVED'] = True
    locais()

##### Fluxo principal #####

def main_game_loop():
    while not meu_jogador.game_over:
        prompt()
        # Aqui tratar se os enigmas foram resolvidos, chefe derrotado, tudo explorado, etc.
    limpar_tela()
    print("\n\n**FIM DE JOGO**")
    sys.exit()
    exit()
    limpar_tela()
    print("\n\n**FIM DE JOGO**")

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
        meu_jogador.atk = meu_jogador.atk_base
        meu_jogador.item_equipado = Item(arma_padrao['nome'], arma_padrao['atk'], arma_padrao['desc'], True, arma_padrao['consumivel'], arma_padrao['preco'])
        meu_jogador.add_item(meu_jogador.item_equipado)
        meu_jogador.atk_final = meu_jogador.atk + meu_jogador.item_equipado.atk
        meu_jogador.add_item(Item(pocao_vida_baixa['nome'], pocao_vida_baixa['atk'], pocao_vida_baixa['desc'], pocao_vida_baixa['equipado'], pocao_vida_baixa['consumivel'], pocao_vida_baixa['preco']))
        meu_jogador.add_item(Item(pocao_vida_media['nome'], pocao_vida_media['atk'], pocao_vida_media['desc'], pocao_vida_media['equipado'], pocao_vida_media['consumivel'], pocao_vida_media['preco']))
        meu_jogador.add_item(Item(pocao_vida_alta['nome'], pocao_vida_alta['atk'], pocao_vida_alta['desc'], pocao_vida_alta['equipado'], pocao_vida_alta['consumivel'], pocao_vida_alta['preco']))
        calcular_atributos(meu_jogador)

    elif meu_jogador.classe == 'mago':
        pocao_mana_baixa = lista_consumiveis[3]
        pocao_mana_media = lista_consumiveis[4]
        pocao_mana_alta = lista_consumiveis[5]
        magia_basica = lista_magias[0]
        meu_jogador.vida_base = 50
        meu_jogador.vida = meu_jogador.vida_base
        meu_jogador.vida_max = meu_jogador.vida
        meu_jogador.mana_base = 100
        meu_jogador.mana = meu_jogador.mana_base
        meu_jogador.mana_max = meu_jogador.mana
        meu_jogador.atk_base = 5
        meu_jogador.atk = meu_jogador.atk_base
        meu_jogador.magias.append(Magia(magia_basica['nome'], magia_basica['dano'], magia_basica['desc'], magia_basica['mana_gasta']))
        meu_jogador.add_item(Item(pocao_mana_baixa['nome'], pocao_mana_baixa['atk'], pocao_mana_baixa['desc'], pocao_mana_baixa['equipado'], pocao_mana_baixa['consumivel'], pocao_mana_baixa['preco']))
        meu_jogador.add_item(Item(pocao_mana_media['nome'], pocao_mana_media['atk'], pocao_mana_media['desc'], pocao_mana_media['equipado'], pocao_mana_media['consumivel'], pocao_mana_media['preco']))
        meu_jogador.add_item(Item(pocao_mana_alta['nome'], pocao_mana_alta['atk'], pocao_mana_alta['desc'], pocao_mana_alta['equipado'], pocao_mana_alta['consumivel'], pocao_mana_alta['preco']))
        calcular_atributos(meu_jogador)

    elif meu_jogador.classe == 'monge':
        meu_jogador.vida_base = 150
        meu_jogador.vida = meu_jogador.vida_base
        meu_jogador.vida_max = meu_jogador.vida
        meu_jogador.mana_base = 0
        meu_jogador.mana = meu_jogador.mana_base
        meu_jogador.mana_max = meu_jogador.mana
        meu_jogador.atk_base = 9
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
    print ("=====================================")
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