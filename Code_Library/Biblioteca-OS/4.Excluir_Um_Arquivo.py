# EXCLUIR UM ARQUIVO

import os

class ExcluirArquivo:
    def __init__(self, nome):
        self.nome = nome
    
    def excluir(self):
        os.remove(self.nome)
        print("Arquivo", self.nome, "excluído com sucesso.")


arquivo_a_excluir = "arquivo_de_teste.txt"
excluidor = ExcluirArquivo(arquivo_a_excluir)
excluidor.excluir()
