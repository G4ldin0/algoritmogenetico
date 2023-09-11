import numpy as np
import operations as op
import random as r
import grafico as g

#-----------------------------------------------------------------------------------

inferior = 0
superior = 7
tamanhoPopulacao = 100
parada = 5000

geracao = 0

#-----------------------------------------------------------------------------------

#função usada para teste
#x e y estando no intevalo [0,7]
def f(x, y):
   xi = op.real(x, superior, inferior)
   yi = op.real(y, superior, inferior)
   return np.sqrt(pow(xi, 3) + 2 * pow(yi, 4))


#-----------------------------------------------------------------------------------




#lista com a população: [representação numerica dos 6 bits, valor de retorno de f(x,y), parte da roleta]
populacao = []


#preenchimento da população com valores aleatorios
while len(populacao) < tamanhoPopulacao:
   populacao.append([r.randint(0, pow(2, op.bits) -1), 0, 0])




#loop do algoritmo genético
while geracao != parada:

   print('\ngeracao ' + str(geracao))

   totalAvaliacao = 0
   melhorCaso = 0

   #avalia cada cromossomo
   debug = ""
   for i in populacao:
      i[1] = ( f( op.getLo( i[ 0 ] ), op.getHi( i[ 0 ] ) ) + 0)

      totalAvaliacao += i[1]

      if populacao[melhorCaso][1] < i[1]:
         melhorCaso = populacao.index(i)

      debug += str(i[0]) + ' '
   print(debug)

   g.plotPoints.append(populacao[melhorCaso][0])

   #preenche o ultimo campo com a porcentagem da roleta
   for i in populacao:
      i[2] = ( i[1] / totalAvaliacao) * 360

   print('melhor caso: ' + str(populacao[melhorCaso]))
   print(str(totalAvaliacao) + '\n')


   #escolhe o primeiro pai
   i = 0
   aux = populacao[i][2]
   aleatorio = r.random() * 360
   #print('\n\n' + str(aleatorio))
   while (aux < aleatorio) & (i < tamanhoPopulacao):
      #print(aux)
      i+=1
      aux += populacao[i][2]

   print("selecionado = " + str(populacao[i][0]))


   #escolhe o segundo pai
   j = 0
   aux = populacao[j][2]
   aleatorio = r.random() * 360
   #print('\n' + str(aleatorio))
   while (aux < aleatorio) & (j < tamanhoPopulacao):
      #print(aux)
      j+=1
      aux += populacao[j][2]

   print("selecionado = " + str(populacao[j][0]))


   placeholder = op.crossover(populacao[i][0], populacao[j][0])

   print("filhos = " + str(placeholder[0][0]) + " & " + str(placeholder[1][0]))

   #substituição dos pais pelos filhos
   populacao[i] = placeholder[0]
   populacao[j] = placeholder[1]


   geracao += 1

g.gerarGrafico()
