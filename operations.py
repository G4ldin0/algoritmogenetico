import random as r

bits = 3
taxaMutacao = 0.05


#os três primeiros bits do numero se tornam um novo valor
def getLo(n):
   binario = ""
   for i in range(bits):
      binario += '1'
   return n & int(binario, 2)

#os três bits após os três primeiros se tornam um novo valor
def getHi(n):
   return n >> bits


#gera o valor real que será usado na função de avaliação
def real(n, sup, inf):
   numerador = sup - inf
   denominador = pow(2, bits) - 1
   return inf + (numerador / denominador) * n


#função basica que gera uma mascara de bits aleatorios e altera em n
def mutacao(n):
   bit = r.randint(1, bits*2 + 1) - 1

   random = 0 

   mask = ''
   for i in range(bits*2):
      random = r.random()
      if i == bit:
         mask += '1'
      else:
         # mask += '0'
         if random > taxaMutacao/4:
            mask += '0'
         else:
            mask += '1'
      
   print(mask)
   return n ^ int(mask, 2)

#operador de crossover de ponto único simples 
def crossover(pai1, pai2):

   #randomiza a ordem dos novos filhos
   aux1 = 0
   aux2 = 0
   ordem = r.random()
   if(ordem > 0.5):
      aux1 = pai1
      aux2 = pai2
   else:
      aux1 = pai2
      aux2 = pai1

   corte = r.randint(0, bits*2 - 1)
   
   mask = ""
   while len(mask) < bits:
      mask += '1'
   
   valor1 = (( aux1 >> corte ) << corte ) | ( aux2 & int(mask,2))
   valor2 = (( aux2 >> corte ) << corte ) | ( aux1 & int(mask,2))

   #testa a mutação em cada filho
   muta = r.random()
   if muta <= taxaMutacao:
      valor1 = mutacao(valor1)
   
   muta = r.random()
   if muta <= taxaMutacao:
      valor2 = mutacao(valor2)

   return [[valor1,0,0], [valor2,0,0]]
