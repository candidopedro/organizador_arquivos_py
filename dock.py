import os
from colorama import init, Back, Fore, Style
import keyboard

init(autoreset=True)

RESET = '\033[0m'
AZUL = '\033[34m'
VERDE = "\033[92m"

os.get_terminal_size = lambda: os.terminal_size((100, 20))  # Define o tamanho do terminal como 100x20
tamanho_terminal = lambda: os.get_terminal_size().columns  # Função para obter 

class Interface:
    # Funções para criar a interface do programa
    def part_superior(self,cor):
        if cor:
            return print(f'{cor}╭' + '─' * (tamanho_terminal()) + f'╮{RESET}')
        elif cor == None:
            return print(f'╭' + '─' * tamanho_terminal() + f'╮')

    def part_central(self, cor):
        if cor:
            return print(f'{cor}├' + '─' * tamanho_terminal() + f'┤{RESET}')
        elif cor == None:
            return print(f'├' + '─' * tamanho_terminal() + f'┤')

    def part_inferior(self,cor):
        if cor:
            return print(f'{cor}╰' + '─' * tamanho_terminal() + f'╯{RESET}')
        elif cor == None:
            return print(f'╰' + '─' * tamanho_terminal() + f'╯')

    def refesh(self):
        os.system('cls' if os.name == 'nt' else 'clear')

def barra_de_opcoes(self):
    # {Back.BLUE}[1] NOME {Style.RESET_ALL} - sempre atualizar a dock e a organização conforme for selecionando os tipos diferentes de organizaçã

    tecla = ''
    item_dock = 1
    while tecla != 'esc':
        
        dock = {1:f'[1] NOME{Style.RESET_ALL}', 2:f'[2] TAMANHO{Style.RESET_ALL}', 3: f'[3] DATA DE CRIAÇÃO{Style.RESET_ALL}', 4:f'[4] DATA DE MODIFICAÇÃO{Style.RESET_ALL}', 5: f'[5] TIPO DE ARQUIVO{Style.RESET_ALL}'}

        for chave, valor in dock.items():
            if chave == item_dock:
                dock.update({item_dock: f"{Back.BLUE}{valor}{Style.RESET_ALL}"})

        Interface.part_superior(self, None)
        for chave, valor in dock.items():
            if chave == 1:
                print(f'│    {valor} │', end= " ")
            elif chave == 5:
                print(f'{valor}    │')
            else:
                print(f'{valor} │', end= " ")
        Interface.part_inferior(self, None)

        print('Pressione <- ou ->')
        tecla = keyboard.read_key()
        
        if tecla == 'right' and item_dock < 5:
            item_dock += 1
        elif tecla == 'left' and item_dock > 1:
            item_dock -= 1

        while keyboard.is_pressed(tecla): # Para aguardar a tecla ser pressionada 
            pass
            
barra_de_opcoes(None)