import urllib3
import ssl

# Desabilitar a verificação de certificados SSL (NÃO RECOMENDADO PARA AMBIENTES DE PRODUÇÃO)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager(cert_reqs=ssl.CERT_NONE)

try:
    response = http.request("GET", "https://www.pudim.com.br/")
    
    if response.status == 200:
        print('Tudo ok.')
        # Aqui você pode fazer o que quiser com a resposta do site
        # Por exemplo, imprimir o conteúdo da página:
        # print(response.data.decode('utf-8'))
    else:
        print(f'O site retornou o código de erro {response.status}.')

# Retorna se há erro de conexão, proxy, firewall, etc.
except urllib3.exceptions.MaxRetryError as erro:
    print('O site pudim não está acessível no momento.')
    print(f'Deu erro {erro.__class__}.')
    print(f'O motivo foi: {erro.__cause__}')

else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(response.data.decode('utf-8')) # Imprime o conteúdo da página
    # response.data.decode('utf-8'): O método data do objeto response retorna o conteúdo da página em bytes. 
    # Para imprimir o conteúdo em texto, é necessário decodificá-lo usando decode('utf-8').
    