def cek_angka(a, b, c):
    if (a != b and a != c and b != c) and ((a + b == c) or (a + c == b) or (b + c == a)):
        return True
    else:
        return False

print(cek_angka(9, 5, 4))
print(cek_angka(3, 5, 2))
print(cek_angka(2, 4, 2))
print(cek_angka(4, 7, 11))
print(cek_angka(2, 5, 4))
