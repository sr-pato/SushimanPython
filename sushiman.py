def test_primo(n):
   n = int(n)
   if n <= 1:
      return False
   else:
      for i in range(2, n):
         if n % i == 0:
            return False
   return True


def primos(inicio, saida):
    numbers = list(range(inicio, saida))
    primos = [x for x in numbers if test_primo(x)]
    return primos


def all_numbers(algarimos):
    start = int('1'+'0'*(algarimos-1))
    end = int('9'*algarimos)
    return start, end


def test_super_primos(primos):
    super_primos = list()
    for p in primos:
        p2 = str(p)
        boolsss = set()
        while len(p2) != 1:
          p2 = p2[:-1].strip()
          if test_primo(p2):
            boolsss.add(True)
          else:
            boolsss.add(False)
        if len(boolsss) == 1 and True in boolsss:
          super_primos.append(p)
    return super_primos

def main():
    algarismos = int(input("Quantidade de algarismos: "))
    escala = all_numbers(algarismos)
    n_primos = primos(escala[0], escala[1])
    super_primos = test_super_primos(n_primos)
    print(super_primos)

main()            