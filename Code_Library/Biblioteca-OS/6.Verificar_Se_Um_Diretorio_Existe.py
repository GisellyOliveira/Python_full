# VERIFICAR SE UM DIRETÓRIO EXISTE

import os

class VerificarDiretorio:
    def __init__(self, nome):
        self.nome = nome
    
    def verificar(self):
        if os.path.exists(self.nome):
            print("O diretório", self.nome, "existe.")
        else:
            print("O diretório", self.nome, "não existe.")


diretorio_a_verificar = "diretorio_renomeado"
verificador = VerificarDiretorio(diretorio_a_verificar)
verificador.verificar( )
