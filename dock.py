import os
from colorama import init, Back, Fore, Style

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

def barra_de_opcoes(self): #Navegar pela seta <- / -> e selecionar com ENTE - Fazer uma list
    dock = [{1:'[1] NOME', 2:'[2] TAMANHO', 3: '[3] DATA DE CRIAÇÃO', 4:'[4] DATA DE MODIFICAÇÃO', 5: '[5] TIPO DE ARQUIVO'}]

    while True:
        command = int(input('<- or ->')) # Encontrar um forma de ler outras teclas como entrada

    Interface.part_superior(self, None)
    print(f'│{4 * " "}{Back.BLUE}[1] NOME {Style.RESET_ALL} │ [2] TAMANHO │ [3] DATA DE CRIAÇÃO │ [4] DATA DE MODIFICAÇÃO │ [5] TIPO DE ARQUIVO{4 * " "}│')
    Interface.part_inferior(self, None)

barra_de_opcoes(None)