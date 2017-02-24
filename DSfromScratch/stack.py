class stack:

    def __init__(self):
        self.items=[]
    
    def __str__(self):
        return " ".join(str(self.items))
    
    def __len__(self):
        return len(self.items)
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        #return self.items[len(self.items)-1]
        return self.items.pop()
    
    def isEmpty(self):
        return (len(self.items)==0)

    def peek(self):
        return self.items[-1]
    
        
if __name__ == "__main__":
    s = stack()
    s.push(1)
    print s
    s.push("s")
    s.push("e")
    s.push("d")
    s.pop()
    print s
    