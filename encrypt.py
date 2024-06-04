import hashlib as h

class Encrypted:
    
    def sha1(inputan):
        encrypt = h.sha1(inputan.encode()).hexdigest()
        print('Hasil encrypt:', encrypt)

    def sha256(inputan):
        encrypt = h.sha256(inputan.encode()).hexdigest()
        print('Hasil encrypt:', encrypt)

    def sha224(inputan):
        encrypt = h.sha224(inputan.encode()).hexdigest()
        print('Hasil encrypt:', encrypt)
    def md5(inputan):
        encrypt = h.md5(inputan.encode()).hexdigest()
        print('Hasil encrypt (MD5):', encrypt)

    def sha512(inputan):
        encrypt = h.sha512(inputan.encode()).hexdigest()
        print('Hasil encrypt (SHA-512):', encrypt)

    def blake2b(inputan):
        encrypt = h.blake2b(inputan.encode()).hexdigest()
        print('Hasil encrypt (BLAKE2b):', encrypt)


print(""" ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝
                                                              """)
inputan = input('Masukkan yang akan di-encrypt: ')
print("Pilih algoritma enkripsi:")
print("1. SHA-1")
print("2. SHA-256")
print("3. SHA-224")
print("4. MD5")
print("5. SHA-512")
print("6. BLAKE2b")
pilihan = int(input('Masukkan pilihan (1-6): '))

if pilihan == 1:
    Encrypted.sha1(inputan)
elif pilihan == 2:
    Encrypted.sha256(inputan)
elif pilihan == 3:
    Encrypted.sha224(inputan)
elif pilihan == 4:
    Encrypted.md5(inputan)
elif pilihan == 5:
    Encrypted.sha512(inputan)
elif pilihan == 6:
    Encrypted.blake2b(inputan)
else:
    print('Pilihan tidak valid')