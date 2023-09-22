#Felipe de Resende
#Suellen Guedes


import subprocess

def executar_comando_docker(comando):
    try:
        # Executar o comando Docker e capturar a saída
        saida = subprocess.check_output(comando, universal_newlines=True, stderr=subprocess.STDOUT)
        return saida
    except subprocess.CalledProcessError as e:
        # Lidar com erros, se houver algum
        return f"Erro ao executar o comando: {e.output}"
        
    
def main ():
    print("__<<SIMPLE DOCKER MAGEMENT & CONTROLLER>>__")
    IP = input("DIgite o alvo IP:PORTA -> ")
    while True:
               

        # Solicitar ao usuário que escolha o comando
        print("Escolha um comando:")
        print("1. Listar Containers")
        print("2. Listar imagens")
        print("3. Listar Processos de um Container")
        print("4. Capturar Logs de um Container")
        print("5. Iniciar um Container")
        print("6. Parar um Container")
        print("7. Reiniciar um Container")
        print("8. Matar um Container")
        print("9. Remover um Container")
        print("10. Remover uma Imagem")
        print("11. Obter Informações do Sistema")
        print("12. Obter Dados de Uso")
        print("13. Obter Versão do Docker")
        print("14. Obter um shell interativa")
        print("15. Criar Container")
        print("16. Baixar imagem")
        opcao = input("Digite o número do comando desejado: ")

        # Definir o comando escolhido com base na opção do usuário
        if opcao == "1":
            comando_docker = ["sudo", "docker", "-H", IP, "ps"]
        elif opcao == "2":
            comando_docker = ["sudo", "docker", "-H", IP, "images"]
        elif opcao == "3":
            container_id = input("Digite o ID do container para listar processos: ")
            comando_docker = ["sudo", "docker", "-H", IP, "top", container_id]
        elif opcao == "4":
            container_id = input("Digite o ID do container para capturar logs: ")
            comando_docker = ["sudo", "docker", "-H", IP, "logs", container_id] 
        elif opcao == "5":
            container_id = input("Digite o ID do container para iniciar: ")
            comando_docker = ["sudo", "docker", "-H", IP, "start", container_id]
        elif opcao == "6":
            container_id = input("Digite o ID do container para parar: ")
            comando_docker = ["sudo", "docker", "-H", IP, "stop", container_id]
        elif opcao == "7":
            container_id = input("Digite o ID do container para reiniciar: ")
            comando_docker = ["sudo", "docker", "-H", IP, "restart", container_id]
        elif opcao == "8":
            container_id = input("Digite o ID do container para matar: ")
            comando_docker = ["sudo", "docker", "-H", IP, "kill", container_id]
        elif opcao == "9":
            container_id = input("Digite o ID do container para remover: ")
            comando_docker = ["sudo", "docker", "-H", IP, "rm", container_id]
        elif opcao == "10":
            imagem_id = input("Digite o ID da imagem para remover: ")
            comando_docker = ["sudo", "docker", "-H", IP, "rmi", imagem_id]
        elif opcao == "11":
            comando_docker = ["sudo", "docker", "-H", IP, "info"]
        elif opcao == "12":
            comando_docker = ["sudo", "docker", "-H", IP, "stats"]
        elif opcao == "13":
            comando_docker = ["sudo", "docker", "-H", IP, "--version"]
        elif opcao == "14":
            container_id = input("Digite o ID do container, para rodar: ")
            comando_docker = ["sudo", "docker", "-H", IP, "exec", "-it", container_id, "/bin/bash"]
            processo = subprocess.Popen(comando_docker)
            processo.communicate() 
        elif opcao == "15":
            nome_imagem = input("Digite o nome da imagem para criar o container: ")
            comando_docker = ["sudo", "docker", "-H", IP, "run", "-d", nome_imagem, "tail", "-f", "/dev/null"]
        elif opcao == "16":
            nome_imagem = input("Digite o nome da imagem para baixar: ")
            comando_docker = ["sudo", "docker", "pull", nome_imagem]
        else:
            print("Opção inválida.")
            exit()

        # Executar o comando escolhido
        saida = executar_comando_docker(comando_docker)
        print("\nSaída do comando:")
        print(saida)

if __name__ == "__main__":
    main()
