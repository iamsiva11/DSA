"""
Every time when pushing one element into stack, push queue 1's top in queue 2, and push the new element in queue 1.

Every time when popping the top element in stack, push the queue 1's top (only one element in this queue). 
Then push n-1 elements from queue 2 to queue 1, where n is the total number of elements in queue 2.
In other words, we left one element in queue 2 (this is the top element in the current stack), and push all the other elements into the empty queue (queue 1).
Finally we swap queue 1 and queue 2. 
The stack is empty iff queue 1 and queue 2 are all empty. The top element is always the only element in queue 1.

"""

class Stack:
	def __init__(self):
		self.q1 = []
		self.q2 = []

	def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q1.append(x)
        if(len(self.q1)==1): #if it was empty
            return
        else:    
            self.q2.append(self.q1.pop(0)) #or just pop() , since q1 len is always 1
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.q1:
            for i in xrange(len(self.q2)-1):
                self.q1.append(self.q2.pop(0))
            self.q1, self.q2 = self.q2, self.q1 
            return self.q1.pop() if self.q1 else None #or pop(0)
        
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q1[0] if self.q1 else None
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q2)==0 and len(self.q1) ==0