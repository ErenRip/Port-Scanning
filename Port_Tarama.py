#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT TARAMA")
print("""

[]-------CodeHub--------[]
[]---------ER3N---------[]
Port Tarama Programına Hoş Geldiniz. 

1) Hızlı Tarama
2) Servis ve Versiyon Bilgisi
3) İşletim Sistemi Bilgisi


[]-------CodeHub--------[]
[]---------ER3N---------[]

""")

islemno = raw_input("İşlem Numarasını Girin: ")


if(islemno=="1"):
	hedefip = raw_input("Hedef İp Girin: ")
	os.system("nmap " + hedefip)
elif(islemno=="2"):
	hedefip = raw_input("Hedef İp Girin: ")
	os.system("nmap -sS -sV " + hedefip)
elif(islemno=="3"):
	hedefip = raw_input("Hedef İp Girin: ")
	os.system("nmap -O " + hedefip)
else:
	print("Hatalı Seçim Yaptınız. Program Kapatılıyor.")
