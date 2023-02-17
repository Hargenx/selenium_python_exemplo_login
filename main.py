# Instalar o pacote selenium.
# pip install selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

nomeusuario = "Nome de usuario"
senha = "Sua senha"
# Instalar o drive da web para o chrome do selenium.
# !apt-get update
# !apt install chromium-chromedriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

# Executar o navegador e abrir a URL do github no drive da web.
driver.get("https://github.com/login")

# Achar o campo nomedeusuario/email e enviar ao campo.
nuser = driver.find_element("id", "login_field")
nuser.send_keys("username")

# Achar o campo senha enviar ao campo.
pword = driver.find_element("id", "password")
pword.send_keys("password")

# Clicar no botão de entrar no site.
driver.find_element("name", "commit").click()
# Esperar o processo de login se completar.
WebDriverWait(driver=driver, timeout=10).until(
  lambda x: x.execute_script("return document.readyState === 'complete'"))
# Verificar se o login foi sucesso.
erro_messagem = "nome de usuario ou senha incorreto."
# Achar qualquer erro.
erros = driver.find_elements(By.CLASS_NAME, "flash-error")

# Quando encontrar erros, o login vai falhar.
if any(erro_messagem in e.text for e in erros):
  print("[!] Login falhou!")
else:
  print("[+] Login sucesso!")
# Fechar o driver
driver.close()
