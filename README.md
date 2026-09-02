# 📁 Organizador Automático de Arquivos

Script em Python que varre uma pasta (ex: `Downloads`) e organiza automaticamente os arquivos em subpastas de acordo com o tipo de arquivo (imagens, PDFs, planilhas, documentos, vídeos, etc).

## ✨ Funcionalidades

- Varre uma pasta indicada pelo usuário
- Identifica o tipo de cada arquivo pela extensão
- Cria subpastas automaticamente (caso não existam)
- Move os arquivos para a subpasta correspondente
- Arquivos com extensões não mapeadas vão para uma pasta "Outros"

## 🛠️ Tecnologias

- **Python 3**
- **os** — biblioteca padrão utilizada para:
  - Listar os arquivos da pasta (`os.listdir` / `os.scandir`)
  - Verificar se é arquivo ou pasta (`os.path.isfile`)
  - Criar subpastas (`os.makedirs`)
  - Mover arquivos (`os.rename`)
  - Extrair a extensão do arquivo (`os.path.splitext`)

> Não são necessárias bibliotecas externas — o projeto usa apenas recursos nativos do Python.

## 📂 Categorias de Organização

| Categoria | Extensões |
|---|---|
| Imagens | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg` |
| PDFs | `.pdf` |
| Planilhas | `.xlsx`, `.xls`, `.csv` |
| Documentos | `.doc`, `.docx`, `.txt`, `.odt` |
| Vídeos | `.mp4`, `.avi`, `.mkv`, `.mov` |
| Áudios | `.mp3`, `.wav`, `.flac` |
| Compactados | `.zip`, `.rar`, `.7z` |
| Outros | Extensões não mapeadas |

## 🚀 Como usar

```bash
python organizador.py
```

Por padrão, o script organiza a pasta configurada no código (ex: `Downloads`). É possível alterar o caminho da pasta-alvo editando a variável correspondente no script.

## ⚙️ Configuração

As categorias e extensões podem ser ajustadas diretamente no dicionário de configuração dentro do script, permitindo personalizar a organização conforme a necessidade.

## ⚠️ Observações

- Recomenda-se testar o script em uma pasta de exemplo antes de rodar em pastas importantes.
- Arquivos com nomes duplicados na pasta de destino podem ser sobrescritos, dependendo da lógica implementada — verifique o comportamento no código antes de usar em produção.

## 📌 Status do Projeto

🚧 Em desenvolvimento

## 📄 Licença

Este projeto está sob a licença MIT.
