# Generated by Selenium IDE

import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/bin/chromedriver')
class TestCadastrodemanda():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/bin/chromedriver')
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cadastrodemanda(self):
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(1280, 672)
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(1) img").click()
    self.driver.find_element(By.ID, "titulo").click()
    self.driver.find_element(By.ID, "titulo").send_keys("Calculo")
    self.driver.find_element(By.NAME, "select_tag0").click()
    dropdown = self.driver.find_element(By.NAME, "select_tag0")
    dropdown.find_element(By.XPATH, "//option[. = 'COMPUTAÇÃO - Programação Estruturada']").click()
    self.driver.find_element(By.CSS_SELECTOR, "form").click()
    self.driver.find_element(By.ID, "titulo").send_keys("Ponteiros")
    self.driver.find_element(By.CSS_SELECTOR, ".demanda-grupo > label").click()
    self.driver.find_element(By.ID, "descricao-demanda").click()
    self.driver.find_element(By.ID, "descricao-demanda").send_keys("me ajuda")
    self.driver.find_element(By.CSS_SELECTOR, ".botao-cadastro").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card:nth-child(2) img").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td:nth-child(6) img").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td:nth-child(7) img").click()