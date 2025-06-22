import random

print("=" * 40)
print("-" * 10 + " Mines " + "-" * 10)
print("-" * 5 + " Regras do jogo " + "-" * 5)
print("-" * 3 + "Acerte o máximo de diamantes que conseguir sem escolher as bombas!" + "-" * 3)

nome = input("Insira seu nome para jogar: ")
print(f"\nSeja bem-vindo, {nome}!\n")

tamanho = 4
total_celulas = tamanho * tamanho
base_aposta = 10.00  # valor fixo

# Validação da quantidade de bombas
while True:
    try:
        qtdBombas = int(input("Escolha o número de bombas (mín 1, máx 15): "))
        if 1 <= qtdBombas < total_celulas:
            break
        else:
            print("Escolha inválida. Número deve ser entre 1 e 15.")
    except ValueError:
        print("Digite um número válido.")

def matrizBomba():
    bombas = random.sample(range(total_celulas), qtdBombas)
    matrizReal = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            index = i * tamanho + j
            if index in bombas:
                linha.append('💣')
            else:
                linha.append('💎')
        matrizReal.append(linha)
    matrizVisivel = [['⬜' for _ in range(tamanho)] for _ in range(tamanho)]
    return matrizReal, matrizVisivel

def mostrarMatriz(matriz):
    print("\n    1   2   3   4")
    letras = ['A', 'B', 'C', 'D']
    for i, linha in enumerate(matriz):
        print(f' {letras[i]} ', end=' ')
        for celula in linha:
            print(celula, end='  ')
        print()
    print()

def revelarJogada(linha, coluna, matrizReal, matrizVisivel):
    if matrizVisivel[linha][coluna] != '⬜':
        return False, "❗ Já revelada!"
    valor = matrizReal[linha][coluna]
    matrizVisivel[linha][coluna] = valor
    if valor == '💣':
        return False, '💥 Você pisou numa bomba!'
    return True, '✅ Seguro!'

def salvar_ranking(nome, valor, status):
    with open("ranking.txt", "a", encoding="utf-8") as f:
        f.write(f"{nome} | R$ {valor:.2f} | {status}\n")

# Inicializa o jogo
matrizReal, matrizVisivel = matrizBomba()
letras = ['A', 'B', 'C', 'D']
pontuacao = 0
multiplicador = 1.0
diamantes_totais = total_celulas - qtdBombas

while True:
    mostrarMatriz(matrizVisivel)
    print(f"💰 Multiplicador atual: x{multiplicador:.2f}")
    print(f"💎 Diamantes coletados: {pontuacao} / {diamantes_totais}")
    print(f"🏆 Valor possível de saque: R$ {base_aposta * multiplicador:.2f}")

    jogada = input("Escolha uma célula (ex: A1): ").strip().upper()

    if len(jogada) != 2 or jogada[0] not in letras or not jogada[1].isdigit():
        print("❌ Jogada inválida! Use o formato A1, B3, etc.")
        continue

    linha = letras.index(jogada[0])
    coluna = int(jogada[1]) - 1

    if not (0 <= linha < tamanho and 0 <= coluna < tamanho):
        print("❌ Posição fora do tabuleiro.")
        continue

    sucesso, msg = revelarJogada(linha, coluna, matrizReal, matrizVisivel)
    print(msg)

    if not sucesso:
        mostrarMatriz(matrizReal)
        print(f"\n☠️ Fim de jogo, {nome}! Você perdeu a aposta de R$ {base_aposta:.2f}")
        salvar_ranking(nome, 0.00, "💥 PERDEU")
        break
    else:
        pontuacao += 1
        multiplicador += 0.2

        if pontuacao == diamantes_totais:
            mostrarMatriz(matrizReal)
            ganho = base_aposta * multiplicador
            print(f"\n🎉 Parabéns, {nome}! Você venceu pegando todos os diamantes!")
            print(f"🏆 Valor total ganho: R$ {ganho:.2f}")
            salvar_ranking(nome, ganho, "🎉 VENCEU")
            break

        # Pergunta se o jogador quer continuar
        decisao = input("Deseja continuar jogando? (s = sim / n = sacar): ").strip().lower()
        if decisao == 'n':
            ganho = base_aposta * multiplicador
            mostrarMatriz(matrizVisivel)
            print(f"\n✅ Você decidiu sacar! Parabéns, {nome}!")
            print(f"💰 Valor sacado: R$ {ganho:.2f}")
            salvar_ranking(nome, ganho, "✅ SACOU")
            break
