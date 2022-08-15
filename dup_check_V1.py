l1 = [1, 2, 8, 3, 2, 10, 11, 10, 3, 1]
igual, diferente, conta_iguais, x, menor_caractere, menor_contagem = 0, 0, 0, 0, 0, 99999999

for a in l1:
   x = 0
   igual = 0
   for b in l1:
      if a == b:
         igual += 1

      if igual < 2:
         x += 1
      elif igual == 2:
         if x < menor_contagem:
            menor_contagem = x
            menor_caractere = a


print(f'O primeiro número duplicado é: {menor_caractere}')
