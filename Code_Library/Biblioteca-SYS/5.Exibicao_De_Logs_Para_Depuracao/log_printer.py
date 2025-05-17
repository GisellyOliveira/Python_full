import logging
import sys

# Configuração básica do logging
logging.basicConfig(
    stream=sys.stdout,  # Mostrar as mensagens no terminal
    level=logging.DEBUG,  # Mostrar tudo a partir do nível DEBUG
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Criando um "logger"
logger = logging.getLogger("MeuPrograma")

# Testando vários níveis de mensagens
logger.debug("Esta é uma mensagem de DEBUG (detalhes para programadores).")
logger.info("Esta é uma mensagem de INFO (informações gerais).")
logger.warning("Esta é uma mensagem de WARNING (algo está estranho).")
logger.error("Esta é uma mensagem de ERROR (algo deu errado).")
logger.critical("Esta é uma mensagem CRÍTICA (o programa pode parar).")
