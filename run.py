import marshal
import os,re,sys,bs4,time,json,random,datetime,requests, calendar, random


header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}
ses=requests.Session()

#warna coeg
K = "\x1b[0;33m"
N = "\x1b[0m" 
B = "\x1b[0;34m"
M = "\x1b[0;31m"
H = "\x1b[0;32m"

def logo():
	loo=f"""
______________________
\_   _____/\__    ___/
 |    __)    |    |   
 |     \     |    |  {B}FACEBOOK TOOLS {N}
 \___  /     |____|        {N}2022
     \/{H}  Github.com/zhukov-z{N}               """
	print(f"  {loo}{N}   \n ")
	
#loggin
def login():
	logo()
	try:
		cookie = input(" ? cookie fb : ")
		get_tok = requests.get('https://business.facebook.com/business_locations',headers = {"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"},cookies = {"cookie":cookie})
		tokenz = re.search("(EAAG\w+)", get_tok.text).group(1)
		coki = {"cookie":cookie}
	except Exception as e:
		exit("coki modar")
	idt = input(f" ? masukan link : {H} ")
	limit = int(input(f" {N}? {N}masukan limit : {H} "))
	print(f"\n\t\t{H}ctrl+z {N}untuk berhenti\n")
	token = tokenz 
	cookie = coki
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
	login()
