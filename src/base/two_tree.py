class TreeStruct(object):
    def __init__(self, num):
        self.element = num
        self.leftNode = None
        self.rightNode = None

    def pre_list(self, node):
        while True:
            if node is None:
                print(node.element)
                break
            else:
                print("element root: " + str(tree.element))
                self.pre_list(node.leftNode)
                self.pre_list(node.rightNode)

tree = TreeStruct(1)
treeL1 = TreeStruct(11)
treeR1 = TreeStruct(12)
tree.leftNode = treeL1
tree.rightNode = treeR1
treeL11 = TreeStruct(111)
treeR11 = TreeStruct(113)
treeR1.leftNode = treeL11
treeR1.rightNode = treeR11
treeL12 = TreeStruct(121)
treeR12 = TreeStruct(122)

tree.pre_list(tree)
