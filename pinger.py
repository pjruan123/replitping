import time
import requests
import os

# --- CONFIGURAÇÃO ---
# O URL do seu Replit será passado como uma Variável de Ambiente
REPLIT_URL = os.environ.get("https://replit.com/@pabloabreujuan2/discordbotajdzip#discordbotajd/main.py") 
PING_INTERVAL_SECONDS = 300  # 5 minutos

def ping_replit():
    if not REPLIT_URL:
        print("ERRO: Variável REPLIT_URL não configurada.")
        return

    try:
        # Tenta acessar o URL do Replit (o endpoint "/")
        response = requests.get(REPLIT_URL) 
        
        # O código 200 significa sucesso (o servidor Flask respondeu)
        if response.status_code == 200:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Ping bem-sucedido. Status: {response.status_code}")
        else:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Erro no Ping. Status inesperado: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Erro Crítico ao acessar o Replit: {e}")

# Loop principal para rodar continuamente
if __name__ == "__main__":
    print("Iniciando o serviço de Ping do Replit...")
    while True:
        ping_replit()
        time.sleep(PING_INTERVAL_SECONDS) # Espera 5 minutos  
