#queue
class queue:
    
    def __init__(self):
        self.items=[]        

    def enqueue(self, item):
        self.items.append(item)
    
    def enqueue(self):
        if (not self.isEmpty()):  
            self.items = self.items[1:]            

    def isEmpty(self):
        return len(self.items)==0
        #return self.items == []
    
    def __str__(self):
        return " ".join(str(self.items))
    
if __name__ == "__main__":
    q = queue()
    q.push(2)
    q.push(3)
    q.push(4)
    q.pop()
    q.pop()
    print q
    

    
    