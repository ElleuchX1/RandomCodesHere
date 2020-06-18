


class Noeud:
    
    def __init__(self,val):
        self.valeur=val
        self.leftChild=None
        self.rightChild=None
    #---------------------------- INSERT -------------------------------
    def insert1(self,data):
        if self.valeur == data:
            return False
        elif self.valeur >data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild= Noeud(data)
                return True
        else:
            self.rightChild=Noeud(data)
            return True
    #------------------------ FIND ----------------------------------------
    def find1(self,data):
        if(self.valeur == data):
            return True
        elif self.valeur>data:
            if self.leftChild:
                return self.leftChild.find1(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find1(data)
            else:
                return False
    # -------------- PRE ------------------------------
    def preorder1(self):
        print(str(self.valeur))
        if self:
            if self.rightChild:
                return self.rightChild.preorder1()
            if self.leftChild:
                return self.leftChild.preoder1()
    #----------- POST ---------------------------------
    def postorder1(self):
        
        if self:
            if self.rightChild:
                return self.rightChild.postorder1()
            if self.leftChild:
                return self.leftChild.postoder1()
        print(str(self.valeur))
    #--------- IN -----------------------------------------
    def inorder1(self):
        
        if self:
            if self.rightChild:
                return self.rightChild.inorder1()
            print(str(self.valeur))
            if self.leftChild:
                return self.leftChild.inorder1()
        

#---------------------------------------------------------------------------
class Tree():
    def __init__(self):
        self.root=None
    #----------------------- INSERT ---------------------------
    def insert(self,data):
        if self.root:
            return self.root.insert1(data)
        else:
            self.root= Noeud(data)
            return True
    #-------------------------- FIND -------------------------
    def find(self,data):
        if self.root:
            return self.root.find1(data)
        else:
            return False
    #----------------------- PRE -----------------------------
    def preorder(self):
        print("PreOrder")
        self.root.preorder1()
    #------------------------ POST --------------------------
    def postorder(self):
        print("PostOrder")
        self.root.postorder1()
    #----------------------- IN ---------------------
    def inorder(self):
        print("InOrder")
        self.root.inorder1()


myTree=Tree()
myTree.insert(10)
myTree.insert(15)
myTree.insert(16)
print(myTree.find(16))
