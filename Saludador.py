from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.common.exceptions
import time
import random
import pandas as pd
from datetime import datetime

#importamos el usuario y contraseña, debe completarse el documento que se llama contras2 
from contras import password, username
#importamos las funciones 
from Funcionessaludaor import *

path()
instanames=birthday_check()
time.sleep(1)
url_name("https://instagram.com/matiasnharper")
login(username, password)
for i in instanames:
    url= 'https://instagram.com/' + i
    url_name(url)
    mensaje = "en este lugar ponermos el texto que queremos que se envie por medio del bot"
    send_msj(mensaje)
    time.sleep(4)
pathclose()