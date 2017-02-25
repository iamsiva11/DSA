#doublylinkedlist
class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.size  = 0
        self.last  = None
        self.first = None
        
    def addFirst(self, data):
        if(self.size==0):
            self.first = Node(data, None, None)
            self.last = self.first
        elif self.size>0:
            # create a new node pointing to self.first
            node = Node(data, None, self.first)
            self.first.prev=node
            self.first=node
        self.size+=1
        
    def __str__(self):
        self.current=self.first
        dll_str=""
        while self.current:
            dll_str += "<->"+(str(self.current.data))
            self.current=self.current.next
        return dll_str    

    def add_last(self, data): 
        if(self.size > 0):                
                self.last.next = Node(data, self.last, None)
                self.last = self.last.next
                self.size += 1
        else:
            print "List is empty"
        
            
    def traverse_backwards(self):
        self.current=self.last
        elements=[]
        while(self.last):
            elements.append(self.last.data)
            self.last = self.last.prev
        return elements   
            
        
if __name__=="__main__":
    dll = DoublyLinkedList()
    dll.addFirst(1)
    dll.addFirst(2)
    dll.addFirst(33)
    dll.add_last(44)
    dll.add_last(4)
    print dll
    print dll.traverse_backwards()