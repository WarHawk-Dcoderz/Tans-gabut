def salam(kata):
     print (kata) 

salam('\033[1;35m jones :b,hiyaaaa jones')
nama = input('\033[1;32m Siapa Namamu? : ')

print ('\033[1;32m Selamat datang', nama)

import requests,os
os.system('clear')

print ("\033[1;32m❛ ━━━━━･━━━━━━･━━━━━━･❪ ❁ ❫ ･━━━━━━ ━━━━━･━━━━━━･❜")
print ("\033[1;31m[\033[1;37m1\033[1;31m] \033[1;33m Author=Tania`27")
print ("\033[1;31m[\033[1;37m1\033[1;31m] \033[1;33m WA   =08993307590")
print ("\033[1;32m❛ ━━━━━･━━━━━━･━━━━━━･❪ ❁ ❫ ･━━━━━━ ━━━━━･━━━━━━･❜")


import requests, os


def cekip():
 print(f'[!] Mendapatkan IP..')
 re = requests.get('https://api.myip.com').json()
 ip = re['ip']
 print(f'[!] IP kamu : {ip}')
 
def sms():
 print(f'[!] Menginstall tools sms..')
 os.system('cd sms')
 os.system('python sms.py')
 
def call():
 print(f'[!] Menginstall tools spam call..')
 os.system('cd callspam')
 os.system('php callspam.php')
 
def spamsms():
 print(f'[!] Menginstall tools spam sms..')
 os.system('cd spamsms')
 os.system('php spamsms.php')
 
 
import random
import sys
import time
def mengetik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()

        time.sleep(random.random() * 0.1)

mengetik("\033[1;36m Ciee,ketemu lagi sama Tania yang Canss ini .hayuu dipilih : ")


print("\033[1;32m╬╬═══════════════╬╬")
print ("\033[1;31m[\033[1;37m1\033[1;31m] \033[1;33m akses Go.id")
print("\033[1;32m╬╬═══════════════╬╬")
print ("\033[1;31m[\033[1;37m2\033[1;31m] \033[1;33m akses sch.id")
print("\033[1;32m╬╬═══════════════╬╬")
print ("\033[1;31m[\033[1;37m3\033[1;31m]\033[1;33m Akses Gov.in")
print("\033[1;32m╬╬═══════════════╬╬")
print ("\033[1;31m[\033[1;37m4\033[1;31m]\033[1;33m cek ip")
print("\033[1;32m╬╬═══════════════╬╬")
print ("\033[1;31m[\033[1;37m5\033[1;31m]\033[1;33m sms gratis ")
print("\033[1;32m╬╬═══════════════╬╬")
print ("\033[1;31m[\033[1;37m6\033[1;31m]\033[1;33m Spam Telepon ")
print("\033[1;32m╬╬═══════════════╬╬")
print ("\033[1;31m[\033[1;37m7\033[1;31m]\033[1;33m Spam Sms ")
print("\033[1;32m╬╬═══════════════╬╬")

menu = input("\033[1;32m Hayoo mau yang manaa: ")
if menu =="1":
      print ("\033[1;36m Ciee yang ketipu :b,kok minta sih,berjuang dong ishh ,btw ini kan nggak bisa,coba pilih yang nomor dua,sipa tau bisa,soalnya ini kan random" )

elif menu == "2":
      print ("\033[0;31m Ciee ketipu lagii ,unchh Marah yah ,kaciaaan ,deface sendiri lah kak,jangan minta minta akses ,huh dasar 2k19,btw no.3 itu beneran ada lohh,coba lagi")

elif menu == "3":
      print ("\033[0;37m Aq kasian sama anak ini yaampun,hmm yaudah deh ,chat WA tania ajh ,nanti tania kasih ,")

elif menu == "4":cekip()
elif menu == "5":sms()
elif menu == "6":call()
elif menu == "7":spamsms()