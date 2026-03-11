import sys
# int somatorio (int n)
# retorna o somatorio de n
# condição de parada: n == 0 retorna 0

def somatorio(n):
  if n == 0 : return 0

  if n > 0:
    return n + somatorio(n-1)
  
  if n < 0:
    return n + somatorio(n+1)


if __name__ == "__main__":
  n = int(sys.argv[1])
  print(somatorio(n))