# bool palindromo(string str)
# retorna se a string é um palindromo
# erro: quando str for null
# condiçoes de parada: 0 ou 1 retornam True
import sys 

def palindromo(str):
  size = len(str)
  if size == 0 or size == 1: return True

  if str[0] != str[size-1]: return False

  if str[0] == str[size-1]: 
    substr = str[1:-1]
    return palindromo(substr)

if __name__ == "__main__":
  str = str(sys.argv[1])
  print(palindromo(str))