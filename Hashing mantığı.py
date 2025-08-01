# Basit bir hash tablosu implementasyonu
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Basit hash fonksiyonu: anahtarı tablo boyutuna göre mod alıyoruz
    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value

    def get(self, key):
        index = self.hash_function(key)
        return self.table[index]

# Kullanım
ht = HashTable(10)
ht.insert(123, "Ali")
ht.insert(456, "Zeynep")

print(ht.get(123))   # Çıktı: Ali
print(ht.get(456))   # Çıktı: Zeynep
