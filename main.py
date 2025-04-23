import time
import random

print("="*40)
print(" "*10 + "Mines" + " "*10)
print(" "*5 + "Regras do jogo:" + " "*5)
print(" "*3 + "Acerte o máximo de diamantes que conseguir sem escolher as bombas!" + " "*3)

nome = input("Insira seu nome para jogar: ")
print(f"Seja bem-vindo {nome}!")

qtdBombas = input("Escolha o número de bombas (quanto maior o número de bombas, maior sua pontuação): ")

def gerarFiguras(qtdBombas: int, tamanhoTabuleiro: int):
    escolhaCerta = ['💎']

    if qtdBombas >= tamanhoTabuleiro - 1:
        raise ValueError("Número de bombas não pode preencher o tabuleiro inteiro")



tamanho = 4

def matrizBomba():
    totalCelulas = tamanho * tamanho
    bombas = random.sample(range(totalCelulas), qtdBombas)

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
    print(" 1   2   3   4")
    letras = ['A', 'B', 'C', 'D']
    for i, linha in enumerate(matriz):
        print(f'{letras[i]}', end='')
        for celula in linha:
            print(celula, end=' ')
        print()

def revelarJoagada(linha, coluna, matrizReal, matrizVisivel):
    if matrizVisivel[linha][coluna] != '⬜':
        return False, "Já revelada"

    valor = matrizReal[linha][coluna]
    matrizVisivel[linha][coluna] = valor
    if valor == '💣':
        return False, '💥 Você pisou numa bomba!'
    return True, '✅ Seguro!'
    




