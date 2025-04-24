# EXCLUI QUALQUER DIRETÓRIO COM QUALQUER CONTEÚDO
# USE COM MODERAÇÃO

import os
import shutil

class Excluir_Qualquer_Diretorio:
    def __init__(self, nome):
        self.nome = nome

    def excluir(self):
        shutil.rmtree(self.nome)
        print("Diretório", self.nome, "excluído com sucesso.")
    

diretorio_a_excluir = "diretorio_renomeado"
excluidor = Excluir_Qualquer_Diretorio(diretorio_a_excluir)
excluidor.excluir()
