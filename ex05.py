import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('''
      O valor {}.
      O dobro  {} vale {}.
      O triplo {} vale {}.
      a raiz   {} vale {:.2f}.
      '''
      .format(
          num, num, num*num, num, num*3, num, raiz
      ))