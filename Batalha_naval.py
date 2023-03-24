import random

jogador = []
computador = []
computadorEscondido = []
# aqui eu crio as matrizes
for x in range(5):
    jogador.append(["O"] * 10)
for y in range(5):
    computador.append(["O"] * 10)
for z in range(5):
    computadorEscondido.append(["O"] * 10)


# Nessa função eu arrumo a matriz para parecer um tabuleiro de batalha naval
def Tabuleiro(jogador):  # E imprimo a matriz, e uso o metodo join para unir os elemntos das listas, tirar as virgulas
    print("     BATALHA NAVAL")
    print('  0 1 2 3 4 5 6 7 8 9')
    l = 0
    for linha in jogador:
        print("%d|%s|" % (l, " ".join(linha)))
        l += 1


# Aqui eu peço para o jogador posicionar seus barcos.
def NavioJogador():
    print(f"Posicione seus 5 barcos.")
    for i in range(5):
        linhajogador = int(input("Escolha a linha: "))

        while linhajogador not in (0, 1, 2, 3, 4):  # Caso ele tente posicionar em um local que não existe
            print("Valor Invalido!")  # Eu faço ele digitar de novo, mas caso ele tente colocar um barco no mesmo lugar
            linhajogador = int(input("Escolha a linha: "))  # ele consegue, pq caso ele faça isso ele que vai sair perdendo

        colunajogador = int(input("Escolha a coluna: "))

        while colunajogador not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
            print("Valor Invalido!")
            colunajogador = int(input("Escolha a coluna: "))

        jogador[linhajogador][colunajogador] = '\33[7;49;34mN\033[m'  # AZUL
        return int(linhajogador), int(colunajogador)


def NavioComputador(computador):
    for j in range(5):  # Aqui eu faço o computador colocar seus navios, e faço de uma maneira que ele não consiga
        linha = int(random.randint(0, 4))  # Colocar mais de um Navio no mesmo lugar.
        coluna = int(random.randint(0, 9))
        while computador[linha][coluna] == '\33[7;49;34mN\033[m':  # AZUL
            linha = int(random.randint(0, 4))
            coluna = int(random.randint(0, 9))
        computador[linha][coluna] = '\33[7;49;34mN\033[m'  # AZUL
        return int(linha), int(coluna)


def Atirar():  # Aqui eu peço para o player atirar, mas caso ele peça um valor que não existe
    linhaatirar = int(input("Linha: "))  # Ele tem que digitar de novo
    while linhaatirar not in (0, 1, 2, 3, 4):
        print("Valor Invalido!")
        linhaatirar = int(input("Linha: "))
    colunaatirar = int(input("Coluna: "))
    while colunaatirar not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9):
        print("Valor Invalido!")
        colunaatirar = int(input("Coluna: "))
    return int(linhaatirar), int(colunaatirar)


def AtirarComputador():
    linhaC = int(random.randint(0, 4))  # Aqui eu faço o computador atirar randomicamente
    colunaC = int(
        random.randint(0, 9))  # Caso ele tente acertar um local que ele ja acertou, eu fiz ele escolher outro número
    while jogador[linhaC][colunaC] == '\33[7;49;32mX\033[m' or jogador[linhaC][colunaC] == '\33[7;49;31mO\033[m':  # VERDE
        linhaC = int(random.randint(0, 4))
        colunaC = int(random.randint(0, 9))
    return linhaC, colunaC


Tabuleiro(jogador)
navios = 5
while navios != 0:  # Aqui o jogador e o PC colocam seus navios
    linhajogador, colunajogador = NavioJogador()
    NavioComputador(computador)
    Tabuleiro(jogador)
    navios -= 1

print('           VAMOS JOGAR!!!')
print('Tente acertar o navio do computador.')
c = 0
c1 = 0
n = 5
n1 = 5
while True:  # Aqui eu inicio o jogo
    print("         VOCÊ")
    Tabuleiro(jogador)
    print("         PC")
    Tabuleiro(computadorEscondido)
    print("      PlACAR")
    print(f"Você:{c} PC:{c1}")
    print(f"Seus Navios:{n1} PC Navios:{n}")
    linhaatirar, colunaatirar = Atirar()
    if computadorEscondido[linhaatirar][colunaatirar] == '\33[7;49;31mO\033[m':  # VERMELHO
        print("-" * 30)
        print("Você ja atirou ai!")
        print("-" * 30)
    else:
        if computadorEscondido[linhaatirar][colunaatirar] == '\33[7;49;32mX\033[m':  # VERDE
            print("-" * 30)
            print("Você ja derrubou esse Navio!")
            print("-" * 30)
        else:
            if computador[linhaatirar][colunaatirar] == '\33[7;49;34mN\033[m':  # AZUL
                print("-" * 30)
                print("Parabens você Derrubou um Navio!")
                print("-" * 30)
                computadorEscondido[linhaatirar][colunaatirar] = '\33[7;49;32mX\033[m'  # VERDE
                c += 1
                n -= 1
            else:
                print("-" * 30)
                print("Você Errou!")
                print("-" * 30)
                computadorEscondido[linhaatirar][colunaatirar] = '\33[7;49;31mO\033[m'  # VERMELHO
    if c == 5:
        print("-" * 30)
        print('Parabéns você destruiu todos os navios inimigos!')
        print("-" * 30)
        break
    print("É a vez do computador.")
    linhaC, colunaC = AtirarComputador()
    if jogador[linhaC][colunaC] == '\33[7;49;34mN\033[m':  # AZUL
        print(f"O PC atirou na linha {linhaC} e coluna {colunaC}.")
        print("O computador acertou o seu navio.")
        print("-" * 30)
        jogador[linhaC][colunaC] = '\33[7;49;32mX\033[m'  # VERDE
        c1 += 1
        n1 -= 1
    else:
        print(f"O PC atirou na linha {linhaC} e coluna {colunaC}.")
        print("O computador errou.")
        print("-" * 30)
        jogador[linhaC][colunaC] = '\33[7;49;31mO\033[m'  # VERMELHO
    if c1 == 5:
        print("-" * 30)
        print("Que pena você Perdeu!!!")
        print("-" * 30)
print("-" * 40)
print("       Obrigado por Jogar        ")
print("-" * 40)