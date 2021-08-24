def gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  while a > 0 and b > 0:
    if a >= b:
      a = a % b
    else:
      b = b % a
  return max(a, b)

def extended_gcd(a, b):
  if b == 0:
    d, x, y = a, 1, 0
  else:
    d, p, q = extended_gcd(b, a % b)
    x = q
    y = p - (a // b) * q
  return d, x, y
  
def divide(a, b, n):
  assert n > 1 and a > 0 and gcd(a, n) == 1
  
  d, inv, k = extended_gcd(a, n)
  return (b * inv) % n

if __name__ == "__main__":
    x = divide(3, 5, 7)
    print(x)