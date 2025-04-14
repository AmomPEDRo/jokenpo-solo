import random

def jogar():
    opcoes = ['pedra', 'papel', 'tesoura' ]
    
   
    escolha_usuario = input("Escolha entre Pedra, Papel ou Tesoura: ").lower()
    
    if escolha_usuario not in opcoes:
        print("Opção inválida. Tente novamente.")
        return


    escolha_computador = random.choice(opcoes)
    print(f"Computador escolheu: {escolha_computador}")
        
    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
         (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        print("Você venceu!")
    else:
        print("Você perdeu!")


jogar()
