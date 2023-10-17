from builtins import all,exec,format,id,print,int,range,set,str,open,quit
exec('')
import os
try:
	import requests,colorama,prettytable
except:
	os.system('pip install requests')
	os.system('pip install colorama')
	os.system('pip install prettytable')
import threading,requests,ctypes,random,json,time,base64,sys,re
from prettytable import PrettyTable
import random
from time import strftime
from colorama import init,Fore
from urllib.parse import urlparse,unquote,quote
from string import ascii_letters,digits
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import requests
import base64, json,os
from datetime import date
from datetime import datetime
from time import sleep,strftime
from bs4 import BeautifulSoup
from datetime import datetime
import re,requests,os,sys
from time import sleep 
from datetime import date
import requests, random
import uuid, re
from pystyle import Write,Colors
from bs4 import BeautifulSoup
import socket
from datetime import datetime
time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
#IP
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
import os,sys
import requests,json
from time import sleep
from datetime import datetime, timedelta
import base64,requests,os
#màu
lam = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb="\033[1;37m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
def get_ip_from_url(url):
    response = requests.get(url)
    ip_address = socket.gethostbyname(response.text.strip())
    return ip_address
url = "http://kiemtraip.com/raw.php"
ip = get_ip_from_url(url)
a = "\033[1;31m=>"
hdang = trang + " " + trang + "[" + do + "÷_+" + trang + "] " + trang + "=> "
thanh = "\033[1;37m========================================================="
hd = "\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32m"
# Lmao
thanh_xau=do+'➩' +trang
os.system("cls" if os.name == "nt" else "clear")
loag = (thanh_xau+ ' Đang Xử Lý....')
for x in loag:
  sys.stdout.write(x)
  sys.stdout.flush()
  sleep(0.090)
import random
from atexit import register
from time import sleep
import os,json,re,sys
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests
System.Clear()
dau="\033[1;31m[\033[1;32m⟨⟩\033[1;31m]\033[1;33m➩"
banner = f""" 
\033[1;31m┌══════════════════════════════════════════════════════════════════════════════┐
\033[1;34m ██████╗ ███╗  ██╗ █████╗ ███╗   ███╗      ██╗  ██╗███╗  ██╗ █████╗ ███╗   ███╗
\033[1;35m ██╔══██╗████╗ ██║██╔══██╗████╗ ████║      ██║  ██║████╗ ██║██╔══██╗████╗ ████║
\033[1;33m ██████╦╝██╔██╗██║███████║██╔████╔██║█████╗███████║██╔██╗██║███████║██╔████╔██║
\033[1;32m ██╔══██╗██║╚████║██╔══██║██║╚██╔╝██║╚════╝██╔══██║██║╚████║██╔══██║██║╚██╔╝██║
\033[1;36m ██████╦╝██║ ╚███║██║  ██║██║ ╚═╝ ██║      ██║  ██║██║ ╚███║██║  ██║██║ ╚═╝ ██║
\033[1;31m ╚═════╝ ╚═╝  ╚══╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═╝  ╚═╝╚═╝  ╚══╝╚═╝  ╚═╝╚═╝     ╚═╝
\033[1;34m┠══════════════════════════════════════════════════════════════════════════════┨
\033[1;32m ➯ Cre   : Bảo Nam x Hoàng Nam                                         
\033[1;36m ➯ Nhóm Zalo  : https://zalo.me/g/pdsvkf650                            
\033[1;31m ➯ Facebook Bảo Nam :                         
\033[1;33m ➯ Facebook Hoàng Nam : facebook.com/nam.nhn131                                
\033[1;34m└══════════════════════════════════════════════════════════════════════════════┘
 """
for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)
print(f"{trang} ➩ Ngày{trang} : {do}{ngay_hom_nay}{vang} |{luc} Tháng{trang}: {do}{thang_nay} {vang}| {luc}Năm{trang}: {do}{nam_}{vang}")
print(f'{trang} ➩ IP Hiện Tại Của Bạn : {vang}{ip}')
ngay=int(strftime('%d'))
key1= str('key3ngay')
key = 'bnamxhnam'+key1
url = 'https://namtool131.000webhostapp.com/key.php?key='+key
token_link1s = 'e41deba5-b008-44d1-a6a4-19b9e4519e01'
link1s = requests.get(f'https://web1s.com/api?token={token_link1s}&url={url}').json()
if link1s['status']=="error": 
    print(link1s['message'])
    quit()
else:
    link_key=link1s['shortenedUrl']
h=open('KEYTOOL.txt',mode='a+')
h=open('KEYTOOL.txt',mode='r')
thien=h.read()
h.close()
print()
if thien== keyv1 or thien== key:
    print('\033[1;31m ➩\033[1;37m Chào Mừng Bạn Đến Với Tool Của Bảo Nam x Hoàng Nam!!!')
    sleep(1)
    exec(requests.get('https://run.mocky.io/v3/865328af-0af7-432d-bb4a-d0f7eef261e2').text)
else:
     print('\033[1;31m ➩ \033[1;37m  [  Nhập Link Để Vào Tool Miễn Phí ]')
     print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =')
print('\033[1;31m ➩ \033[1;37mLink Lấy Key Free :\033[1;31m '+link_key)
print('\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =')
keynhap = input('\033[1;31m ➩ \033[1;37mNhập Key Đã Vượt\033[1;37m :\033[1;33m ')
print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
if keynhap == key or keynhap== keyv1:
    print('\033[1;31m ➩\033[1;37m Key Đúng Rồi ! Mời Bạn Vào Tool')
    print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
    sleep(2)
    h=open('KEYTOOL.txt',mode='w')
    h.write(keynhap)
    h.close()
    exec(requests.get('https://run.mocky.io/v3/865328af-0af7-432d-bb4a-d0f7eef261e2').text)
else:
    print('\033[1;31m ➩\033[1;37m Key Sai Rồi ! Hãy Nhập Lại Key')
    print("\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = ")
