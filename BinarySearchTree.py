import sys
#import pydot
import random

class Node:
    def __init__(self,depth,value):
        self.left = None
        self.right = None
        self.value = value
        self.parent = None 

    def getValue(self):
        return self.value 

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setValue(self, newdata):
        self.value = newdata

    def setLeft(self,newleft):
        self.left = newleft

    def setRight(self,newright):
        self.right = newright 

    def getParent(self):
        return self.parent

    def setParent(self, newparent):
        self.parent = newparent

    def children_count(self):
        if self is None:
            return None
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt


    def replaceNodeData(self,key,value):
        self.key = key
        self.value = value
        self.leftChild = lc
        self.rightChild = rc
        if self.getLeft():
            self.left.parent = self
        if self.getRight():
            self.right.parent = self


class binaryTree(Node):
    def __init__(self, depth):
        self.root =  None
        #self.left  = binaryTree(depth-1, value*2 + 1) if depth > 0 else None
        #self.right = binaryTree(depth-1, value*2 + 2) if depth > 0 else None
    
    def addNode(self, depth,value):
        return Node(depth,value)

    def insert(self, root,value, depth):
        if(root == None):
            return self.addNode(depth,value)
        else:
            if(value <= root.value):
                root.left = self.insert(root.left,value, depth)
                root.left.parent = root
            else:
                root.right = self.insert(root.right,value, depth)
                root.right.parent = root
            return root 

    def find(self, root,target, parent=None):
        if root == None:
            return 0
        else:
            if target == root.value:
                return 1
            else:
                if target < root.value:
                    return self.find(root.left, target)
                else:
                    return self.find(root.right, target)

    def findNode(self, root,target, parent=None):
        if root == None:
            return 0
        else:
            if target == root.value:
                return root 
            else:
                if target < root.value:
                    return self.findNode(root.left, target)
                else:
                    return self.findNode(root.right, target) 

    def delete(self,root, value):
        node = self.findNode(root,value)
        parent = node.parent
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
                    successor = successor.left 
                    parent = successor
                node.value = successor.value 
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right 

    def replaceValue(self,root,value,target):
        node = self.findNode(root,value)
        if node.value is not None:
            node.value = target
        else:
            return None

    def verify(self,root):
        if not root:
            return True
        if (self.maxDepth(root) <= root.value <= self.minValue(root) and self.verify(root.left) and self.verify(root.right)):
            return True
        else: 
            return False  

    def rotatation(self, root, value):
        node = self.findNode(root,value)
        parent = node.getParent()
        node.setParent(parent.getParent())
        if node.getValue() > parent.getValue():
            right = node.getRight()
            node.setRight(parent)
            self.insert(right, node)
        if node.getValue() <= parent.getValue():
            left = node.getLeft()
            node.setLeft(parent)
            self.insert(left, node)

    def minValue(self,root):
        while(root.left != None):
            root = root.left
        return root.value 

    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            ldepth = self.maxDepth(root.left)
            rdepth = self.maxDepth(root.right)
            return max(ldepth, rdepth) + 1

    def size(self, root):
        if root == None:
            return 0
        else:
            return self.size(root.left) + 1 + self.size(root.right)

    def printTree(self, root):
        if root == None:
            pass
        else:
            self.printTree(root.left)
            print(root.value)
            self.printTree(root.right)

    def printRevTree(self, root):
        if root == None:
            pass
        else:
            self.printRevTree(root.right)
            print(root.value)
            self.printRevTree(root.left)
            

    #def createGraph(self):
    #    if(self.root == None):
    #        raise Exception()
    #    graph = pydot.Dot(graph_type='graph')
    #    colorSequence = ["red,","orange","yellow","green","blue","indigo","violet"]
    #    graphNode = pydot.Node(self.root.getValue(),style="filled",fillcolor=colorSequence[0])
     #   graph.add_node(graphNode)
     #   graph = self.createGraphHelper(self.root.getValue(),self.root.getLeft(),1,colorSequence,graph,"left")
     #   graph = self.createGraphHelper(self.root.getValue(),self.root.getRight(),1,colorSequence,graph,"right")
     #   graph.write_png("bstGraph.png")

    #def createGraphHelper(self,prevValue,bstNode,level,colorSequence,graph,direction):
    #    if(bstNode == None):
    #        return graph
    #    else:
    #        graphNode = pydot.Node(bstNode.getValue(),style="filled",fillcolor=colorSequence[level % 7])
    #        graph.add_node(graphNode)
    #        if(direction == "left"):
    #            graph.add_edge(pydot.Edge(prevValue,bstNode.getValue(),color="green"))
    #        elif(direction == "right"):
     #            graph.add_edge(pydot.Edge(prevValue,bstNode.getValue(),color="red"))
    #        else:
    #             raise Exception()
     #       graph = self.createGraphHelper(bstNode.getValue(),bstNode.getLeft(),level+1,colorSequence,graph,"left")
     #       graph = self.createGraphHelper(bstNode.getValue(),bstNode.getRight(),level+1,colorSequence,graph,"right")
      #      return graph

if __name__ == "__main__":
    data = int(input("insert the the depth of the tree:"))
    BTree = binaryTree(data)
    root = BTree.addNode(data,0)
    #for i in range(len(items)):
    #    #BTree.insert(root,(random.randrange(20)))
    #    BTree.insert(root, item)
    #print()
    for i in range(0,data):
        #data = int(input("insert the node value:"))
        BTree.insert(root,random.randrange(0,50),data)
    print()

    #BTree.printRevTree(root)
    BTree.printTree(root)
    #print()
    data = int(input("insert a value to find:"))
    if BTree.find(root,data):
        print("found")
    else:
        print("not found")
    print()
    data = int(input("insert a value to delete:"))
    print("Deleting",data)
    BTree.delete(root,data)
    BTree.printTree(root)
    #BTree.printTree(root)
    print()
    target = int(input('insert which value you want to replace'))
    data = int(input('insert node value:'))
    BTree.replaceValue(root,target,data)
    #BTree.printTree(root)
    data = int(input('insert node value to root:'))
    BTree.rotatation(root,data)
    #BTree.printTree(root)
    print()
    print("This is the BTree min", BTree.minValue(root))
    print("This is the BTree maxDepth",BTree.maxDepth(root))
    print("This is the BTree's size", BTree.size(root))
    #print("Verifying", BTree.verify(root))
    #BTree.createGraph()

