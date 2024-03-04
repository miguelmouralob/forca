import random

# Lista de palavras para o jogo
palavras = ["quiz", "python", "java", "jogo", "programacao",
            "rede", "codigo", "bug", "servidor", "internet",
            "computador", "monitor", "teclado", "mouse", "carregador"]

# Escolha uma palavra aleatória da lista
palavra_aleatoria = random.choice(palavras)

# Inicialize as variáveis
palavra_secreta = list(palavra_aleatoria)
letras_corretas = ["_"] * len(palavra_secreta)
tentativas = 5

# Loop principal do jogo
while True:
    # Imprima a palavra oculta
    print(" ".join(letras_corretas))

    # Peça ao jogador para adivinhar uma letra
    letra = input("Adivinhe uma letra: ").lower()

    # Verifique se a letra está na palavra
    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_corretas[i] = letra
    else:
        tentativas -= 1
        print(f"Letra '{letra}' não está na palavra. Você tem {tentativas} tentativas restantes.")

    # Verifique se o jogador ganhou ou perdeu
    if "".join(letras_corretas) == palavra_aleatoria:
        print("Parabéns, você venceu! A palavra era:", palavra_aleatoria)
        break
    if tentativas == 0:
        print("Você perdeu. A palavra era:", palavra_aleatoria)
        break
