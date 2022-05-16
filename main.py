import numpy as np
import math

# Zadanie 1
# Utwórz dwie macierze 1x3 różnych wartości a następnie wykonaj operację mnożenia.

a = np.arange(3)
b = np.arange(3).reshape((3, 1))
c = 4*a

print(c)

# Zadanie 2
# Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu.

trzy = np.random.rand(3,3)
counter = 1
print(trzy)
print(" ")
d = np.amin(trzy, axis=0)
for i in trzy:
    d = np.amin(trzy, axis=0)
    print(f"najmniejszym elementem wiersza {counter} jest {min(i)}")

for d in d:
    print(f"najmniejszym elementem kolumny {counter} jest {d}")

print(" ")
cztery = np.random.rand(4,4)
counter = 1
print(cztery)
print(" ")

f = np.amin(cztery, axis=0)
for i in cztery:
    d = np.amin(trzy, axis=0)
    print(f"najmniejszym elementem wiersza {counter} jest {min(i)}")

print(" ")
for i in f:
    print(f"najmniejszym elementem kolumny {counter} jest {d}")
    counter += 1

# Zadanie 3
# Wykorzystaj macierze z zadania pierwszego i wykonaj iloczyn macierzy

print(np.dot(a, b))

# Zadanie 4
# Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite, a druga
# liczby rzeczywiste. Następnie wykonaj na nich operację mnożenia.

a = np.linspace(1, 3, num=3, dtype="int32")
b = np.linspace(0.5, 1.2 , num=3)
print(b)
print(np.dot(a, b))

# Zadanie 5
# Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z jej wartości i
# zapisz do zmiennej “a”.

g = np.random.rand(2,3)
h = []
print(g)
for i in g.flat:
    h.append(math.sin(i))
a = np.array(h).reshape((2, 3))
print(a)

# Zadanie 6
# Utwórz nową macierz 2x3 różnych wartości a następnie wylicz cosinus dla każdej z jej
# wartości i zapisz do zmiennej “b”.

g = np.random.rand(2,3)
h = []
print(g)
for i in g.flat:
    h.append(math.cos(i))
b = np.array(h).reshape((2, 3))
print(b)

# Zadanie 7
# Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.

print(a+b)
print("")

# Zadanie 8
# Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.

[print(a) for a in np.random.rand(3, 3)]

# Zadanie 9
# Wygeneruj macierz 3x3 i wyświetl w pętli każdy element korzystając z opcji “spłaszczenia”
# macierzy. (użyj funkcji flat())

[print(a) for a in np.random.rand(3, 3).flat]

# Zadanie 10
# Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego?
#odpowiedz: macierz 9x9 posiada 81 elementow, ksztalt mozemy zmienic tylko na taki ze iloczyn ilosci kolumn i ilosci wierszy
# utworzy liczbę 81

v = np.arange(81).reshape((9, 9))
print(v)
print(v.reshape(27, 3))

# Zadanie 11
# Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4. Wygeneruj w ten sposób
# jeszcze kombinacje 4x3 i 2x6. Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?

t = np.arange(12)
print(t)
t = t.reshape(3, 4)
print(t)
print([a for a in t.flat])
f = np.arange(12).reshape((4, 3))
print(f)
print([a for a in f.flat])
jh = np.arange(12).reshape((2, 6))
print(jh)
print([a for a in jh.flat])











