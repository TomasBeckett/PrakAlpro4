def cek_digit_belakang(a, b, c):
        angka1 = a % 10
        angka2 = b % 10
        angka3 = c % 10

        if angka1 == angka2 or angka1 == angka3 or angka2 == angka3:
            return True
        else:
            return False
        
a = int(input("Angka 1 : "))
b = int(input("Angka 2 : "))
c = int(input("Angka 3 : "))

result = cek_digit_belakang(a, b, c)
print(result)

# print(cek_digit_belakang(30, 20, 18))
# print(cek_digit_belakang(145, 5, 100))
# print(cek_digit_belakang(71, 187, 18))
# print(cek_digit_belakang(1024, 14, 95))
# print(cek_digit_belakang(53, 8900, 658))


