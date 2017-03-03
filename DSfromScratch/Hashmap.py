# Simple Hashtable implementation
class Hashmap:
    
    def __init__(self):
        self.hashmap = [ [] for i in range(256) ]  #256*[]
        # [ [][][][][]...] - This is how it will look like

    def insert(self, key, value):
        # Mapping the keyto the hashmap range
        hash_key = hash(key) % len(self.hashmap)
        key_exists= False
        # List of list index value
        bucket = self.hashmap[hash_key]
        """Iterating through all the keys in the storage index, 
            To check it key already exists"""
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        #If exists, replace the key,Value
        if key_exists: 
            bucket[i] = ((key, value))
        #If not, add to the existing storage index
        else: 
            bucket.append((key, value))
                

    def retrieve(self , key):
        hash_key = hash(key) % len(self.hashmap)
        bucket = self.hashmap[hash_key]        
        for i, kv in enumerate(bucket):
            k,v = kv
            return v
        raise KeyError

if __name__ =="__main__":
    hm = Hashmap()
    hm.insert("22", "val1")
    hm.insert("111", "val2")
    hm.insert("22", "val22")    
    print hm.retrieve("111")    
    print hm.hashmap