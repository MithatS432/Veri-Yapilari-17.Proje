# Yerleşik hash fonksiyonunu kullanma
isimler = ["Ahmet", "Mehmet", "Ayşe"]

for isim in isimler:
    print(f"{isim} -> Hash değeri: {hash(isim)}")


import hashlib
#Sabit hash fonksiyonunu kullanma
def sha256_hash(veri):
    return hashlib.sha256(veri.encode()).hexdigest()

# Kullanım
isim = "Mithat"
print(f"{isim} -> SHA-256 Hash: {sha256_hash(isim)}")
