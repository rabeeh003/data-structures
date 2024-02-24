
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
class Hash_tab:
    def __init__(self, size):
        self.size = size
        self.data = [[] for _ in range(size)]
    
    def _hash(self, key):
        return sum(ord(char) for char in key ) % self.size
    
    def add(self, key, value):
        stno = self._hash(key)
        return self.data[stno].append((key,value))

    def get(self,key):
        h_value = self._hash(key)
        for i in self.data[h_value]:
            if i[0] == key:
                return i[1]
        return None
    
bb = Hash_tab(10)
bb.add("rabi", 12345)
pp = bb.get("rabi")
print(pp)       
        
        
  