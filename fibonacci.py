import sys
# int fibonacci (int n)
# retorna o n-ésimo número da sequência de fibonacci
# erro: Ns iguais ou menores a 0
# condições de parada: 1 e 2 retornam 1


def fibonacci(n):
  if n <= 0: raise Exception('Número inexistente na sequência de Fibonacci')
  if n==1 or n==2: return 1

  return fibonacci (n-1) + fibonacci (n-2)

if __name__ == "__main__":
  n = int(sys.argv[1])
  print(fibonacci(n))