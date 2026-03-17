# int somatorioInt (int j, int k)
# retorna o somatório dos valores entre j e k
# condiçao de parada:  j==k

import sys

def somatorioInt (j, k):
  if j == k: return j

  if j > k:
    return j + somatorioInt(j-1, k)
  
  if k > j:
    return k + somatorioInt(j, k-1)

if __name__ == "__main__":
  j = int(sys.argv[1])
  k = int(sys.argv[1])
  print(somatorioInt(4, 8))