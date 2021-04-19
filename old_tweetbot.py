from random import randint
import tweepy
from termcolor import colored
import requests
from bs4 import BeautifulSoup
import os

## Script que eu usava para fazer web scraping do site de SP e pegar os valores do otal de vacinados e fazer o tweet
## Old pois a ideia agora é pegar os dados de um arquivo disponibilizado pelo https://coronavirusbra1.github.io/

def keys():
    global api
    twitter_auth_keys = { 
        "consumer_key"        : "yay",
        "consumer_secret"     : "yay",
        "access_token"        : "yay",
        "access_token_secret" : "yay"
    }
    auth = tweepy.OAuthHandler(twitter_auth_keys['consumer_key'], twitter_auth_keys['consumer_secret'])
    auth.set_access_token(twitter_auth_keys['access_token'], twitter_auth_keys['access_token_secret'])
    api = tweepy.API(auth)

keys()

def saopaulo():
    #make requests
    request_sp = requests.get("https://vacinaja.sp.gov.br/")
    soup_sp = BeautifulSoup(request_sp.content, 'html.parser')
    #scarping
    data_sp = soup_sp.find(class_='data-atualizacao-vac')
    num_sp = soup_sp.find(class_='pane')
    #now int trans
    now_num_sp_split = num_sp.text.split(".")
    now_int_sp = int(now_num_sp_split[0]+now_num_sp_split[1]+now_num_sp_split[2])
    #old int trans
    old_file_sp = open('sp.num', "r")
    old_num_sp = old_file_sp.read()
    old_num_sp_split = old_num_sp.split(".")
    old_int_sp = int(old_num_sp_split[0]+old_num_sp_split[1]+old_num_sp_split[2])
    print(old_num_sp)
    #today
    today_sp = now_int_sp - old_int_sp
    #save in a file 
    if os.path.exists('sp.num'):
        os.remove('sp.num') 
    file_sp = open("sp.num", "w")
    file_sp.write(str(num_sp.text))
    #payload
    global payload_sp
    payload_sp = f"""
    [💉🦠] Informações sobre a vacinação no Estado de São Paulo:
    {data_sp.text}
    Número de vacinados hoje: {today_sp}
    Número de vacinados até agora: {num_sp.text}
    """


print(colored("botzinho :]", "blue"))
print(colored("\n[+] Verifying creds...", "yellow"))
try:
    api.verify_credentials()
    print(colored("[i] Authentication OK", "green"))
except:
    print(colored("[i] Error during authentication", "red"))


print(colored("[+] Tweeting...", "yellow"))


try:
    saopaulo()
    api.update_status(payload_sp)
    print(payload_sp)
    print(colored("[i] Success!", "green"))
except:
    print(colored("[i] Error", "red"))

