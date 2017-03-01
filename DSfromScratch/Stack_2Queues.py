class Stack:
	def __init__(self):
		self.q1 = []
		self.q2 = []

	def push(self, x):
		self.q1.append(x)
		if len(self.q1==1):
			return
		else:
			self.q2.append(self.q1.pop(0))

	def pop(self):
		self.q1.pop(0)
		for i in range(len(self.q2)-1):
			self.q1.append(self.q2.pop(0))
	    self.q1, self.q2 =  self.q2, self.q1

	def top(self):
		return self.q1[0]

	def empty(self):
		if len(self.q1)==0 and len(self.q2)==0:
			return True
		else:
			return False