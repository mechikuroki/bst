from nodo import Node

#por como hice el árbol se fuerza que haya una root

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, data, node):
        if not self.root:
            self.root = Node(data)
            return
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

    def _not_has_child(self, node):
        if not node.right and not node.left:
            return True
        else: 
            return False

    def find(self, data, node=None):
        if node is None:
            node = self.root
        if node.data == data:
            return node
        elif self._not_has_child(node):
            return "Not found"
        elif node.data > data:
            return self.find(data, node.left)
        else:
            return self.find(data, node.right)

    def _find_with_parent(self, data, node, parent=None, is_left=None):
        if node.data == data:
            return node, parent, is_left
        elif self._not_has_child(node):
            return None
        elif node.data > data:
            return self._find_with_parent(data, node.left, node, True)
        else:
            return self._find_with_parent(data, node.right, node, False)
 
    def _count_children(self, node):
        children = 0
        if node.left:
            children += 1
        if node.right:
            children += 1
        return children

     def _find_min_remove(self, node, parent=None):
        if node.left == None:
            node_copy = node
            parent.left = None
            return node_copy
        return self.find_min(node.left, node)

   
    def remove(self, data):
        try:
            node, parent, is_left = _find_with_parent(data, self.root)
        except:
            return "Not found"
        children = _count_children(node)
        match children:
            case 0:
                if is_left:
                    parent.left = None
                    del node
                    return
                else:
                    parent.right = None
                    del node
                    return
            case 1:
                is_child_left = True if node.left else False
                if is_left:
                    if is_child_left:
                        parent.left = node.left
                    else:
                        parent.left = node.right
                else:
                    if is_child_left:
                        parent.left = node.left
                    else:
                        parent.left = node.right
            case 2:
                new = _find_min_remove(node.right)
                if is_left:
                    parent.left = new

            

bst = BinarySearchTree()
bst.add(3, bst.root)
bst.add(6, bst.root)
bst.add(14, bst.root)
bst.add(2, bst.root)

print(bst.find_max(bst.root))
print(bst.find_min(bst.root))
print(bst.find(3, bst.root))
print(bst.find(50, bst.root))

