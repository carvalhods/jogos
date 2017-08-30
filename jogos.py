import forca
import adivinhacao

def escolhe_jogo():
    print("*" * 30)
    print("**** Escolha o seu jogo! ****")
    print("*" * 30)

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if jogo == 1:
        forca.jogar()
    elif jogo == 2:
        adivinhacao.jogar()

if __name__ == "__main__":
    escolhe_jogo()