import numpy as np

def lagrange(n, x, y):
  # definição do ponto de interpolação
  xp = float(input('Defina o ponto de interpolação: '))

  # Inicialmene o valor interpolado começa em 0
  yp = 0

  # Interpolação por Lagrange
  for i in range(n):
      p = 1
  
      for j in range(n):
          if i != j:
            # Equação de lagrange
            p = p * (xp - x[j])/(x[i] - x[j])   
  
      # Valor de yp na função interpoladora no ponto p
          
      yp = yp + p * y[i]

       
  print("O valor interpolado em", xp, "é: ")
  return yp

if __name__ == "__main__" :
  n = int(input('Digite q quatidade de pontos: '))

  # Fazendo array  e inicializando com zero para armazenar os valores de x e y
  x = np.zeros((n))
  y = np.zeros((n))


  #Leitura dos dados
  print('Enter data for x and y: ')
  for i in range(n):
      x[i] = float(input( 'x['+str(i)+']='))
      y[i] = float(input( 'y['+str(i)+']='))

  #chamada da função
  print(lagrange(n, x, y))
  
