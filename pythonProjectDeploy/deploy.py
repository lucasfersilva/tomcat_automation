import psutil  
import subprocess  
import time


def check_memory_usage():
    # Obtém o uso de memória atual
    memory_usage = psutil.virtual_memory().percent
    return memory_usage


def check_service_status(service_name):
    # Comando para verificar o status do serviço no Windows
    status_command = f"sc query {service_name} | findstr RUNNING"

    # Executa o comando e verifica se está em execução
    result = subprocess.run(status_command, shell=True, capture_output=True, text=True)
    if "RUNNING" in result.stdout:
        return True
    else:
        return False


def take_action(service_name, memory_threshold=90):
    # Verifica o uso de memória e o status do serviço
    memory_usage = check_memory_usage()
    service_status = check_service_status(service_name)

    # Se o uso de memória for superior ao limite e o serviço estiver em execução, reinicia o serviço
    if memory_usage > memory_threshold and service_status:
        print(f"O serviço {service_name} está utilizando mais de 80% de memória. Reiniciando o serviço...")
        subprocess.run(f"sc stop {service_name}", shell=True)
        subprocess.run(f"sc start {service_name}", shell=True)
        print(f"O serviço {service_name} foi reiniciado.")
    elif not service_status:
        print(f"O serviço {service_name} está parado.")
    else:
        print(f"O serviço {service_name} está em execução e dentro dos limites de memória.")


if __name__ == "__main__":


    while True:
        # Nome do serviço do Tomcat
        with open('tomcats.txt') as file:
            for line in file:
                tomcat_service_name = line
                take_action(tomcat_service_name)
        time.sleep(300)  # Verifica a cada 5 minutos
