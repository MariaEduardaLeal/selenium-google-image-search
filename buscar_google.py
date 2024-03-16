#Importando SELENIUM e webdriver para poder usar o CHROME
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#IMPORTA O DRIVER DO GOOGLE PARA QUE NÃO PRECISE BAIXAR DIRETO DO NAVEGADOR
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#Verifica a versão do seu google chrome e ele mesmo já instala o chrome driver referente aquela versão
servico = Service(ChromeDriverManager().install())
#Criando instância do CHROMEDRIVER passando o chromedriver intalado automaticamente
navegador = webdriver.Chrome(service=servico)

#Abre a página desejada
navegador.get("https://www.google.com/")

# Localizando o campo de pesquisa e inserindo o termo de pesquisa
campo_pesquisa = navegador.find_element('xpath', '//*[@name="q"]')
campo_pesquisa.send_keys('Imagens de Cachorro')

# Enviando o formulário (simulando um submit)
campo_pesquisa.submit()

# Aguardando a entrada do usuário para fechar o navegador
input("Pressione Enter para fechar o navegador...")

# Fechando o navegador
navegador.quit()
