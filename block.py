# Inicie esse script na raiz
  
import time 
from datetime import datetime as dt 
  
# Selecione o diretório hosts de sua máquina
#hosts_path = "C:\Windows\System32\drivers\etc\hosts"
hosts_path = str(input("Digite o caminho do diretório: "))
# IP Local
redirect = "127.0.0.1"
  
# Sites que vão ser bloqueados
website_list = ["www.facebook.com","facebook.com", "www.youtube.com", "web.whatsapp.com", "www.twitter.com", "www.instagram.com", "youtube.com", "twitter.com", "instagram.com"] 
try:  
    while True: 
        # Tempo de bloqueio 
        if dt(dt.now().year, dt.now().month, dt.now().day,8)< dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16): 
            print("Bloqueando...") 
            with open(hosts_path, 'r+') as file: 
                content = file.read() 
                for website in website_list: 
                    if website in content: 
                        pass
                    else: 
                        # Mapeando hostnames para endereços locais 
                        file.write(redirect + " " + website + "\n") 
        else:
            with open(hosts_path, 'r+') as file: 
                content=file.readlines() 
                file.seek(0) 
                for line in content: 
                   if not any(website in line for website in website_list): 
                       file.write(line)
except KeyboardInterrupt:          
                with open(hosts_path, 'r+') as file: 
                    content=file.readlines() 
                    file.seek(0) 
                    for line in content: 
                       if not any(website in line for website in website_list): 
                           file.write(line)
                           file.truncate()
                print("Finish") 
                
