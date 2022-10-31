# -*- coding: utf-8 -*-
#cria um alerta automatico no whatsapp para lembrar as pessaos a tomarem agua

from IPython.display import display
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib 

contatos_df = pd.read_excel("Enviar.xlsx")
display(contatos_df)

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

# "site" eh um elemento que so existe quando o whatsapp ja fez o login
#while len(find_element(By.ID, 'side')) < 1:
while len(navegador.find_elements(by=By.ID, value='side')) < 1:  #enquanto o tamanho da lista for <1
  time.sleep(1) #espera 1 segundo

#login do whatsapp web ja esta feito

#enviando as mensagens
for i, mensagem in enumerate(contatos_df['Mensagem']):
  pessoa = contatos_df.loc[i, "Pessoa"]
  numero = contatos_df.loc[i, "Numero"]
  texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
  link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
  navegador.get(link)
  
  while len(navegador.find_elements(by=By.ID, value='side')) < 1:  #enquanto o tamanho da lista for <1
    time.sleep(1) #espera 1 segundo
  
  apertarEnter = navegador.find_element(by=By.XPATH, value='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p')
  apertarEnter.send_keys(Keys.ENTER)
  time.sleep(10)