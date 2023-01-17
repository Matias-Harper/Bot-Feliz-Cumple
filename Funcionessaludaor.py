from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.common.exceptions
import time
import random
import pandas as pd
from datetime import datetime

#abrimos una sesión chrome
def path():
    global chrome
    chrome = webdriver.Chrome()

#cerramos la sesión
def pathclose():
    global chrome
    chrome = webdriver.Chrome()
    chrome.close()

#función que nos permite entrar a una url 
def url_name(url):
    chrome.get(url)
    #ponemos un tiempo de espera que será de "carga"
    time.sleep(4)

#Como realice esto? hay que abrir Instagram en una ventana incognito y ver los diferentes pasos
# a realizar para poder entrar en la cuenta que se quiere entrar, siempre poniendo tiempos de sleep para que parezca que lo hace una persona
def login(username,password):
    boton_entrar = chrome.find_element(By.CLASS_NAME, "_aaco")
    boton_entrar.click()
    time.sleep(3)

    user = chrome.find_element(By.NAME,"username")
    user.send_keys(username)
    time.sleep(3)

    passw = chrome.find_element(By.NAME,"password")
    passw.send_keys(password)

    #simulamos el apretar enter
    passw.send_keys(Keys.RETURN)
    time.sleep(5)
    #aca cuando se repite el código no aparece la ventana y genera el error "NoSuchElementException" asi que lo hacemos como considereando el posible error
    try:
        noguardardatos = chrome.find_element(By.CLASS_NAME,"_aiit")
        noguardardatos.click()
        time.sleep(4)
    except: 
        time.sleep(3)


def send_msj(texto):
    #ahora estamos parados en el Instagram de la persona que queremos mandarle el mensaje
    boton_env_mensj = chrome.find_element(By.CLASS_NAME, "xjqpnuy")
    boton_env_mensj.click()
    time.sleep(3)
    #no_notif = chrome.find_element(By.CLASS_NAME,"_a9_1")
    #aca cuando se repite el código no aparece la ventana y genera el error "NoSuchElementException" asi que lo hacemos como considereando el posible error
    try:
        no_notif=chrome.find_element(By.XPATH,"//*[contains(@class,'_a9-- _a9_1')]")
        no_notif.click()
        time.sleep(2)
    except :
        time.sleep(2)
    m_box = chrome.find_element(By.TAG_NAME,"textarea")
    m_box.send_keys(texto)
    m_box.send_keys(Keys.RETURN)
   
def birthday_check():
    #Esta función se fija si tenemos gente que cumple años en el dia
    df_bday =pd.read_excel("Listacumples.xlsx")
    df_bday["month"]= pd.DatetimeIndex(df_bday["Birthday"]).month
    df_bday["day"]= pd.DatetimeIndex(df_bday["Birthday"]).day
    #Convertimos algunas columnas en listas para usarlas mas fácil 
    name=list(df_bday["Name"])
    birthdate_month=list(df_bday["month"])
    birthdate_day=list(df_bday["day"])
    instaname=list(df_bday["Instagram"])

    #Creamos un diccionario con esta información, Key = nombre, Data =(mes, dia, Instagram)
    dictionary={}
    for i in range(len(name)):
        dictionary[name[i]]=(birthdate_month[i],birthdate_day[i],instaname[i])

    #en una variable ponemos el mes y dia en el que estamos
    date=datetime.now().month,datetime.now().day

    #generaremos una lista que tenga los Instagram de las personas que cumplan este dia
    instanames=[]
    for i in dictionary:
        if dictionary[i][0:2]==date:
            instanames.append(dictionary[i][-1])
    return (instanames)
