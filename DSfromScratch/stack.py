class ArrayStack:

    def __init__(self):
        """Create an empty stack."""
        self._items=[] # nonpublic list instance
    
    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._items)
    
    def push(self,item):
        """Add element to the top of the stack."""
        self._items.append(item)
        
    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).
        Raise Empty exception if the stack is empty."""
        if self.isEmpty():
            print "Stack is empty'"
        return self._items.pop()
    
    def isEmpty(self):
        """Return True if the stack is empty."""
        return (len(self._items)==0)

    def top(self):
        """Return (but do not remove) the element at the top of the stack.
        Raise Empty exception if the stack is empty.
        """
        if self.isEmpty():
            #raise Empty('Stack is empty')
            print "Stack is empty'"
        return self._items[-1]

    def __str__(self):
        """ Print the stack object as a string"""
        return " ".join(str(self._items))
    
if __name__ == "__main__":
    s = ArrayStack()
    s.push(1)
    print s
    s.push("s")
    s.push("e")
    s.push("d")
    s.pop()
    print s    