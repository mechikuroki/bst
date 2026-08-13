from nodo import Node

class BinarySearchTree:
    def __init__(self, data):
        self.root = Node(data)

    def add(self, data, node):
        if not node:
            return Node(data)
        if node.data > data:
            node.left = self.add(data, node.left)
        else:
            node.right = self.add(data, node.right)
        return node

    def find_min(self, node):
        if node.left == None:
            return node.data
        return self.find_min(node.left)

    def find_max(self, node):
        if node.right == None:
            return node.data
        return self.find_max(node.right)

    def find(self, data, node):
        if not node.right and not node.left:
            return "Not found"
        if node.data == data:
            return node
        elif node.data > data:
            return self.find(data, node.left)
        else:
            return self.find(data, node.right)


bst = BinarySearchTree(8)
bst.add(3, bst.root)
bst.add(6, bst.root)
bst.add(14, bst.root)
bst.add(2, bst.root)

print(bst.find_max(bst.root))
print(bst.find_min(bst.root))
print(bst.find(3, bst.root))
print(bst.find(50, bst.root))

