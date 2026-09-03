from pathlib import Path

from main import Organizador


def test_classificar_arquivo():
    assert Organizador.classificar_arquivo("arquivo.jpg") == "Imagens"
    assert Organizador.classificar_arquivo("arquivo.pdf") == "PDFs"
    assert Organizador.classificar_arquivo("arquivo.desconhecido") == "Outros"


def test_organizar_move_arquivos_para_pastas(tmp_path):
    pasta_origem = tmp_path / "Downloads"
    pasta_origem.mkdir()

    (pasta_origem / "foto.jpg").write_text("foto")
    (pasta_origem / "relatorio.txt").write_text("texto")
    (pasta_origem / "arquivo.sem_extensao").write_text("outro")

    organizador = Organizador(str(pasta_origem))
    organizador.organizar()

    assert (pasta_origem / "Imagens" / "foto.jpg").exists()
    assert (pasta_origem / "Documentos" / "relatorio.txt").exists()
    assert (pasta_origem / "Outros" / "arquivo.sem_extensao").exists()
