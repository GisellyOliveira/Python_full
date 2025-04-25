import sys

class ConfiguracaoInterpretador:
    def __init__(self) -> None:
        pass

    def alterar_variavel_interpretador(self, variavel, valor):
        setattr(sys, variavel, valor)

if __name__ == '__main__':  
    config_interpretador = ConfiguracaoInterpretador()
    config_interpretador.alterar_variavel_interpretador("maxsize", 99999)
    print(f"Tamanho máximo de um objeto: {sys.maxsize}")
