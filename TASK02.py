# Проверяет истинность утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X=int(input('Ввведите Х (0 или 1): '))
Y=int(input('Ввведите Y (0 или 1): '))
Z=int(input('Ввведите Z (0 или 1): '))

print((not(X or Y or Z)==(not X and not Y and not Z)))
