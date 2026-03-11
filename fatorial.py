import sys
# int somatorio (int n)
# retorna o somatorio de n

# erro: n negativo
# condição de parada: 0 ou 1 retornam 1

def fatorial(n):
  if n == 0 or n == 1:
    return 1

  if n < 0:
    raise Exception('negativo n pode')

  return n * fatorial(n-1)
  
if __name__ == "__main__":
  n = int(sys.argv[1])
  print(fatorial(n))