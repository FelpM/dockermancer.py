#Felipe de Resende
#Suellen Guedes


import requests
import subprocess

def executar_comando_docker(api_url, comando_docker):
    try:
        # Enviar uma solicitação POST para a API Docker com o comando
        response = comando_docker
        print(f"Status da resposta: {response.status_code}")
        print(f"Resposta: {response.text}")
        
        # Verificar se a solicitação foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            return response.text
        else:
            return f"Erro ao executar o comando: {response.text}"
    except Exception as e:
        return f"Erro ao executar o comando: {str(e)}"

def main():
    print("__<<SIMPLE DOCKER MANAGEMENT & CONTROLLER>>__")
    api_url = input("Digite a URL da API Docker:")  # Por exemplo, http://localhost:2375
    while True:
        # Solicitar ao usuário que escolha o comando
        print("Escolha um comando:")
        print("1. List containers")
        print("2. Create a container")
        print("3. Inspect a container")
        print("4. List processes running inside a container")
        print("5. Get container logs")
        print("6. Get changes on a container’s filesystem")
        print("7. Get container stats based on resource usage")
        print("8. Start a container")
        print("9. Stop a container")
        print("10. Restart a container")
        print("11. Kill a container")
        print("12. Rename a container")
        print("13. Pause a container")
        print("14. Unpause a container")
        print("15. Remove a container")
        print("16. Delete stopped containers")
        print("17. List Images")
        print("18. Inspect Images")
        print("19. Remove an image")
        print("20. Get system information")
        print("21. Get data usage information")
        print("22. Get data usage information")
        print("23. Get version")
        print("24. List network")
        print("25. List config")
        opcao = input("Digite o número do comando desejado: ")

        # Definir o comando escolhido com base na opção do usuário
        if opcao == "1":
            comando_docker = requests.get(api_url + "/containers/json?all=1")
        elif opcao == "2":
            nome_da_imagem = input("Digite o nome da imagem utilizada: ")
            comando_docker = requests.post(api_url + "/containers/create", json={"Image": nome_da_imagem})
        elif opcao == "3":
            id = input("Digite o ID do container para inspecionar: ")
            comando_docker = requests.get(api_url + f"/containers/{id}/json")
        elif opcao == "4":
            id = input("Digite o ID do container para listar processos: ")
            comando_docker = requests.get(api_url + f"/containers/{id}/top")
        elif opcao == "5":
            id = input("Digite o ID do container para capturar logs: ")
            comando_docker = requests.get(api_url + f"/containers/{id}/logs")
        elif opcao == "6":
            id = input("Digite o ID do container para obter mudanças no sistema de arquivos: ")
            comando_docker = requests.get(api_url + f"/containers/{id}/changes")
        elif opcao == "7":
            id = input("Digite o ID do container para obter estatísticas: ")
            comando_docker = requests.get(api_url + f"/containers/{id}/stats")
        elif opcao == "8":
            id = input("Digite o ID do container para iniciar: ")
            comando_docker = requests.post(api_url + f"/containers/{id}/start")
        elif opcao == "9":
            id = input("Digite o ID do container para parar: ")
            comando_docker = requests.post(api_url + f"/containers/{id}/stop")
        elif opcao == "10":
            id = input("Digite o ID do container para reiniciar: ")
            comando_docker = requests.post(api_url + f"/containers/{id}/restart")
        elif opcao == "11":
            id = input("Digite o ID do container para matar: ")
            comando_docker = requests.post(api_url + f"/containers/{id}/kill")
        elif opcao == "12":
            id = input("Digite o ID do container para renomear: ")
            novo_nome = input("Digite o novo nome: ")
            comando_docker = requests.post(api_url + f"/containers/{id}/rename?name={novo_nome}")
        elif opcao == "13":
            id = input("Digite o ID do container para pausar: ")
            comando_docker = requests.post(api_url + f"/containers/{id}/pause")
        elif opcao == "14":
            id = input("Digite o ID do container para despausar: ")
            comando_docker = requests.post(api_url + f"/containers/{id}/unpause")
        elif opcao == "15":
            id = input("Digite o ID do container para remover: ")
            comando_docker = requests.delete(api_url + f"/containers/{id}")
        elif opcao == "16":
            comando_docker = requests.post(api_url + "/containers/prune")
        elif opcao == "17":
            comando_docker = requests.get(api_url + "/images/json")
        elif opcao == "18":
            id = input("Digite o ID da imagem para inspecionar: ")
            comando_docker = requests.get(api_url + f"/images/{id}/json")
        elif opcao == "19":
            id = input("Digite o ID da imagem para remover: ")
            comando_docker = requests.delete(api_url + f"/images/{id}")
        elif opcao == "20":
            comando_docker = requests.get(api_url + "/info")
        elif opcao == "21":
            comando_docker = requests.get(api_url + "/system/df")
        elif opcao == "22":
            comando_docker = requests.get(api_url + "/system/df")
        elif opcao == "23":
            comando_docker = requests.get(api_url + "/version")
        elif opcao == "24":
            comando_docker = requests.get(api_url + "/networks")
        elif opcao == "25":
            comando_docker = requests.get(api_url + "/configs")
        else:
            print("Opção inválida.")
            exit()

        # Executar o comando escolhido
        saida = executar_comando_docker(api_url, comando_docker)
        print("\nSaída do comando:")
        print(saida)
 
if __name__ == "__main__":
    main()

