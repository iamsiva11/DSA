class TreeNode:
    def __init__(self, data , left= None, right = None):
        self.data = data
        self.left = left
        self.right = right
        
class BST:
    
    def __init__(self):
        self.root = None
        
    def getRoot(self):
        return self.root.data
    
    def addNode(self, node, value):
        if(node==None):
            self.root= TreeNode(value)
        else:
            if(value < node.data):
                if(node.left==None):
                    node.left = TreeNode(value)
                else:
                    self.addNode(node.left, value)
            else:
                if(node.right==None):
                    node.right = TreeNode(value)
                else:
                    self.addNode(node.right, value)

                    
    def printInorder(self, node):
        if(node!=None):
            self.printInorder(node.left)
            print(node.data)
            self.printInorder(node.right)            
        
    def printPreOrder(self, node):
        pass
    
    def printPostOrder(self, node):
        pass
    

#     3
# 0     4
#   2      8

if __name__=="__main__":
    tree = BST()
    tree.addNode(tree.root,3)
    tree.addNode(tree.root,4)
    tree.addNode(tree.root,0)
    tree.addNode(tree.root,8)
    tree.addNode(tree.root,2)
    print tree.printInorder(tree.root)
    #print tree.getRoot
    print tree.root.data