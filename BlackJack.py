import random

# Função para criar um baralho ordenado (52 cartas)
def criar_baralho():

      naipes = ['Copas', 'Espadas', 'Paus', 'Ouros']
      valores = ['Ás', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
      baralho = ([(valor, naipe) for naipe in naipes for valor in valores])
      return baralho


# Função para o sortear e remover uma carta aleatória do baralho e retornar
# a carta e quantos pontos ela vale
def sorteio_aleatorio(baralho):
    valores = {'Ás': 1, 'J': 10, 'Q': 10, 'K': 10}
    if len(baralho) > 0:
        carta = random.choice(baralho)
        baralho.remove(carta)
        pontos = valores.get(carta[0], carta[0])
        return carta, pontos
    else:
        return "O baralho está vazio!"


# Função para distribuir cartas iniciais
def distribuir_cartas_iniciais(jogadores, pontuacoes, baralho):
    for jogador in jogadores:
        carta1 = sorteio_aleatorio(baralho)
        carta2 = sorteio_aleatorio(baralho)
        pontuacoes[jogador] += carta1[1] + carta2[1]
        print(f"{jogador} recebeu cartas de valor {carta1[0]} e {carta2[0]}. Pontuação atual: {pontuacoes[jogador]}")


# Função para a jogada
def jogada(jogador, pontuacoes, ativos, baralho):

    # Verifica se o jogador está ativo e se ainda tem menos de 21 pontos
    if ativos[jogador] and pontuacoes[jogador] < 21:
        # Pergunta ao jogador se ele quer comprar uma carta
        resposta = input(f"{jogador}, você quer comprar uma carta? (s/n): ").strip().lower()
        # Só para de receber carta se digitar 'n', qualquer outro caracter ele recebe outra carta
        if resposta != 'n':
            # Recebe a carta aleatória e soma os pontos
            carta = sorteio_aleatorio(baralho)
            pontuacoes[jogador] += carta[1]
            print(f"{jogador} comprou uma carta de valor {carta[0]}. Pontuação atual: {pontuacoes[jogador]}")
            # Verifica se o jogador estourou e imprime a mensagem
            if pontuacoes[jogador] > 21:
                print(f"{jogador} estourou com {pontuacoes[jogador]} pontos.")
                ativos[jogador] = False
        else:
            ativos[jogador] = False
    else:
        print(f"{jogador} não pode mais comprar cartas.")
        ativos[jogador] = False


# Função de verificação dos vencedores
def verificar_vencedores(pontuacoes):
    vencedores = []
    maior_pontuacao = 0
    for jogador, pontuacao in pontuacoes.items():
        # Testa se a pontuação é <= 21 e maior que 0 e define a maior pontuação
        if pontuacao <= 21 and pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
            vencedores = [jogador]
        # Testa se a pontuação é igual a maior pontuação (caso de haver mais de 1 ganhador)
        elif pontuacao == maior_pontuacao:
            vencedores.append(jogador)
    return vencedores

def valida_numero_jogadores(num_jogadores):

        # Verifica se o número de jogadores é um número inteiro e esta dentro dos limites
      try:
        num_jogadores = int(num_jogadores)
        if num_jogadores < 2:
            print("O jogo precisa de pelo menos 2 jogador.")
            return False
        elif num_jogadores > 6:
            print("O jogo não pode ter mais de 6 jogadores.")
            return False
        else:
            return True
      except ValueError:
        print("O número de jogadores deve ser um número inteiro.")
        return False


# Função principal para iniciar o jogo
def blackjack():

    # Mensagem inicial
    print("Bem-vindo ao jogo de Blackjack!\n")
    # Pergunta ao usuário quantos jogadores irão participar
    num_jogadores = input("Digite o número de jogadores: ")
    # Valida o número de jogadores
    while not valida_numero_jogadores(num_jogadores):
        num_jogadores = input("Digite o número de jogadores: ")

    # Cria uma lista vazia para os jogadores
    jogadores = []
    num_jogadores = int(num_jogadores)
    # Com o número de jogadores ele vai perguntar o nome de cada um dos jogadores
    for i in range(num_jogadores):
        nome = input(f"Digite o nome do jogador {i+1}: ")
        jogadores.append(nome)

    # Mensagem de boas vindas e os nomes dos jogadores
    print("\nIniciando o jogo de Blackjack...\n")
    print(f"Os jogadores participantes são: {', '.join(jogadores)}\n")

    # Criação do baralho
    baralho = criar_baralho()
    # Cria um dicionário com os nomes dos jogadores e com a pontuação zerada
    pontuacoes = {jogador: 0 for jogador in jogadores}
    # Cria um dicionário com os nomes dos jogadores e com o valor True (ativos)
    ativos = {jogador: True for jogador in jogadores}
    # Distribui as cartas iniciais (2 cartas para cada jogador)
    distribuir_cartas_iniciais(jogadores, pontuacoes, baralho)

    # Loop principal do jogo
    while True:
        jogadores_ativos = sum(ativos.values())  # Conta quantos jogadores ainda estão ativos
        if jogadores_ativos == 0:  # Se nenhum jogador estiver ativo, sai do loop
            break
        for jogador in jogadores:
            if ativos[jogador]:  # Verifica se o jogador está ativo
                jogada(jogador, pontuacoes, ativos, baralho)

    # Verifica os vencedores ao final do loop while
    vencedores = verificar_vencedores(pontuacoes)
    if vencedores:
        print("O(s) vencedor(es):")
        for vencedor in vencedores:
            print(f"{vencedor} com {pontuacoes[vencedor]} pontos")
    else:
        print("Nenhum jogador ganhou.")

# Iniciar o jogo
blackjack()