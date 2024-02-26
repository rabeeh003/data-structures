
# class HashTable:
#   def __init__(self, size):
#     self.size = size
#     self.data = [[] for _ in range(size)]  # Initialize an empty array of lists

#   def _hash(self, key):
#     # Simple hash function for demonstration (can be improved)
#     return sum(ord(char) for char in key) % self.size

#   def put(self, key, value):
#     hash_index = self._hash(key)
#     self.data[hash_index].append((key, value))  # Add key-value pair to the bucket

#   def get(self, key):
#     hash_index = self._hash(key)
#     for item in self.data[hash_index]:
#       if item[0] == key:  # Check if key matches
#         return item[1]  # Return the value
#     return None  # Key not found

# # Example usage
# phonebook = HashTable(10)  # Create a hash table with 10 buckets
# phonebook.put("Alice", 12345678)
# phonebook.put("Bob", 98765432)
# print(phonebook.get("Alice"))  # Output: 12345678



# hash
# class Hash_tab:
#     def __init__(self, size):
#         self.size = size
#         self.data = [[] for _ in range(size)]
    
#     def _hash(self, key):
#         return sum(ord(char) for char in key ) % self.size
    
#     def add(self, key, value):
#         stno = self._hash(key)
#         return self.data[stno].append((key,value))

#     def get(self,key):
#         h_value = self._hash(key)
#         for i in self.data[h_value]:
#             if i[0] == key:
#                 return i[1]
#         return None
    
# bb = Hash_tab(10)
# bb.add("rabi", 12345)
# pp = bb.get("rabi")
# print(pp)       
        
        
# # hash table other example
# class HashTable:
    
#     def __init__(self, size):
#         self.size = size
#         self.data = [[] for _ in range(size)]
#     def _hash(self,key):
#         return sum(ord(char) for char in key) % self.size
#     def add(self,key,value):
#         ind = self._hash(key)
#         self.data[ind].append((key,value))
#     def get(self,key):
#         ind = self._hash(key)
#         for it in self.data[ind]:
#             if it[0] == key:
#                 return it[1]
#         return None

# ht = HashTable(5)
# ht.add("Rabeeh","muhammed rabeeh pk")
# print(ht.get("Rabeeh"))



# hash ex
# class hashTable:
#     def __init__(self, length):
#         self.size = length
#         self.data = [[] for _ in range(length)]
    
#     def _hash(self,key):
#         return sum(ord(chat) for chat in key) % self.size
    
#     def add(self,key,value):
#         ind = self._hash(key)
#         self.data[ind].append((key,value))
    
#     def get(self, key):
#         ind = self._hash(key)
#         for i in self.data[ind]:
#             if i[0] == key:
#                 return i[1]
#         return None
# h = hashTable(10)
# h.add("rabeeh","12345")
# print(h.get("rabeeh"))




class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [[] for _ in range(size)]
    def _hash(self, key):
        return sum(ord(char) for char in key) % self.size
    def add(self, key, value):
        ind = self._hash(key)
        self.data[ind].append((key,value))
    def get(self, key):
        ind = self._hash(key)
        for i in self.data[ind]:
            if i[0] == key:
                return i[1]
        return None
    
h = HashTable(10)
h.add("rabeeh","1223344556")
h.add("shamil","0998877665")
print(h.get("shamil"))