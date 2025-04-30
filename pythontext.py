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
bug: abrir mochila -> equipar/desequipar item -> fechar mochila -> sair(fechar jogo) -> abre mochila, mas quando sair de novo vai sair
sistema de EQUIPAR, DESEQUIPAR, REMOVER
sistema de GANHAR XP, SUBIR NIVEL
sistema de SPAWNAR MOSNTRO POR SALA
sistema de magias
comando de ver MAPA
'''
######### Setup do jogador ########

class Player:
    def __init__(self):
        self.nome = ''
        self.classe = ''
        self.nivel = 1
        self.vida = 0
        self.vida_max = self.vida
        self.mana = 0
        self.mana_max = self.mana
        self.atk = 5
        self.atk_final = self.atk
        self.item_equipado = None
        self.mochila = []
        self.efeitos_status = []
        self.magias = []
        self.local = 'começo'
        self.game_over = False
    
    def add_item(self, item):
        self.mochila.append(item)

class Monstro:
    def __init__(self, nome, vida, nivel, atk, xp):
        self.nome = nome
        self.vida = vida*nivel
        self.vida_max = vida*nivel
        self.nivel = nivel
        self.atk = atk
        self.xp = xp
        self.item = arma_aleatoria()

class Arma:
    def __init__(self, nome, atk, desc, equipado):
        self.nome = nome
        self.atk = atk
        self.desc = desc
        self.equipado = equipado

lista_armas = [
    {'nome': 'Adaga enferrujada', 'atk': 3, 'desc': 'Parece ser bem antiga', 'equipado': False},
    {'nome': 'Varinha capenga', 'atk': 3, 'desc': 'É nova, mas bem barata', 'equipado': False},
    {'nome': 'Espada longa', 'atk': 4, 'desc': 'A espada de todo guerreiro.', 'equipado': False},
    {'nome': 'Grimório', 'atk': 2, 'desc': 'O grimório de um mago, o local de sua sabedoria.', 'equipado': False},
]

class magias:
    def __init__(self, nome, dano, desc, mana_gasta):
        self.nome = nome
        self.dano = dano
        self.desc = desc
        self.mana_gasta = mana_gasta

lista_magias = [
    {'nome': 'Bola de fogo', 'dano': 20, 'desc':'A magia mais forte de um mago', 'mana_gasta': 30}
]

lista_monstros_normais = [
    {'nome': 'slime', 'vida': 10, 'nivel': 1, 'atk': 2, 'xp': 5},
    {'nome': 'goblin', 'vida': 20, 'nivel': 2, 'atk': 4, 'xp': 10},
    {'nome': 'lobo selvagem', 'vida': 25, 'nivel': 3, 'atk': 5, 'xp': 15},
    {'nome': 'esqueleto', 'vida': 30, 'nivel': 4, 'atk': 6, 'xp': 20},
    {'nome': 'zumbi', 'vida': 35, 'nivel': 4, 'atk': 4, 'xp': 18},
    {'nome': 'morcego gigante', 'vida': 28, 'nivel': 3, 'atk': 6, 'xp': 12},
    {'nome': 'aranha venenosa', 'vida': 22, 'nivel': 2, 'atk': 7, 'xp': 14},
    {'nome': 'orc', 'vida': 40, 'nivel': 5, 'atk': 8, 'xp': 25},
    {'nome': 'troll da caverna', 'vida': 50, 'nivel': 6, 'atk': 10, 'xp': 30},
    {'nome': 'gárgula', 'vida': 45, 'nivel': 5, 'atk': 9, 'xp': 28}
]

def arma_aleatoria():
    chances = [30, 30, 20, 20]
    arma_random = random.choices(lista_armas, weights=chances, k=1)[0]
    arma = Arma(arma_random['nome'], arma_random['atk'], arma_random['desc'], arma_random['equipado'])
    return arma

monstro = lista_monstros_normais[0]
monstro2 = lista_monstros_normais[1]
monstro_exemplo = Monstro(monstro['nome'], monstro['vida'], monstro['nivel'], monstro['atk'], monstro['xp'])
monstro_exemplo2 = Monstro(monstro2['nome'], monstro2['vida'], monstro2['nivel'], monstro2['atk'], monstro2['xp'])
meu_jogador = Player()

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
    print('#########################')
    print('# >Bem vindo ao ARKYOS! #')
    print('#########################')
    print('        - Jogar -        ')
    print('        - Ajuda -        ')
    print('        - Sair  -        ')
    navegação_tela_titulo()

def ajuda_menu():
    limpar_tela()
    print('#########################')
    print('# >Bem vindo ao ARKYOS! #')
    print('#########################' "\n")
    print('principais comandos: [mover / olhar / mochila]')
    print('- Digite mover para se movimentar')
    print('- Digite seus comandos para executá-los')
    print('- Use o comando "inspecionar ou olhar" para examinar algo')
    print('- Boa sorte e não morra :p')
    if meu_jogador.nome != '':
        print('Voltar ao game? [s/n]')
        voltar_game = input('>>').lower()
        if voltar_game != 's':
            limpar_tela()
            ajuda_menu()
        print_local()
        main_game_loop()
    print("voltar ao MENU? [s/n]")
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
    'a1': False, 'a2': False, 'a3': False, 'a4': False,
    'b1': False, 'b2': False, 'b3': False, 'b4': False,
    'c1': False, 'c2': False, 'c3': False, 'c4': False,
    'd1': False, 'd2': False, 'd3': False, 'd4': False,
}

mapa = {
    'a1': {
        'NOME_LOCAL': 'Sala 1',
        'DESCRICAO': 'Local de início, você começa aqui!',
        'EXAMINAR': 'Você vê duas galinhas.',
        'SOLVED': False,
        'SUBIR': '',
        'DESCER': '',
        'AVANÇAR': 'a2',
        'RETORNAR': '',
        'MONSTRO': ''
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
        'NOME_LOCAL': "Sala2 Segundo andar",
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

#mapa mental dos andares:
#|a1|a2|
#|b1|b2|
#|c2|c1|
#Começamos em a1

##### Interações em jogo #####

def print_local():
    local_nome = mapa[meu_jogador.local]['NOME_LOCAL']
    local_desc = mapa[meu_jogador.local]['DESCRICAO']
    print('\n' + ('#' * (4 + len(local_nome))))
    print(f"# {local_nome.upper()} #")
    print(f"# {local_desc} #")
    print('#' * (4 + len(local_nome)))
    mostrar_status()
    if mapa[meu_jogador.local]['MONSTRO'] != '':
        print(f"há um {mapa[meu_jogador.local]['MONSTRO'].nome} na sala. O que deseja fazer?\n[lutar / fugir / falar]")
        escolha = input(">>").lower()
        if escolha not in ['lutar', 'fugir', 'falar']:
            print_local()
        acao_luta(escolha, mapa[meu_jogador.local]['MONSTRO'])
    main_game_loop()

def prompt():
    print("\n" + "=====================================")
    print("O que deseja fazer?")
    acao = input("->").lower()
    acoes_aceitas = ['examinar', 'mover', 'sair', 'ajuda', 'olhar', 'inspecionar', 'ir', 'teleportar', 'dormir', 'mochila', 'mapa']
    while acao not in acoes_aceitas:
        print("Ação inválida, tente novamente.\n")
        acao = input("-> ").lower()
    if acao == 'sair':
        sair()
    if acao in ['mover', 'ir', 'teleportar']:
        jogador_mover()
    elif acao == 'ajuda':
        ajuda_menu()
    elif acao in ['examinar', 'olhar', 'inspecionar']:
        jogador_examinar()
    elif acao == 'dormir':
        jogador_dormir()
    elif acao == 'mochila' and acao != 'sair':
        abrir_mochila()

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
        luta(monstro)
    elif escolha == 'fugir':
        fugir()
        print_local()
    elif escolha == 'falar':
        loading()
        print(f'O {monstro.nome} não te entende e te ataca')
        intervalo()
        meu_jogador.vida -= monstro_exemplo.atk
        luta(monstro)

def abrir_mochila():
    if meu_jogador.game_over:
        main_game_loop()
    if meu_jogador.mochila:
        for i in range(len(meu_jogador.mochila)):
            if meu_jogador.mochila[i].equipado == True:
                print(f'{i+1}. {meu_jogador.mochila[i].nome} ATK: {meu_jogador.mochila[i].atk} desc: {meu_jogador.mochila[i].desc} (EQUIPADO)')
                continue
            print(f'{i+1}. {meu_jogador.mochila[i].nome} ATK: {meu_jogador.mochila[i].atk} desc: {meu_jogador.mochila[i].desc}')
        print('--> Use números para selecionar os itens ou [fechar]')
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
            # jogador selecionou sem item equipado
            else:
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

def luta(monstro):
    print(f'\n{monstro.nome} #{monstro.nivel}')
    print(f'vida: {monstro.vida}/{monstro.vida_max} ATK: {monstro.atk}')
    print('-'*50)
    mostrar_status()
    print('atacar / magia / fugir')
    acao = input(">>").lower()
    if acao not in ['atacar', 'magia', 'fugir']:
        limpar_tela()
        print("comando invádido".upper())
        luta(monstro)
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
                print(f'{i+1}. {magia.nome} | DANO: {magia.dano} | custo de mana: {magia.mana_gasta} | desc: {magia.desc}')
                input(">>")
        else:
            print('Você ainda não sabe magias')
            loading()
            meu_jogador.vida -= monstro.atk
            print(f'o {monstro.nome} te ataca')
            intervalo()
    elif acao == 'fugir':
        fugir()
    
    if meu_jogador.vida > 0 and monstro.vida > 0:
        luta(monstro)
        
    if meu_jogador.vida <= 0:
        meu_jogador.local = 'a1'
        meu_jogador.vida = meu_jogador.vida_max
        limpar_tela()
        print('Você morreu e acorda na sala inicial')
    elif monstro.vida <= 0:
        limpar_tela()
        print(f'VOCÊ DERROTOU {monstro.nome}')
        drop(monstro)

def drop(monstro):
    print(f'o {monstro.nome} dropou {monstro.item.nome}')
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

def mostrar_status():
    print(f'{meu_jogador.nome} #{meu_jogador.nivel}')
    print(f'vida: {meu_jogador.vida}/{meu_jogador.vida_max} ATK: {meu_jogador.atk}')
    if meu_jogador.item_equipado:
        print(f'arma: {meu_jogador.item_equipado.nome} ATK: {meu_jogador.item_equipado.atk}')

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
    if meu_jogador.local == 'a1':
        pergunta = "Para onde deseja se mover? (avançar)\n"
    elif meu_jogador.local in ['b1', 'c1']:
        pergunta = "Para onde deseja se mover? (avançar ou subir)\n"
    elif meu_jogador.local in ['a2', 'b2', 'c2']:
        pergunta = "para onde deseja se mover? (descer ou retornar)\n"
    
    dest = input(pergunta).lower()
    direcoes_validas = ['subir', 'descer', 'avançar', 'retornar']
    if dest in direcoes_validas:
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
    if mapa[meu_jogador.local]['SOLVED']:
        print("Você já examinou aqui.")
    else:
        print(mapa[meu_jogador.local]['EXAMINAR'])
        mapa[meu_jogador.local]['SOLVED'] = True

##### Fluxo principal #####

def main_game_loop():
    while not meu_jogador.game_over:
        prompt()
        # Aqui tratar se os enigmas foram resolvidos, chefe derrotado, tudo explorado, etc.
    limpar_tela()
    print("\n\n**FIM DE JOGO**")
    sys.exit()
    exit()

def setup_jogo():
    os.system('clear' if os.name != 'nt' else 'cls')

    pergunta1 = "\n Qual seu nome?\n"
    for caractere in pergunta1:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(0.001)
    meu_jogador.nome = input("-> ")

    pergunta2 = "Qual sua classe?\n(Escolha: guerreiro, mago ou despojado)\n"
    for caractere in pergunta2:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(0.001)

    classes_validas = ['guerreiro', 'mago', 'despojado']
    jogador_classe = input("-> ").lower()
    while jogador_classe not in classes_validas:
        print("Classe inválida, tente novamente.")
        jogador_classe = input("-> ").lower()
    meu_jogador.classe = jogador_classe
    print(f"Classe selecionada: {meu_jogador.classe.capitalize()}\n")

    if meu_jogador.classe == 'guerreiro':
        meu_jogador.vida = 120
        meu_jogador.vida_max = meu_jogador.vida
        meu_jogador.mana = 20
        meu_jogador.mana_max = meu_jogador.mana
        meu_jogador.item_equipado = Arma('Espada longa', 4, 'A espada de todo guerreiro.', True)
        meu_jogador.add_item(meu_jogador.item_equipado)
        meu_jogador.atk_final = meu_jogador.atk + meu_jogador.item_equipado.atk     

    elif meu_jogador.classe == 'mago':
        meu_jogador.vida = 40
        meu_jogador.vida_max = meu_jogador.vida
        meu_jogador.mana = 120
        meu_jogador.mana_max = meu_jogador.mana
        meu_jogador.magias.append(magias('Bola de fogo', 20, 'A magia mais forte de um mago', 30))
    elif meu_jogador.classe == 'despojado':
        meu_jogador.vida = 60
        meu_jogador.vida_max = meu_jogador.vida
        meu_jogador.mana = 60
        meu_jogador.mana_max = meu_jogador.mana

    fala1 = f"Bem-vindo, {meu_jogador.nome} o {meu_jogador.classe.capitalize()}!\n"
    fala2 = "Espero que se divirta nessa incrível aventura!\n"
    fala3 = "Seu objetivo é descer a Torre de ARKYOS vivo, mas cuidado com os monstros que espreitam por aqui. Boa sorte!\n"

    for fala in [fala1, fala2, fala3]:
        for caractere in fala:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(0.001)
    time.sleep(2)

    os.system('clear' if os.name != 'nt' else 'cls')
    print ("=====================================")
    introducao1 = f'nome: {meu_jogador.nome} // classe: {meu_jogador.classe} // vida: {meu_jogador.vida} // mana: {meu_jogador.mana} \n'
    for introducao in introducao1:
        sys.stdout.write(introducao)
        sys.stdout.flush()
        time.sleep(0.001)
    introducao2 = 'Você acordou naquele quarto escuro, aparentemente sua luz acabou e você não sabe o por que. \n Você vivia pacificamente em seu quarto e nunca precisou sair pois um cara sempre trazia tudo que você precisa mas aparentemente essa pessoa sumiu.\n Agora é com você o encontrar.\n'
    for introducao in introducao2:
        sys.stdout.write(introducao)
        sys.stdout.flush()
        time.sleep(0.001)
    ajuda = 'principais comandos: [mover / olhar / mochila]\n'
    for ajuda in ajuda:
        sys.stdout.write(ajuda)
        sys.stdout.flush()
        time.sleep(0.001)

    start_game()
    print_local()

##### Executar #####
tela_titulo()