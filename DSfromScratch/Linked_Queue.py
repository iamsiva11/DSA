class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""

    def __init__(self, element, next):
      self._element = element
      self._next = next

class LinkedQueue:

	def __init__(self):
		self._head = None
    	self._tail = None
    	self._size = 0    

    def __len__(self):
	    """Return the number of elements in the queue."""
    	return self._size

    def enqueue(self,e):
    	"""Add an element to the back of queue."""
		newNode = Node(e,None)
	    if self.is_empty():
	    	self._head=newNode
	    else:    	
	    	self._tail.next = newNode
	    	self._tail=newNode
	    	self._size+=1
