import sys

class ManipulacaoEntradaSaida:
    def __init__(self) -> None:
        pass

    def ler_linhas_entrada_padrao(self):
        print("--- Iniciando leitura stdin ---") 
        for linha in sys.stdin:
            sys.stdout.write(f"Entrada padrão: {linha}")
        print("--- Fim da leitura stdin ---")

    def redirecionar_saida_padrao(self):
        original_stdout = sys.stdout
        print("--- Redirecionando stdout ---")
        try:
            with open('saida.txt', 'w') as f:   # 'with' garante que o arquivo será fechado mesmo se ocorrer erro
                sys.stdout = f # Redireciona stdout para o arquivo
                print("Este é um teste de saída padrão redirecionada.")
        finally:
            sys.stdout = original_stdout
            print("--- stdout restaurado ---") # Vai para a tela novamente
        

if __name__ == '__main__':
    manipulador_io = ManipulacaoEntradaSaida()

    print(">>> Teste 1: Leitura da Entrada Padrão (Digite linhas e Ctrl+D/Ctrl+Z+Enter) <<<")
    manipulador_io.ler_linhas_entrada_padrao()

    print("\n>>> Teste 2: Redirecionamento da Saída Padrão (Verifique saida.txt) <<<")
    manipulador_io.redirecionar_saida_padrao()

    print("\n>>> Script concluído. <<<")
