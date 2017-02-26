# Simple Hashtable implementation
class Hashmap:
    
    def __init__(self):
        self.hashmap = [ [] for i in range(256) ]  #256*[]

    def insert(self, key, value):
        hash_key = hash(key) % len(self.hashmap)
        key_exists= False
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
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