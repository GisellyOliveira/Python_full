import sys

class InformacoesAmbientePython:
    def __init__(self) -> None:
        pass

    def obter_info_ambiente(self):
        print(f"Versão do Python: {sys.version}")
        print(f"Plataforma: {sys.platform}")
        print(f"Prefixo do Executável: {sys.exec_prefix}")
        print(f"Caminho do Módulo: {sys.path}")

info_ambiente = InformacoesAmbientePython()
info_ambiente.obter_info_ambiente()
