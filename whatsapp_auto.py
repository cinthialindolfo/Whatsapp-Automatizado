# voce tem que esta com o whatsapp logado na web para poder enviar a mensagem

# whatsapp_auto.py
import pywhatkit as whatsapp
import time

# Lista de números (substitua com seus contatos no formato +55DDDNNNNNNNNN)
lista_contatos = [

    # você vai colocar os números dos contatos que deseja enviar a mensagem, exemplos abaixo e acima

    # "+551234567890", "+551234567890", "+551234567890"
    
]

# Mensagem que será enviada
mensagem = """bla, bla, bla"""

# Configurações de segurança
intervalo_entre_envios = 60 # segundos (NÃO reduza esse valor!)

# Loop de envio
for numero in lista_contatos:
    try:
        print(f"Enviando para {numero}...")
        
        whatsapp.sendwhatmsg_instantly(
            phone_no=numero,
            message=mensagem,
            wait_time=30,  # Tempo para carregar a página
            tab_close=True
        )
        
        print(f"✓ Enviado para {numero}")
        time.sleep(intervalo_entre_envios)  # Pausa OBRIGATÓRIA
        
    except Exception as erro:
        print(f"Erro no número {numero}: {str(erro)}")
        time.sleep(300)  # Pausa maior se houver erro

print("Processo concluído!")
