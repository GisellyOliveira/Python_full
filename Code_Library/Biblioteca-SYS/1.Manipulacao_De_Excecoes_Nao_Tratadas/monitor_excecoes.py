import sys
import traceback # Importar para formatar melhor o traceback

# --- Importar módulo que vai causar o erro ---
# Fazemos isso aqui, mas só chamaremos a função depois de ativar o hook
import modulo_com_erro


class ExcecaoNaoTratada:
    def __init__(self):
        pass

    def excecao_nao_tratada(self, exc_type, exc_value, exc_traceback):
        print("-" * 50)
        print("### MONITOR GLOBAL CAPTUROU UMA EXCEÇÃO NÃO TRATADA ###")
        print(f"Tipo: {exc_type.__name}")
        print(f"Valor: {exc_value}")
        print("Rastreamento (Traceback):")
        # Usar o módulo traceback para formatar a saída fica mais legível
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        print("-" * 50)

    def ativar_monitoramento_excecoes(self):
        print("Ativando o monitor global de exceções...")
        sys.excepthook = self.excecao_nao_tratada
        print("Monitor ativado.")


# --- Bloco principal ---
if __name__ == "__main__": # Boa prática para código que pode ser importado
    excecao_monitor = ExcecaoNaoTratada()
    excecao_monitor.ativar_monitoramento_excecoes()

    print("\nAgora vamos chamar a função do outro módulo...")

    try:
        # Chamar a função do outro módulo que vai causar o erro
        modulo_com_erro.funcao_que_falha()
    except Exception as e:
        # Este bloco except SÓ será executado se a funcao_que_falha
        # TIVESSE um try... except interno e relançasse a exceção,
        # ou se o erro ocorresse DENTRO deste try, ANTES da chamada
        # Se o erro dentro de funcao_que_falha não for tratado LÁ DENTRO,
        # o sys.excepthook será chamado diretamente.
        print(f"Exceção tratada aqui em monitor_excecoes.py: {e}")
        # Neste cenário específico (erro não tratado em funcao_que_falha),
        # esta linha NÃO deve ser impressa.
    

    print("\nEsta linha em monitor_excecoes.py será executada APENAS se a exceção for tratada")
    # Se o excepthook for chamado, o programa geralmente termina ali.
