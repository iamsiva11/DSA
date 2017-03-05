"""FIFO queue implementation using a Python list as underlying storage."""
class ArrayQueue:
    
    def __init__(self):
        """Create an empty queue."""
        self._items=[]        

    def enqueue(self, item):
        """Add an element to the back of queue."""
        self._items.append(item)
    
    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty."""

        if (not self.isEmpty()):  
            temp = self._items[0]
            self._items = self._items[1:]            
            del temp

    def isEmpty(self):
        return len(self._items)==0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty."""
        if self.isEmpty():
            print "Queue is empty"
        return self._items[0]
    
    def __str__(self):
        """ Print the queue object as a string"""
        return " ".join(str(self._items))
    
    def __len__(self):
    """Return the number of elements in the queue."""
        return len(self._items)

if __name__ == "__main__":
    q = ArrayQueue()
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    q.enqueue(4)    
    q.enqueue(5)
    q.dequeue()
    print q