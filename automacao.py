import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://plataforma-arquitetura.streamlit.app/"

def acordar_streamlit():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] A aceder à plataforma...")
    
    # Configuração robusta para o ambiente Linux do GitHub Actions
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Obrigatório para rodar no GitHub Actions
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")  # Simula uma resolução de ecrã normal
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get(URL)
        
        # Aguarda que a página carregue o estado inicial
        print("A aguardar carregamento da página (10s)...")
        time.sleep(10)
        
        # --- TENTATIVA 1: Procurar pelo botão com o texto "Wake up" ---
        try:
            print("A tentar localizar o botão 'Wake up' pelo texto...")
            botao_wake_up = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Wake up') or contains(text(), 'Wake up app')]"))
            )
            botao_wake_up.click()
            print("Botão 'Wake up' encontrado e clicado! A app está a acordar...")
            time.sleep(20)  # Aguarda a app iniciar após o clique
            print("Processo concluído com sucesso.")
            return
            
        except Exception:
            print("Botão de texto 'Wake up' não foi encontrado. A tentar seletor alternativo...")

        # --- TENTATIVA 2: Seletor alternativo por componentes comuns do Streamlit ---
        try:
            botao_alt = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid='stStatusWidget'] button, .stButton button"))
            )
            botao_alt.click()
            print("Botão alternativo estrutural clicado! A app está a acordar...")
            time.sleep(20)
            print("Processo concluído com sucesso.")
            return
            
        except Exception:
            print("Nenhum botão de suspensão foi encontrado.")
            
        # Se chegou aqui, a app provavelmente já estava acordada e funcional
        print("A app já parece estar acordada e ativa. Nada a fazer.")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        
    finally:
        driver.quit()
        print("Sessão do navegador encerrada.\n")

if __name__ == "__main__":
    acordar_streamlit()
