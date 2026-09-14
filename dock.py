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

def barra_de_opcoes(self): #Navegar pela seta <- / -> e selecionar com ENTE - Fazer uma list

    dock = {1:'[1] NOME', 2:'[2] TAMANHO', 3: '[3] DATA DE CRIAÇÃO', 4:'[4] DATA DE MODIFICAÇÃO', 5: '[5] TIPO DE ARQUIVO'}
    # {Back.BLUE}[1] NOME {Style.RESET_ALL} - adionar ao conjunto de caracteres no inicio e no fim quando selecionado - sempre atualizar a dock e a organização conforme for selecionando os tipos diferentes de organização
    # print(f'│{4 * " "}[1] NOME │ [2] TAMANHO │ [3] DATA DE CRIAÇÃO │ [4] DATA DE MODIFICAÇÃO │ [5] TIPO DE ARQUIVO{4 * " "}│')
    # command = int(input('<- or ->')) # Encontrar um forma de ler outras teclas como entrada
    
    item_dock = 1
    while True:
        print('Pressione <- ou ->')
        tecla = keyboard.read_key()
        print(tecla)
        if tecla == 'right' and item_dock < 6:
            item_dock += 1
        elif tecla == 'left' and item_dock > 1:
            item_dock -= 1

        print(item_dock)
        for key, value in dock.items():
            if key == item_dock:
                dock.update({item_dock: f"{Back.BLUE}{value}{Style.RESET_ALL}"})

        Interface.part_superior(self, None)
        for chave, valor in dock.items():
            if chave == 1:
                print(f'│    {valor} │', end= " ")
            elif chave == 5:
                print(f'{valor}    │')
            else:
                print(f'{valor} │', end= " ")

        Interface.part_inferior(self, None)
        break
        
barra_de_opcoes(None)