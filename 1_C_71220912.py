a = str(input("Masukkan Kata atau angka : "))
def balikkata (a):
    str = " "
    for i in a:
        str = i + str
    return str 

print (balikkata (a))