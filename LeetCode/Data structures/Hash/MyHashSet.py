# https://leetcode.com/explore/learn/card/hash-table/182/practical-applications/1139/
# this is a custom implementation of a hash set that uses separate chaining as collision treatment

class MyHashSet:
    
    def __init__(self):
        self._hash_set = [[]] * 10000

    def add(self, key: int) -> None:
        list_in_index = self._hash_set[self._hash_funct(key)]
        if (key in list_in_index):
            return
        else:
            list_in_index.append(key)


    def remove(self, key: int) -> None:
        list_in_index = self._hash_set[self._hash_funct(key)]
        if(key in list_in_index):
            list_in_index.remove(key)
        else:
            return

    def contains(self, key: int) -> bool:
        list_in_index = self._hash_set[self._hash_funct(key)]
        if(key in list_in_index):
            return True
        else:
            return False
        
    def _hash_funct(self, key) -> int:
        return key % 10000
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)