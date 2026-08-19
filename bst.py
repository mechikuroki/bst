from nodo import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, data, node=None):
        if self.root is None:
            self.root = Node(data)
            return self.root

        if node is None:
            node = self.root
            
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.add(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.add(data, node.right)
        return node

    def find_min(self, node):
        if node is None:
            return None
        if node.left is None:
            return node.data
        return self.find_min(node.left)

    def find_max(self, node):
        if node is None:
            return None
        if node.right is None:
            return node.data
        return self.find_max(node.right)

    def _not_has_child(self, node):
        return not node.right and not node.left

    def find(self, data, node=None):
        if node is None:
            node = self.root
        if node is None:
            return "Not found"
        if node.data == data:
            return node
        elif self._not_has_child(node):
            return "Not found"
        elif node.data > data:
            return self.find(data, node.left)
        else:
            return self.find(data, node.right)

    def _find_with_parent(self, data, node, parent=None, is_left=None):
        if node is None:
            return None, None, None
        if node.data == data:
            return node, parent, is_left
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

    def remove(self, data):
        node, parent, is_left = self._find_with_parent(data, self.root)
        if node is None:
            return "Not found"

        children = self._count_children(node)
        is_root = (parent is None)

        match children:
            case 0:
                if is_root:
                    self.root = None
                else:
                    if is_left: parent.left = None
                    else: parent.right = None
                del node
                return "Done"

            case 1:
                child = node.left if node.left else node.right
                if is_root:
                    self.root = child
                else:
                    if is_left: parent.left = child
                    else: parent.right = child
                del node
                return "Done"

            case 2:
                next_node_parent = node
                next_node = node.right
                while next_node.left is not None:
                    next_node_parent = next_node
                    next_node = next_node.left

                if next_node_parent != node:
                    next_node_parent.left = next_node.right
                else:
                    next_node_parent.right = next_node.right

                if is_root:
                    self.root = next_node
                elif is_left:
                    parent.left = next_node
                else:
                    parent.right = next_node

                next_node.left = node.left
                next_node.right = node.right
                del node
                return "Done"
def main():
    bst = BinarySearchTree()
    bst.add(3)
    bst.add(6)
    bst.add(14)
    bst.add(2)

    print(bst.find_max(bst.root))  
    print(bst.find_min(bst.root)) 
    print(bst.find(3))           
    print(bst.find(50))       
    print(bst.remove(3))     
    print(bst.remove(14))   

main()
