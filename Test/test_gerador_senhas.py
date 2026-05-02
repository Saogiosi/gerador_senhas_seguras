# automacao_teste_gerador_senhas.py
# Projeto de automação de testes para o Gerador de Senhas Seguras
# Tecnologia utilizada: Selenium + Python + Pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
class TestGeradorSenhas:
    def setup_method(self):
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://127.0.0.1:5000")
        time.sleep(2)
    def teardown_method(self):
        self.driver.quit()
    # -----------------------------------
    # TESTE 1 - Validar geração com números
    # -----------------------------------
    def test_validar_geracao_com_numeros(self):
        driver = self.driver
        checkbox_numeros = driver.find_element(By.ID, "numeros")
        campo_tamanho = driver.find_element(By.ID, "tamanho")
        botao_gerar = driver.find_element(By.TAG_NAME, "button")
        campo_resultado = driver.find_element(By.ID, "senhaGerada")
        checkbox_numeros.click()
        campo_tamanho.send_keys("8")
        botao_gerar.click()
        time.sleep(2)
        senha = campo_resultado.get_attribute("value")
        assert any(char.isdigit() for char in senha), \
            "A senha gerada não contém números"
    # -----------------------------------
    # TESTE 2 - Validar caracteres especiais
    # -----------------------------------
    def test_validar_caracteres_especiais(self):
        driver = self.driver
        checkbox = driver.find_element(By.ID, "especiais")
        campo_tamanho = driver.find_element(By.ID, "tamanho")
        botao_gerar = driver.find_element(By.TAG_NAME, "button")
        campo_resultado = driver.find_element(By.ID, "senhaGerada")
        checkbox.click()
        campo_tamanho.send_keys("10")
        botao_gerar.click()
        time.sleep(2)
        senha = campo_resultado.get_attribute("value")
        especiais = "!@#$%&*()-_=+[]{};:,.?/"
        assert any(char in especiais for char in senha), \
            "A senha não contém caracteres especiais"
    # -----------------------------------
    # TESTE 3 - Validar mínimo de 4 dígitos
    # -----------------------------------
    def test_validar_minimo_4_digitos(self):
        driver = self.driver
        checkbox = driver.find_element(By.ID, "maiusculas")
        campo_tamanho = driver.find_element(By.ID, "tamanho")
        botao_gerar = driver.find_element(By.TAG_NAME, "button")
        campo_resultado = driver.find_element(By.ID, "senhaGerada")
        checkbox.click()
        campo_tamanho.send_keys("3")
        botao_gerar.click()
        time.sleep(2)
        mensagem = campo_resultado.get_attribute("value")
        assert "entre 4 e 20" in mensagem, \
            "Não validou corretamente o mínimo permitido"
    # -----------------------------------
    # TESTE 4 - Validar máximo de 20 dígitos
    # -----------------------------------
    def test_validar_maximo_20_digitos(self):
        driver = self.driver
        checkbox = driver.find_element(By.ID, "minusculas")
        campo_tamanho = driver.find_element(By.ID, "tamanho")
        botao_gerar = driver.find_element(By.TAG_NAME, "button")
        campo_resultado = driver.find_element(By.ID, "senhaGerada")
        checkbox.click()
        campo_tamanho.send_keys("25")
        botao_gerar.click()
        time.sleep(2)
        mensagem = campo_resultado.get_attribute("value")
        assert "entre 4 e 20" in mensagem, \
            "Não validou corretamente o máximo permitido"
    # -----------------------------------
    # TESTE 5 - Validar nenhum checkbox selecionado
    # -----------------------------------
    def test_validar_sem_checkbox(self):
        driver = self.driver
        campo_tamanho = driver.find_element(By.ID, "tamanho")
        botao_gerar = driver.find_element(By.TAG_NAME, "button")
        campo_resultado = driver.find_element(By.ID, "senhaGerada")
        campo_tamanho.send_keys("8")
        botao_gerar.click()
        time.sleep(2)
        mensagem = campo_resultado.get_attribute("value")
        assert "Selecione ao menos uma opção" in mensagem, \
            "Sistema não validou ausência de seleção"
    # -----------------------------------
    # TESTE 6 - Validar botão copiar senha
    # -----------------------------------
    def test_validar_botao_copiar_senha(self):
        driver = self.driver
        checkbox = driver.find_element(By.ID, "numeros")
        campo_tamanho = driver.find_element(By.ID, "tamanho")
        botoes = driver.find_elements(By.TAG_NAME, "button")
        campo_resultado = driver.find_element(By.ID, "senhaGerada")
        botao_gerar = botoes[0]
        botao_copiar = botoes[1]
        checkbox.click()
        campo_tamanho.send_keys("8")
        botao_gerar.click()
        time.sleep(2)
        senha = campo_resultado.get_attribute("value")
        botao_copiar.click()
        assert senha != "", \
            "Nenhuma senha foi gerada para copiar"