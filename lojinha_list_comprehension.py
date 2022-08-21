# Usando list comprehension criar um sistema que soma um carrinho de compras
# Apenas com intuito de aprendizado

mouses, teclados, fones = 0, 0, 0
carrinho = []
print(f'############ LOJINHA DO SEU PYTHON ############')
operacao = True

while operacao:
    print(f'\nEscolha o produto desejado utilizando os números correspondentes, caso deseje encerrar'
          f'digite um número qualquer! ')
    print(f'1 - Mouse(R$50,00) ###'
          f' 2 - Teclado(R$100,00) ###'
          f' 3 - Fone(R$150,00)')
    escolha = input()
    if escolha.isdigit():
        escolha = int(escolha)
        if escolha == 1:
            carrinho.append(("Mouse", 50))
            mouses += 1
        elif escolha == 2:
            carrinho.append(("Teclado", 100))
            teclados += 1
        elif escolha == 3:
            carrinho.append(("Fone", 150))
            fones += 1
        else:
            operacao = False
    else:
        print(f'Parabéns você tentou zoar o sistema, bye.')
        break
    print(f'\nCarrinho até o momento: '
          f'\n{mouses}x Mouses\n'
          f'{teclados}x Teclados\n'
          f'{fones}x Fones'
          f'')

compras = sum([float(y) for x, y in carrinho])

print(f'######################################'
      f'\nVocê comprou:\n'
      f'{mouses}x Mouses\n'
      f'{teclados}x Teclados\n'
      f'{fones}x Fones\n'
      f'')
print(f'Total das suas compras:R${compras:.2f}')