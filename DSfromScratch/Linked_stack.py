class _Node:
	
	def __init__(self, element, next):
		self._element = element
		self._next = next

## Stack implementation with linked list
class LinkedStack:
	
	def __init__(self):
		self._head = None
		self._size = 0

	def push(self, e):		
		self._head = _Node(e, self._head)
		self._size += 1

	def __len__(self):
		return self.size

	def is_empty(self):
		#return self.size==0
		pass

	
	def pop(self):
		tmp=self._head
		self._head = self._head.next
		del tmp 
		self.size -= 1

	def top(self):
		if(self.is_empty()):
			print("Stack is empty")
		return self._head.element

	def __str__(self):
		elem=[]
		while(self._head!= None):
			elem.append(self._head._element)
			self._head=self._head._next
		return "".join(str(elem))


if __name__=="__main__":
	s = LinkedStack()
	s.push(1)
	s.push(2)
	s.push(7)
	print s	