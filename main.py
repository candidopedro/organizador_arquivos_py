# ORGANIZADOR DE DOWNLOADS = Windows
# Fazer por último, o ajuste de tamanho automatico da interface, de acordo com o tamanho do nome do usuário & Nome do maior arquivo da pasta de downloads

#Limitar quantidade de caracteres no nome do arquivo, mantendo o nome da extensão do arquivo
import os
from pathlib import Path

RESET = '\033[0m'
AZUL = '\033[34m'
VERDE = "\033[92m"

TERMINAL_SIZE_COLUMNS = (os.get_terminal_size().columns)-2

print(TERMINAL_SIZE_COLUMNS)
class Interface:
    # Funções para criar a interface do programa
    def part_superior(self,cor):
        if cor:
            return print(f'{cor}╭' + '─' * TERMINAL_SIZE_COLUMNS + f'╮{RESET}')
        elif cor == None:
            return print(f'╭' + '─' * TERMINAL_SIZE_COLUMNS + f'╮')

    def part_central(self, cor):
        if cor:
            return print(f'{cor}├' + '─' * TERMINAL_SIZE_COLUMNS + f'┤{RESET}')
        elif cor == None:
            return print(f'├' + '─' * TERMINAL_SIZE_COLUMNS + f'┤')

    def part_inferior(self,cor):
        if cor:
            return print(f'{cor}╰' + '─' * TERMINAL_SIZE_COLUMNS + f'╯{RESET}')
        elif cor == None:
            return print(f'╰' + '─' * TERMINAL_SIZE_COLUMNS + f'╯')

    def barra_de_opcoes(self): #Navegar pela seta <- / -> e selecionar com ENTER
        print(f'│{4 * " "}[1] NOME │ [2] TAMANHO │ [3] DATA DE CRIAÇÃO │ [4] DATA DE MODIFICAÇÃO │ [5] TIPO DE ARQUIVO{2 * " "}│')

    def barra_de_organizacao(self):
        Interface.part_superior(None, cor = None)
        print(f'│{AZUL} Nome {RESET}  {(TERMINAL_SIZE_COLUMNS-85) * " "}│{AZUL}  Tamanho  {RESET}│{AZUL}   Data de Criação  {RESET}│{AZUL}  Data de Modificação  {RESET}│{AZUL}  Tipo de Arquivo{2 * " "}{RESET}│')
        Interface.part_central(None, cor = None)

class Organizador:
    # ORGANIZAR POR: NOME, TAMANHO, DATA DE CRIAÇÃO, DATA DE MODIFICAÇÃO, TIPO DE ARQUIVO
    # Para organizar o tipo de arquivo, basta analisar por ordem alfabética apartir do . (extensão do arquivo)
    def __init__(self, organizar_por):
         self.organizar_por = organizar_por

    def organizar(self):# Lógica para organizar os arquivos na pasta de downloads
        usuario = Organizador.identificar_usuario(self)
        arquivos = os.scandir(path = f'C:\\Users\\{usuario}\\Downloads')

        Interface.barra_de_organizacao(None)

        for arquivo in arquivos:
            if len(arquivo.name) > 9 and Path(arquivo.name).suffix != ' ':
                print(f'│ 📄 {(arquivo.name[:9]) + "[..]" + Path(arquivo.name).suffix + "│"}')

        Interface.part_inferior(None, cor = None)

        #BARRA DE OPÇÕES PARA ORGANIZAR OS ARQUIVOS - MAIN
        Interface.part_superior(None, cor = None)
        Interface.barra_de_opcoes(None)
        Interface.part_inferior(None, cor = None)
        organizar_por = input('Selecione o tipo de organização: ')

    def identificar_usuario(self):
        return os.environ.get('USERNAME')

Interface.part_superior(None,cor=AZUL)
print(f'{AZUL}│{(TERMINAL_SIZE_COLUMNS-82) * " "}{VERDE} Bem-vindo ao Organizador de Downloads! - Windows{(TERMINAL_SIZE_COLUMNS-80)* " "}{AZUL}│{RESET}')

Interface.part_central(None,cor=AZUL)

print(f'{AZUL}│{(TERMINAL_SIZE_COLUMNS-85)* " "}{RESET}📂 C: > Users > {Organizador.identificar_usuario(None)} > Downloads{(TERMINAL_SIZE_COLUMNS-85)* " "}{AZUL}│{RESET}')
Interface.part_inferior(None,cor=AZUL)

Organizador.organizar(None)