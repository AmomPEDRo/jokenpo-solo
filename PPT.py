
def jogar():
    opcoes = ['pedra', 'papel', 'tesoura']
    

    escolha_jogador1 = input("Jogador 1, escolha entre Pedra, Papel ou Tesoura: ").lower()
    if escolha_jogador1 not in opcoes:
        print("Opção inválida. Tente novamente.")
        return
    

    escolha_jogador2 = input("Jogador 2, escolha entre Pedra, Papel ou Tesoura: ").lower()
    if escolha_jogador2 not in opcoes:
        print("Opção inválida. Tente novamente.")
        return

   
    print(f"Jogador 1 escolheu: {escolha_jogador1}")
    print(f"Jogador 2 escolheu: {escolha_jogador2}")
    
  
    if escolha_jogador1 == escolha_jogador2:
        print("Empate!")
    elif (escolha_jogador1 == 'pedra' and escolha_jogador2 == 'tesoura') or \
         (escolha_jogador1 == 'papel' and escolha_jogador2 == 'pedra') or \
         (escolha_jogador1 == 'tesoura' and escolha_jogador2 == 'papel'):
        print("Jogador 1 venceu!")
    else:
        print("Jogador 2 venceu!")

jogar()
   