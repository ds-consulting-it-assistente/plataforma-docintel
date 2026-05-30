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
    
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Ativa para rodar em background no GitHub/Servidor
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get(URL)
        
        # Aguarda um pouco para a página de suspensão carregar o botão
        print("A verificar se a app está a dormir...")
        time.sleep(8)
        
        # Tentativa 1: Procurar pelo botão que contém o texto "Wake up"
        # O Streamlit costuma usar letras maiúsculas/minúsculas específicas, usamos contains para garantir
        try:
            print("A tentar localizar o botão 'Wake up'...")
            botao_wake_up = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Wake up') or contains(text(), 'Wake up app')]"))
            )
            
            botao_wake_up.click()
            print("Botão clicado! A app está a acordar...")
            
            # Como a app demora um pouco a iniciar após acordar, esperamos 15-20 segundos
            time.sleep(20)
            print("App deverá estar ativa agora.")
            
        except Exception:
            # Tentativa 2: Se não encontrar pelo texto (por causa de atualizações de idioma), tenta pelo seletor de botão genérico do ecrã de standby
            print("Botão de texto não encontrado. A tentar seletor alternativo...")
            botao_alt = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "div[data-testid='stStatusWidget'] button, .stButton button"))
            )
            botao_alt.click()
            print("Botão alternativo clicado.")
            time.sleep(20)

    except Exception as e:
        print(f"A app já estava acordada ou ocorreu um erro: {e}")
        # Se quiseres perceber o que o robô estava a ver, descomenta a linha abaixo para guardar uma imagem:
        # driver.save_screenshot("estado_da_app.png")
        
    finally:
        driver.quit()
        print("Sessão encerrada.\n")

if __name__ == "__main__":
    acordar_streamlit()
