import unittest
import sys
from Configurador import ConfiguracaoInterpretador

class TestConfiguracaoInterpretador(unittest.TestCase):

    def setUp(self) -> None:
        """Executado antes de cada teste."""
        # Guarda o valor original do sys.maxsize
        self.original_maxsize = sys.maxsize
        # Cria uma instância da classe para usar nos testes
        self.config_interpretador = ConfiguracaoInterpretador()
        print(f"\n[setUp] Valor original sys.maxsize: {self.original_maxsize}")
    
    def tearDown(self) -> None:
        """Executado depois de cada teste, mesmo se falhar."""
        # Restaura o valor original de sys.maxsize
        sys.maxsize = self.original_maxsize
        print(f"[tearDown] Restaurado sys.maxsize para: {sys.maxsize}")
    
    def test_alterar_maxsize(self):
        """Testa se o método altera o sys.maxsize corretamente"""
        novo_valor = 12345
        print(f"[test_alterar_maxsize] Tentando alterar para: {novo_valor}")

    
        # Chama o método que queremos testar
        self.config_interpretador.alterar_variavel_interpretador("maxsize", novo_valor)

        # Verifica se o valor foi realmente alterado
        valor_atual = sys.maxsize
        print(f"[test_alterar_maxsize] Valor atual sys.maxsize: {valor_atual}")
        self.assertEqual(valor_atual, novo_valor, "sys.maxsize não foi alterado para o valor esperado.")

    
    def test_alterar_outra_variavel_existente(self):
        """Testa se pode alterar outra variável (ex: version - não recomendado!)"""
        # ATENÇÃO: Alterar sys.version é apenas para teste, pode quebrar coisas!
        versao_original = sys.version
        self.addCleanup(setattr, sys, 'version', versao_original) # Outra forma de garantir a restauração

        novo_valor = "Versão Fictícia 1.0"
        print(f"[test_alterar_outra] Tentando alterar sys.version para: {novo_valor}")

        # Chama o método para alterar sys.version
        self.config_interpretador.alterar_variavel_interpretador("version", novo_valor)

        valor_atual = sys.version
        print(f"[test_alterar_outra] Valor atual sys.version: {valor_atual}")
        self.assertEqual(valor_atual, novo_valor, "sys.version não foi alterado corretamente.")

        # Nota: A restauração ocorreráautomaticamente após esse método
        # devido ao addCleanup ou ao tearDown.


if __name__ == '__main__':
    unittest.main(verbosity=2)
