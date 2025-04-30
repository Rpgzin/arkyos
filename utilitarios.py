import os, sys, time
def limpar_tela():
    os.system('clear' if os.name != 'nt' else 'cls')

def loading():
    print('')
    for i in range(0, 5):
        sys.stdout.write('. ')
        sys.stdout.flush()
        time.sleep(0.1)
    print('')
    
def intervalo():
    time.sleep(0.3)