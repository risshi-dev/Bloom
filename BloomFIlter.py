class Bloom:
    def __init__(self, size, numHashes, salt = None):
        self.dataSize = size
        self.noOfHashes = numHashes
        self.salt = salt
        self.bitIndex = [0]*size
        self.database = []
        # using standard offset used by author FNV
        self.FNV_OFFSET_BASIS = 14695981039346656037
        self.FNV_OFFSET_PRIME = 1099511628211
    
    def __encodeHash(self, data: bytes) -> int:
        data = data%self.dataSize
        return data

    def __fnv1_hash (self, data: str) -> int:
        if self.salt is not None:
            data += self.salt
        hashValue = self.FNV_OFFSET_BASIS
        for byte in data.encode('utf-8'):
            hashValue ^= byte
            hashValue *= self.FNV_OFFSET_PRIME
            hashValue &= (2**64) - 1
        hashValue = self.__encodeHash(hashValue)
        return hashValue
    
    def insert(self, data: str):
        for num in range(self.noOfHashes):
            index = self.__fnv1_hash(data)
            self.bitIndex[index] = 1

        self.database.append(data)

    def find(self, lookFor: str) -> bool:
        for num in range(self.noOfHashes):
            index = self.__fnv1_hash(lookFor)
            if self.bitIndex[index] == 0:
                return False
        return True


# Bloom Filter without salt
bloom = Bloom(30, 5)

#Bloom Filter with salt
bloomWithSalt = Bloom(40, 10, "lazy bloom filter")

coffee_types = [
    "Espresso",
    "Americano",
    "Cappuccino",
    "Latte",
    "Mocha",
    "Macchiato",
    "Flat White",
    "Irish Coffee",
    "Turkish Coffee",
    "Vienna Coffee"
]

for coffee in coffee_types:
    bloom.insert(coffee)
    bloomWithSalt.insert(coffee)

#find
print("Is Coffee present? ", bloom.find("Coffee"))
print("Is Macchiato present? ", bloom.find("Macchiato"))
print("")
print("Is Tea present with salt? ", bloomWithSalt.find("Coffee"))
print("Is kurtish coffee present with salt? ", bloomWithSalt.find("kurtish coffee"))
print("Is Macchiato present with salt? ", bloomWithSalt.find("Macchiato"))




