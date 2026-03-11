import sys

def fibonacci(n):
  if n <= 0: raise Exception('Número inexistente na sequência de Fibonacci')
  if n==1 or n==2: return 1

  return fibonacci (n-1) + fibonacci (n-2)

if __name__ == "__main__":
  n = int(sys.argv[1])
  print(fibonacci(n))