import math
e = 2.71828


# definir f(x), para mudar a equação = mudar o return
def f(x): 

    return x**3-x-1

# definir O(x) 
def O(x): 

    return (x+1)**(1/3)

# exemplo:
 
if __name__ == "__main__" :
  
  # O resultado da aproximação será o mais perto de "E"
  E = float(input("E = ").replace(",",".")) 
  # exemplo: 0.001

  # Definir X0
  x = float(input("x0 = ").replace(",","."))
  # Montagem da lista x e fx
  lista_x, lista_fx = [],[]

  # cabeçalho da tabela
  print(f"K ||   x        ||  xk+1 - xk  ||     f(x)    ||")
  print(f"0 || {x:.8f} ||     --      || {f(x):.8f} ||")

  i=0

  # abs() = retorna o valor absoluto
  # equanto a precissão não for alcançada
  while abs(f(x))>E: 
      # executa a função auxiliar
      x=O(x)
      # Adiciona o resultado no fim da lista
      lista_x.append(x)
      #executa a função f(x)
      f(x)
      # Adiciona o resultado no fim da lista
      lista_fx.append(f(x))
      #incrementa i
      i=i+1

# para i de acordo com tamanho da lista
  for i in range(len(lista_x)):
      # Monta a tabela
      if i!=len(lista_x)-1:
          print(f"{i+1} || {lista_x[i]:.8f} || {lista_x[i+1]-lista_x[i]:.8f}  || {lista_fx[i]:.8f} ||") 
      else:
          print(f"{i+1} || {lista_x[i]:.8f} || {lista_x[i]-lista_x[i]:.8f}  || {lista_fx[i]:.8f} ||") 
          
  print(f"\nSolução aproximada = {lista_x[-1]} | (f(x) = {lista_fx[-1]})")
  print()
