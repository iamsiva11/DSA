class Stack:

	def __init__(self):
		self.q=[]

	def push(self,x):
		self.q.append(x)

	def pop(self):
		n=len(self.q)
		pop_element=None
		
		#Bring all elements from front to back
		for _ in range(n):
			self.q.append(self.q[0])
			del self.q[0]

		return self.q.pop()
    
	def __str__(self):
		return ",".join(map(str,self.q))

if __name__=="__main__":
	stck=Stack()
	stck.push(2)
	stck.pop()
	stck.push(3)
	stck.push(4)
	stck.push(6)
	stck.pop()
	print stck

"""
3,4
"""	