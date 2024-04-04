import psutil  # Biblioteca para monitoramento de processos
import subprocess  # Biblioteca para executar comandos do sistema
import time
import datetime
import pystray
from PIL import Image 
import sys 
import threading

def check_memory_usage():
    # Obtém o uso de memória atual
    memory_usage = psutil.virtual_memory().percent
    return memory_usage

statusServico = ''
def check_service_status(service_name):
    service_name.replace("\n","")
    # Comando para verificar o status do serviço no Windows
    status_command = f"sc query {service_name} | findstr RUNNING"

    # Executa o comando e verifica se está em execução
    result = subprocess.run(status_command, shell=True, capture_output=True, text=True)
    if "RUNNING" in result.stdout:
        return True
    else:
        return False

def get_service(name):
    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:
        # raise psutil.NoSuchProcess if no service with such name exists
        print(str(ex))

    return service

def take_action(service_name, memory_threshold=98):
    # Verifica o uso de memória e o status do serviço
    global statusServico
    memory_usage = check_memory_usage()
    service_status = check_service_status(service_name)
    serviceisinstalled = get_service(service_name)
    # Se o uso de memória for superior ao limite e o serviço estiver em execução, reinicia o serviço
    if serviceisinstalled:
        pass
    else:
        icon.notify(f"O servico {service_name} nao esta instalado, favor verificar tomcats.txt e corrigir")
        
    if memory_usage > memory_threshold and service_status:
        statusServico = f"O serviço {service_name} está utilizando mais de 98% de memória. Reiniciando o serviço..."
        print(f"O serviço {service_name} está utilizando mais de 98% de memória. Reiniciando o serviço...")
        subprocess.run(f"sc stop {service_name}", shell=True)
        subprocess.run(f"sc start {service_name}", shell=True)
        print(f"O serviço {service_name} foi reiniciado.")
    elif not service_status:
        statusServico= f"O serviço {service_name} está parado, iniciando..."
        print(f"O serviço {service_name} está parado, iniciando...")
        with open("log_deploy.txt",'w+') as f:
            f.write(f"O serviço {service_name} está parado, iniciando..."+ str(datetime.datetime.now()))
        subprocess.run(f"sc start {service_name}", shell=True)
    else:
        statusServico=f"O serviço {service_name} está em execução e dentro dos limites de memória."
        print(f"O serviço {service_name} está em execução e dentro dos limites de memória.")


systrayImage = Image.open('deploy.jpg')


def after_click_systray(icon, item):
    if str(item) == 'Exit':
        icon.stop()
    elif str(item) == "Status":
        print(statusServico)
        icon.notify(statusServico)


def exit_program(icon):
    icon.stop()
    sys.exit(0)

icon = pystray.Icon("Deploy", systrayImage, menu=pystray.Menu(
    pystray.MenuItem('Exit',exit_program),
    pystray.MenuItem("Status",after_click_systray),
   # pystray.MenuItem("exit",exit_program())
))

def run_icon():
    icon.run()

if __name__ == "__main__":
    icon_thread = threading.Thread(target= run_icon)
    icon_thread.start()
    while True:
        # Nome do serviço do Tomcat
        with open('tomcats.txt') as file:
            for line in file:
                tomcat_service_name = line.strip()
                take_action(tomcat_service_name)
        time.sleep(300)  # Verifica a cada 5 minutos
