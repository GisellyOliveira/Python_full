import unittest
from unittest.mock import patch, mock_open, call
import io # Para simular stdin/stdout
import sys

# Importa a classe do arquivo original
from io_script import ManipulacaoEntradaSaida


class TestManipulacaoEntradaSaida(unittest.TestCase):
    """
    Conjunto de testes para a classe ManipulacaoEntradaSaida,
    verificando a interação com sys.stdin, sys.stdout e arquivos.
    """

    def setUp(self) -> None:
        """
        Método executado antes de cada teste.
        Cria uma nova instância da classe sob teste para garantir isolamento.
        """
        self.manipulador = ManipulacaoEntradaSaida()
    
    def test_ler_linhas_entrada_padrao(self) -> None:
        """
        Verifica se o método 'ler_linhas_entrada_padrao' lê corretamente
        linhas simuladas de sys.stdin e as escreve formatadas em sys.stdout.
        """
        # Preparação: Simular dados de entrada e um buffer para a saída
        input_data = "Primeira linha\nSegunda linha\n"
        fake_stdin = io.StringIO(input_data)

        # Simular/Capturar a saída padrão (o que iria para a tela)
        fake_stdout = io.StringIO()

        # Define o que esperávamos que fosse impresso
        output_esperado = (
            "--- Iniciando leitura stdin ---\n"
            "Entrada padrão: Primeira linha\n"
            "Entrada padrão: Segunda linha\n"
            "--- Fim da leitura stdin ---\n"
        )

        # Execução: Chamar o método sob teste, substituindo temporariamente
        # stdin e stdout pelos nossos objetos simulados usando 'patch'.
        # 'patch' atua como um gerenciador de contexto (with).
        with patch('sys.stdin', fake_stdin), patch('sys.stdout', fake_stdout):
            self.manipulador.ler_linhas_entrada_padrao()
        
        # Verificação: Comparar o que foi escrito no stdout simulado
        # com o resultado que esperávamos.
        output_resultado = fake_stdout.getvalue()
        self.assertEqual(output_resultado, output_esperado, 
                         "A saída formatada em stdout não corresponde ao esperado.")
    
    def test_redirecionar_saida_padrao(self) -> None:
        """
        Verifica se 'redirecionar_saida_padrao' tenta abrir o arquivo
        correto ('saida.txt' em modo 'w') e escrever a mensagem esperada nele,
        usando mocks para evitar a criação real de arquivos.
        """
        # Preparação: Definir o texto esperado e criar um mock para 'open'
        texto_esperado_no_arquivo = "Este é um teste de saída padrão redirecionada."

        # Usar mock_open para simular a abertura de arquivo, sem criar um arquivo real.
        # mock_open simula a função 'open' e o arquivo retornado por ela
        mock_file = mock_open()

        # Texto esperado nas chamadas 'write' (print chama write duas vezes)
        expected_calls = [
            call(texto_esperado_no_arquivo), # Primeira chamada com o texto
            call('\n')                       # Segunda chamada com a nova linha
        ]


        # Usar 'patch' para substituir a função 'open' e 'sys.stdout'
        # Guardamos o stdout original para verificação e restauração
        original_stdout = sys.stdout
        with patch('builtins.open', mock_file), patch('sys.stdout', original_stdout):
            self.manipulador.redirecionar_saida_padrao()
        
        # Verifica se 'open' foi aberto corretamente
        mock_file.assert_called_once_with('saida.txt', 'w')

        # Import 'call' no início do arquivo, junto com os outros imports de mock:
        # from unittest.mock import patch, mock_open, call
        expected_calls = [call(texto_esperado_no_arquivo), call('\n')]
        self.assertEqual(mock_file().write.mock_calls, expected_calls, 
                         "As chamadas ao método 'write'não foram as esperadas.")


if __name__ == '__main__':
    unittest.main(verbosity=2)
