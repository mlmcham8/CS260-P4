class BSTnode(object):
    def __init__(self, parent, t):
        self.key = t
        self.parent = parent
        self.left = None
        self.right = None
        self.size = 1
        

    def children_count(self):
        if self is None:
            return None
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt
    
    def getKey(self):
        return self.key

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setKey(self, newdata):
        self.key = newdata

    def setLeft(self,newleft):
        self.left = newleft

    def setRight(self,newright):
        self.right = newright

    def getParent(self):
        return self.parent

    def setParent(self, newparent):
        self.parent = newparent

    def update_stats(self):
        self.size = (0 if self.left is None else self.left.size) + (0 if self.right is None else self.right.size) 

    def insert(self, t, NodeType):
        self.size += 1
        if t < self.key:
            if self.left is None:
                self.left = NodeType(self, t)                
                return self.left
            else:
                return self.left.insert(t, NodeType)
        else:
            if self.right is None:
                self.right = NodeType(self, t)   
                return self.right
            else:
                return self.right.insert(t, NodeType)

    def find(self, t):
        if t == self.key:
            return self
        elif t < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(t)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(t)

    def rank(self, t):
        left_size = 0 if self.left is None else self.left.size 
        if t == self.key:
            return left_size + 1
        elif t < self.key:
            if self.left is None:
                return 0
            else:
                return self.left.rank(t)
        else:
            if self.right is None:
                return left_size + 1
            else:
                return self.right.rank(t) + left_size + 1 
            
    def minimum(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def check(self, lokey, hikey):
        if lokey is not None and self.key <= lokey:
            raise "BST RI violation"
        if hikey is not None and self.key >= hikey:
            raise "BST RI violation"
        if self.left is not None:
            if self.left.parent is not self:
                raise "BST RI violation"
            self.left.check(lokey, self.key)
        if self.right is not None:
            if self.right.parent is not self:
                raise "BST RI violation"
            self.right.check(self.key, hikey)
        if self.size != 1 + (0 if self.left is None else self.left.size) + (0 if self.right is None else self.right.size):
            raise "BST RI violation"
            
    def __repr__(self):
        return "<BST Node, key:" + str(self.key) + ">"

class BST(BSTnode):

    def __init__(self, NodeType = BSTnode):
        self.root = None
        self.NodeType = NodeType
        self.psroot = self.NodeType(None, None)

    def reroot(self):
        self.root = self.psroot.left

    def insert(self, t):
        if self.root is None:
            self.psroot.left = self.NodeType(self.psroot, t)
            self.reroot()
            return self.root
        else:
            return self.root.insert(t, self.NodeType)
        
    def find(self, t, parent= None):
        if self.root is None:
            return None
        else:
            return self.root.find(t)
        
    def load(self):
        with open('txt.py', 'r') as f:
            tree = BSTnode(None,f.readline().rstrip('\n'))
            ntree = BST(tree)
            return ntree

    def replaceValue(self,value,target):
        node = self.root.find(value)
        if node.key is not None:
            node.key = int(target)
            self.reroot()
        else:
            return None

    def rank(self, t):
        if self.root is None:
            return 0
        else:
            return self.root.rank(t)        

    def delete(self, value):
        node = self.root.find(value)
        parent = node.getParent()
        if node is not None:
            children_count = node.children_count()
            if children_count == 0:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            elif children_count == 1:
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent.left is node:
                    parent.left = n
                else:
                    parent.right = n
                del node
            else:
                parent = node
                sucessor = node.right
                while sucessor.left:
                    parent = successor
                    successor = successor.left
                    node.value = successor.key
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right
        self.reroot()

    def check(self):
        if self.root is not None:
            self.root.check(None, None)

    def delete_min(self):
        if self.root is None:
            return None, None
        else:
            # Walk to leftmost node.
            node = self.root
            while node.left is not None:
                node = node.left
            # Remove that node and promote its right subtree.
            if node.parent is not None:
                node.parent.left = node.right
            else: # The root was smallest.
                self.root = node.right
            if node.right is not None:
                node.right.parent = node.parent
            parent = node.parent
            node.disconnect()
            return node, parent

    def maxDepth(self):
        if self.root == None:
            return 0
        else:
            ldepth = self.maxDepth(root.left)
            rdepth = self.maxDepth(root.right)
            return max(ldepth, rdepth) + 1

    def size(self, root):
        if self.root == None:
            return 0
        else:
            return self.size(root.left) + 1 + self.size(root.right)
    
    def verify(self):
        if not self.root:
            return True
        if (self.maxDepth() <= root.key <= self.minValue() and 
self.verify(root.left) and self.verify(root.right)):
            return True
        else:
            return False

    def rotation(self, value):
        node = self.root.find(value)
        parent = node.getParent()
        node.setParent(node)
        if node.getKey() > parent.getKey():
            right = node.getRight()
            node.setRight(parent)
            self.insert(value)
        if node.getKey() <= parent.getKey():
            left = node.getLeft()
            node.setLeft(parent)
            self.insert(node)
        
        
    def minValue(self):        
        while(node.left != None):
            root = node.left        
        return root.key

    def __str__(self):
        if self.root is None: return '<empty tree>'
        def recurse(node):
            if node is None: return [], 0, 0
            label = str(node.key)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
               node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.': label = ' ' + label[1:]
            if label[-1] == '.': label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle-2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
              [left_line + ' ' * (width - left_width - right_width) +
               right_line
               for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width
        return '\n'.join(recurse(self.root) [0])

def printsizes(node):
    if node is None:
        print("node is nil")
    else:
        print("node", node.key, "has a subtree of size", node.size)

def test(args=None, BSTtype=BST):
    import random, sys
    if not args:
        args = sys.argv[1:]
    if not args:
    #    print('usage: %s <number-of-random-items | item item item ...>')
        sys.argv[0]
        sys.exit()
    elif len(args) == 1:
        items = (random.randrange(100) for i in range(int(args[0])))
    else:
        items = [int(i) for i in args]

    tree = BSTtype()
    print(tree)
    for item in items:
        tree.insert(item)
        print()
    print(tree)
    data = int(input("insert a value to find:"))
    if tree.find(data):
        print('yaya found')
    else: 
        print('opps,not found')
    print()
    #print('Deleting The Min')
    #tree.delete_min()
    #print(tree)
    print()
    tree.find(data)
    value = int(input("insert which value you want to replace:"))
    print()
    target = int(input("enter a value you want to replace that value:"))
    print()
    tree.replaceValue(value,target)
    print(tree)
    data = int(input("enter a value you want to delete:"))
    tree.delete(data)
    print(tree)
    #tree.load()
    #print(tree)
    #print("Verifying", tree.verify())
    #data = int(input("enter a value you want to rotate left:"))
    #tree.rotation(data)
    #print(tree)
    #data = int(input("enter a value you want to rotate right:"))
    #tree.right_rotation(data)
    #print(tree)
    #print("This is the BTree min", tree.minValue())
    #print("This is the BTree maxDepth",tree.maxDepth())
    #print("This is the BTree's size", tree.size())

if __name__ == '__main__': test()
