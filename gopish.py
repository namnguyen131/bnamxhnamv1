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
time=datetime.now().strftime("%H:%M:%S%p")
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
#đánh dấu bản quyền
edit = vang+"]"+trang+"["+do+"[⟨⟩]"+trang+"]"+vang+"["+trang+" ➩ "+luc
edit1 = trang+"["+do+"[⟨⟩]"+trang+"]"+trang+" ➩ "+luc
# =======================[ NHẬP KEY ]=======================
import os, sys, requests
from time import sleep
from pystyle import *
from time import strftime
from datetime import datetime, timedelta
now=datetime.now()
os.system("cls" if os.name == "nt" else "clear")
loag = (f'{do}➩ {trang}Đang Xử Lý....')
for x in loag:
  sys.stdout.write(x)
  sys.stdout.flush()
  sleep(0.090)
os.system('espeak -a 300 "Have a nice day"')
logo = f"""

██╗  ██╗ █████╗ ██╗   ██╗███████╗   █████╗   ███╗  ██╗██╗ █████╗ ███████╗  ██████╗  █████╗ ██╗   ██╗
██║  ██║██╔══██╗██║   ██║██╔════╝  ██╔══██╗  ████╗ ██║██║██╔══██╗██╔════╝  ██╔══██╗██╔══██╗╚██╗ ██╔╝
███████║███████║╚██╗ ██╔╝█████╗    ███████║  ██╔██╗██║██║██║  ╚═╝█████╗    ██║  ██║███████║ ╚████╔╝
██╔══██║██╔══██║ ╚████╔╝ ██╔══╝    ██╔══██║  ██║╚████║██║██║  ██╗██╔══╝    ██║  ██║██╔══██║  ╚██╔╝
██║  ██║██║  ██║  ╚██╔╝  ███████╗  ██║  ██║  ██║ ╚███║██║╚█████╔╝███████╗  ██████╔╝██║  ██║   ██║
╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝  ╚═╝  ╚═╝  ╚═╝  ╚══╝╚═╝ ╚════╝ ╚══════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝	
									
									Ấn Enter Để Vào Tool
									






"""
Anime.Fade(Center.Center(logo), Colors.red_to_yellow, Colorate.Vertical, enter=True)
sleep(0)
banner=f"""
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
  sleep(0)
print(f"{trang} ➩ Ngày{trang} : {do}{ngay_hom_nay}{vang} |{luc} Tháng{trang}: {do}{thang_nay} {vang}| {luc}Năm{trang}: {do}{nam_}{vang} | {luc}Thời Gian: {do}{time}")
print(f'{trang} ➩ IP Hiện Tại Của Bạn : {vang}{ip}')
print("\033[1;34m⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦")
print(f"""{do}[{vang}</>{do}]THÔNG BÁO:{vang}.......
{do}[{vang}</>{do}]LƯU Ý: {trang}Sử dụng VPN khi sử dụng tool trao đổi sub facebook tránh bị lock acc ha!""")
print("\033[1;34m⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦")
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[1] \033[1;32mVÀO TOOL TRAO ĐỔI SUB      \033[1;35m  ║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[2] \033[1;32mVÀO TOOL TƯƠNG TÁC CHÉO      \033[1;35m║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[3] \033[1;32mVÀO TOOL TIỆN ÍCH FB        \033[1;35m ║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[4] \033[1;32mVÀO TOOL TIKTOK             \033[1;35m ║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[5] \033[1;32mVÀO TOOL GOLIKE		\033[1;35m║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[6] \033[1;32mVÀO TOOL ENCODE      \033[1;35m        ║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print(f"\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[7] \033[1;32mVÀO TOOL SPAM SMS + CALL    \033[1;35m ║{do}[{vang}Chưa ra mắt{do}] ")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[8] \033[1;32mVÀO TOOL DDOS + DEFACE      \033[1;35m ║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[9] \033[1;32mVÀO TOOL MAIL    	       \033[1;35m ║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[10] \033[1;32mVÀO TOOL PROXY    	       \033[1;35m ║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[11] \033[1;32mVÀO TOOL TIỆN ÍCH KHÁC     \033[1;35m ║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
sleep(0.2)
print("\033[1;35m╔═══════════════════════════════════════╗")
print("\033[1;35m║ \033[1;31m[\033[1;33m</>\033[1;31m]\033[1;36m[0] \033[1;32m THÔNG TIN TOOL	      \033[1;35m  ║ ")
print("\033[1;35m╚═══════════════════════════════════════╝")
print("\033[1;34m⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦⏦")
sleep(0.2)
chon = int(input('\033[1;33mnhn\033[1;95m@\033[1;36mBNamxHNam$ '))
if chon == 1 :
	exec(requests.get('https://run.mocky.io/v3/20d96796-f6a6-489c-918e-156d17751705').text)
elif chon == 2 :
	exec(requests.get('https://run.mocky.io/v3/3a9a0b9a-06c2-4bb8-aedd-5ed4218198d3').text)
elif chon == 3 :
	exec(requests.get('https://run.mocky.io/v3/30c73667-591a-4deb-aa6e-8030f15513d1').text)
elif chon == 4 :
	exec(requests.get('https://run.mocky.io/v3/9fa3d100-be8a-416c-bfe8-9ee68d2478ee').text)
elif chon == 5 :
	exec(requests.get('https://run.mocky.io/v3/e84a781a-0b4a-4e25-8abc-f4a85553a7ef').text)
elif chon == 6 :
	exec(requests.get('https://run.mocky.io/v3/e210f556-7a7a-408d-ab8a-3b866647330c').text)
elif chon == 7 :
	print(f"{do}Chưa ra mắt ní ơi!!")
elif chon == 8 :
	exec(requests.get('https://run.mocky.io/v3/0718d7c0-7e92-44d7-a8fd-c69597d95800').text)
elif chon == 9 :
	exec(requests.get('https://run.mocky.io/v3/dba7453f-6629-490d-bc67-71f1fa54191d').text)
elif chon == 10:
	exec(requests.get('https://run.mocky.io/v3/05e5b7b9-f0bc-400f-b834-74531404e65e').text)
elif chon == 11:
	exec(requests.get('https://run.mocky.io/v3/1fd379c5-f5aa-4cae-9043-f98c76749a06').text)
elif chon == 0:
	exec(requests.get('https://raw.githubusercontent.com/namnguyen131/bnamxhnamtoolish/main/thongtin.py').text)
else :
	sys.exit('Vui Lòng Chọn Đúng Chế Độ!')