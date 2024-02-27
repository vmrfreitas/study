# https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1140/
# this is a custom implementation of a hash map that uses separate chaining as collision treatment

class MyHashMap:
    
    def __init__(self):
        self._hash_map = [[]] * 10000

    def put(self, key: int, value: int) -> None:
        list_in_index = self._hash_map[self._hash_funct(key)]
        found = False
        for pair in list_in_index:
            if (pair[0] == key):
                found = True
                pair[1] = value
        if (not found):
            list_in_index.append([key, value])


    def remove(self, key: int) -> None:
        list_in_index = self._hash_map[self._hash_funct(key)]
        found = False
        for pair in list_in_index:
            if (pair[0] == key):
                found = True
                value = pair[1]
        if (found):
            list_in_index.remove([key, value])

    def get(self, key: int) -> int:
        list_in_index = self._hash_map[self._hash_funct(key)]
        for pair in list_in_index:
            if (pair[0] == key):
                return pair[1]
        return -1
        
    def _hash_funct(self, key) -> int:
        return key % 10000
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)