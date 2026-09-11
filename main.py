# ORGANIZADOR DE DOWNLOADS = Windows
# Fazer por último, o ajuste de tamanho automatico da interface, de acordo com o tamanho do nome do usuário & Nome do maior arquivo da pasta de downloads

# - Limitar quantidade de caracteres no nome do arquivo, mantendo o nome da extensão do arquivo

# Usar o Try & Except para especificar os dados não encontrados nos arquivos

import os 
import datetime
import getpass
from pathlib import Path

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

    def barra_de_opcoes(self): #Navegar pela seta <- / -> e selecionar com ENTER
        print(f'│{4 * " "}[1] NOME │ [2] TAMANHO │ [3] DATA DE CRIAÇÃO │ [4] DATA DE MODIFICAÇÃO │ [5] TIPO DE ARQUIVO{4 * " "}│')

    def barra_de_organizacao(self):
        Interface.part_superior(None, cor = None)
        print(f'│{AZUL} Nome {RESET}  {(tamanho_terminal()-85) * " "}│{AZUL}  Tamanho  {RESET}│{AZUL}   Data de Criação  {RESET}│{AZUL}  Data de Modificação  {RESET}│{AZUL}  Tipo de Arquivo{2 * " "}{RESET}│')
        Interface.part_central(None, cor = None)

    def refesh(self):
        os.system('cls' if os.name == 'nt' else 'clear')

class Organizador:
    def __init__(self, organizar_por):
        self.organizar_por = organizar_por

    # Nome
    def nome_arquivo(self, arquivo):
        if len(Path(arquivo.name).stem) > 9 and len(Path(arquivo.name).suffix) > 4:
            return (f'│ 📄 {(Path(arquivo.name).stem)[:(13-len(Path(arquivo.name).suffix))] + "[..]" + Path(arquivo.name).suffix} {1 * " "}│')
        elif len(arquivo.name) == 9 and len(Path(arquivo.name).suffix) == 4:
            return (f'│ 📄 {Path(arquivo.name).stem[:9]}[..]{Path(arquivo.name).suffix} {1 * " "}│') # diminuir pelo tamanho do suffix maior (valor padrão - valor do suffix maior) - DIFERENÇA
        elif len(arquivo.name) > 9 and len(Path(arquivo.name).suffix) == 4:
            return (f'│ 📄 {(arquivo.name[:9]) + "[..]" + Path(arquivo.name).suffix} {1 * " "}│')
        else:
           return (f'│ 📄 {((arquivo.name) + 25 * " ")[:19]}│')

    # Tamanho   
    def tamanho_arquivo(self, arquivo): # TAMANHO - MB & GB (até o momento..)
        if len(str(os.path.getsize(arquivo))) >= 10:
            return f'{2 * " "}{((os.path.getsize(arquivo))/ 1024 ** 3):.2f} GB{2 * " "}│'
        elif len(str(os.path.getsize(arquivo))) == 8:
            return f'{4 * " "}{((os.path.getsize(arquivo))/ 1024 ** 2):.0f} MB{2 * " "}│'
        elif len(str(os.path.getsize(arquivo))) == 7:
            return f'{2 * " "}{((os.path.getsize(arquivo))/ 1024 ** 2):.2f} MB{2 * " "}│'
        else:
            return f'{3 * " "}{((os.path.getsize(arquivo))/ 1024 ** 2):.1f} MB{2 * " "}│'

    # Data de Criação
    def data_criacao_arquivo(self, arquivo):
        timestamp_criacao = os.path.getctime(arquivo)
        data_criacao = datetime.datetime.fromtimestamp(timestamp_criacao)
        data_formatada = data_criacao.strftime("%d/%m/%Y %H:%M")
        return f'{2 * " "}{((data_formatada))}{2 * " "}│'

    # Data de Modificação
    def data_modificacao_arquivo(self,arquivo):
        timestamp_modificacao = os.path.getmtime(arquivo)
        data_modificacao = datetime.datetime.fromtimestamp(timestamp_modificacao)
        data_formatada = data_modificacao.strftime("%d/%m/%Y %H:%M")
        return f'{3 * " "}{((data_formatada))}{3 * " "}│'

    # Tipo de Arquivo
    def tipo_de_arquivo(self, arquivo):
        return f'{7 * " "}{((Path(arquivo).suffix) + (25 * " ")[:12-(len(Path(arquivo).suffix))])}│'
        
    def organizar(self):# Lógica para organizar os arquivos na pasta de downloads
        usuario = Organizador.identificar_usuario(self)
        arquivos = os.scandir(path = f'C:\\Users\\{usuario}\\Downloads')

        if usuario == None: # Identificador nome de usuário Linux
            usuario = getpass.getuser()
            arquivos = os.scandir(path = f'\\Home\\{usuario}\\Downloads')

        Interface.barra_de_organizacao(None)

        for arquivo in arquivos: # Definindo o tamanho do nome do arquivo, para que não ultrapasse o tamanho da interface
            print(
                f"{Organizador.nome_arquivo(self, arquivo)}{Organizador.tamanho_arquivo(self, arquivo)}{Organizador.data_criacao_arquivo(self, arquivo)} {Organizador.data_modificacao_arquivo(self, arquivo)}{Organizador.tipo_de_arquivo(self, arquivo)}"
                )
            
        Interface.part_inferior(None, cor = None)

        #BARRA DE OPÇÕES PARA ORGANIZAR OS ARQUIVOS - MAIN
        Interface.part_superior(None, cor = None)
        Interface.barra_de_opcoes(None)
        Interface.part_inferior(None, cor = None)
        organizar_por = input('Selecione o tipo de organização: ')

    def identificar_usuario(self):
        return os.environ.get('USERNAME')

def main():
    Interface.refesh(None)
    Interface.part_superior(None,cor=AZUL)
    print(f'{AZUL}│{(tamanho_terminal()-74) * " "}{VERDE} Bem-vindo ao Organizador de Downloads! - Windows{AZUL}{(tamanho_terminal()-75) * " "}│{RESET}')

    Interface.part_central(None,cor=AZUL)

    print(f'{AZUL}│{(tamanho_terminal()-70)* " "}{RESET}📂 C: > Users > {Organizador.identificar_usuario(None)} > Downloads{(tamanho_terminal()-72)* " "}{AZUL}│{RESET}')
    Interface.part_inferior(None,cor=AZUL)
    Organizador.organizar(None)

if __name__ == '__main__':
    main()