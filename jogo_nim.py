def main():
    print ("Bem-vindo ao jogo do NIM! Escolha:")
    escolha = int(input("1 - para jogar uma partida isolada\n" + "2 - para jogar um campeonato "))
    if escolha ==1 :
        print("Voce escolheu partida isolada!");
        partida()
    else :
        print("Voce escolheu um Campeonato!")
        campeonato()
   

def computador_escolhe_jogada (n, m) :
    return n % (m+1)

def usuario_escolhe_jogada (n,m) :
    user = m+1
    while user > m :
        user = int(input("Quantas peças você vai tirar? "))
    return user

def partida() :
    userJoga = False
    retirada = 0
    numero = ["um","dois","três","quatro","cinco","seis","sete","oito","nove","dez"]
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m+1)==0 :
        userJoga = True
        print("Você começa!")
    else:
        print("Computador começa!")

    while n > 0:
        if userJoga:
            retirada = usuario_escolhe_jogada(n,m)
            print("Voce tirou", retirada," peças")
            n-=retirada
            userJoga = False
        else :
            retirada = computador_escolhe_jogada (n,m)
            print ("O computador tirou",retirada," peças")
            n-=retirada
            userJoga = True
        if n > 0 : print("Agora resta apenas", n, " peça no tabuleiro")

    if userJoga and n==0 :
        print("Fim do jogo! O computador ganhou!")
        return 1
    else :
        return 0

def campeonato() :
    placar=[0,0]
    print("**** Rodada 1 ****")
    placar[partida()]+=1
    print("**** Rodada 2 ****")
    placar[partida()]+=1
    print("**** Rodada 3 ****")
    placar[partida()]+=1
    print("Placar Voce:",placar[0]," X",placar[1]," Computador")

main()
