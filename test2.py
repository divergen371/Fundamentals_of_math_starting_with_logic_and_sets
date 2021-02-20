from sage.all import *
for p in primes(10 ** 20, 10 ** 20 + 1000):
    R = PolynomialRing( GF(p), names='x')
    X = R.gens()[0]

    if not (X ** 4 - 2).is_irreducible():
        print("..reducible polynom mod %s :: X ^ 4 - 2 = %s -> next prime..."
              % (p, factor(X ** 4 - 2)))
        continue

    print("%s is OK" % p)
    break