class Node:
    
    def __init__(self, data):
        self.data=data
        self.next=None
                
class LinkedList:
    
        def __init__(self):
            self.head = None
        
        def add(self, data):
            node = Node(data)
            if  self.head==None:
                self.head=node
            else:
                node.next=self.head
                self.head=node
          
        def __str__(self):
            s = ""
            p = self.head
            while(p.next != None):
                s+=p.data
                p=p.next
            s+= p.data
            return s
                       
        def delete(self, data):
            current = self.head
            prev = None
            while current:
                if current.data == data:
                    if current == self.head:
                        self.head = current.next
                    else:
                        prev.next = current.next
                    return current
                prev = current
                current = current.next
            return None
            

if __name__ == '__main__':
    l = LinkedList()
    l.add( 'a' )
    l.add( 'b' )
    d  =  l.add( 'c' )
    print l      
    l.delete('a')
    print l 
