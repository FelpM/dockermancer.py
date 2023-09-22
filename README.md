# TÍTULO E IMAGEM DE CAPA

<h1 align="center"> Dockermancer </h1>

![Docekr](https://github.com/FelpM/dockermancer.py/blob/main/necromancer.jpg)


# Índice 

* [Título e Imagem de capa](#título-e-imagem-de-capa)
* [Badges](#badges)
* [Índice](#índice)
* [Descrição do Projeto](#descrição-do-projeto)
* [Status do Projeto](#status-do-projeto)
* [Docker](#Docker)
* [Forma de contagem](#forma-de-contagem)
* [Funcionalidades e Demonstração da Aplicação](#funcionalidades-e-demonstração-da-aplicação)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Link de vídeo explicativo]()
* [Pessoas Desenvolvedoras do Projeto](#pessoas-desenvolvedoras-do-projeto)

# Descrição do Projeto

O seguinte projeto tem como objetivo contruir App Monitor e Manager que será responsável pelo monitoramento e gerenciamento de containers através de um programa desenvolvido em Python.


# Status do Projeto

O projeto foi desenvolvido diante da proposta de trabalho do professor Fábio Cabrini, como quinto checkoint da disciplina Coding For Security da turma 1TDCG da Faculdade de Adminsitração e Informatica Paulista. Aguardando aprovação do docente responsável.


# App Monitor e Manager

Um App Monitor e Manager é uma única aplicação que oferece funcionalidades para monitorar o desempenho de aplicativos, como uso de recursos, tempos de resposta e erros, ao mesmo tempo em que permite gerenciar a instalação, atualização e remoção de aplicativos em um dispositivo. Essa ferramenta combinada é útil para otimizar o desempenho e a organização dos aplicativos em um sistema, neste caso, monitorando e gerenciando um Docker.


![contagem](https://static.significados.com.br/foto/fibonacci2_bg.jpg)

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2594...

É possível observar que a composição é formada por números que são o resultado da soma dos
dois anteriores:

![contagem](https://user-images.githubusercontent.com/129625591/229652427-790f7379-9e6b-4bd8-ac15-50e6ee4d61eb.png)

# Funcionalidades e Demonstração da Aplicação

* [Explicando e demonstrando "Fibonacci.py"](https://youtu.be/WcaoXCMeOw4)

Para executar o programa, inicie primeiro o interpretador com o comando py ou python3, no windows powershell ou no terminal do seu sistema operacional.

* Clone o repositório no diretório desejado

```
$ git clone https://github.com/44SEC/contador-sequencial-fibonacci.git
```

* Execute o script com o seguinte comando

```
$ python3 fibonacci.py
```

O código vai exibir uma menssegem de boas vindas e em seguida irá solicitar que o usuários insira a quantidade de valores que deseja gerar. A seguinte mensagem será exibida: 

"Insira um número para gerar a sequência de Fibonnaci:"

O número minimo aceito pelo programa é 2, tendo em vista parâmetros solicitados para o desenvolvimento do trabalho. Caso o usuário insira um número menor, uma mensagem de erro será exibida e o programa voltará ou seu ponto inicial.

A aplicação só aceita números inteiros, caso uma string seja inserida o programa exibirá uma mensagem de erro e retornará ao ponto inicial.

Após a inserção, o programa retornará a contagem em forma de lista sem quebra de linha. A quantidade de números dentro da lista corresponde com o número informado pelo usuário. 

AVISO - Para fins de segurança e preservação da capacidade de processamento de computadores convencionais, o máximo de valores gerados está limitado a 5000 valores. Caso um número maior seja inserido, uma mensagem de erro será exibida e o programa retornará ao inicio.

# Tecnologias utilizadas

Para realizar os cálculos e entregar ao usuário a contagem sequêncial, o grupo 44SEC optou por utilizar a liguagem Python, versão 3.11. Para a criação do código, foram utilizadas funções como "input", "list", "for", "while", "try", "except" e "print", dispensando a necessidade do uso de bibliotecas.

# Pessoas Desenvolvedoras do Projeto

Felipe de Resende Madeira  RM: 

Suellen Guedes Rufino  RM:97687


