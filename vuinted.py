from selenium import webdriver
import selenium
import httpsreqfast.init
import time
import os
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_extension('buster.crx')

#driver = webdriver.Chrome(r'C:\chromedriver.exe')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

os.system("cls")
link = input("[*] Lien de votre article a boost : ")
vu = input("[*] Nombre de vu a ajouté : ")

for x in range(vu):
	driver.get(link)
	print("[*] +1 vu")
	time.sleep(2)
