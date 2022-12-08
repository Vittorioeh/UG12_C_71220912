angka = str(input("Masukkan angka :"))
sum = str(input("Masukkan angka yg dihitung :"))
def hitung():
    str = " "
    for sum in angka:
        str = angka.count(sum)
    return str 

print("Angka" , sum , "muncul sebanyak" , hitung (), "kali")