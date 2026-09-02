# ORGANIZADOR DE DOWNLOADS - Windows
import os

class Organizador:
    # ORGANIZAR POR: NOME, TAMANHO, DATA DE CRIAÇÃO, DATA DE MODIFICAÇÃO, TIPO DE ARQUIVO

    # - Para organizar o tipo de arquivo, basta analisar por ordem alfabética apartir do . (extensão do arquivo)
    def __init__(self, organizar_por):
         self.organizar_por = organizar_por

    def organizar(self):
        # Lógica para organizar os arquivos na pasta de downloads
        usuario = Organizador.identificar_usuario(self)
        arquivos = os.scandir(path = f'C:\\Users\\{usuario}\\Downloads')
        for arquivo in arquivos:
            print(arquivo.name)
    
    def identificar_usuario(self):
        return os.environ.get('USERNAME')


print(f'\n{60 * "-"}\n|{5 * " "}Bem-vindo ao Organizador de Downloads! - Windows{5 * " "}|\n{60 * "-"}')
print(f'{10 * " "}C: > Users > {Organizador.identificar_usuario(None)} > Downloads{10 *""}\n{60 * "-"}')

Organizador.organizar(None)
    