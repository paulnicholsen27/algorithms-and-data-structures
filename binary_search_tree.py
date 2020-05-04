class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_after(self.root, Node(new_val))

    def search(self, find_val):
        return self.search_below(self.root, find_val)

    def insert_after(self, start, new_node):
        if new_node.value > start.value:
            if start.right:
                return self.insert_after(start.right, new_node)
            else:
                start.right = new_node
                return 
        if new_node.value < start.value:
            if start.left:
                return self.insert_after(start.left, new_node)
            else:
                start.left = new_node
                return 

    def search_below(self, current_node, value):
        if current_node.value == value:
            return True
        elif value < current_node.value:
            # go left
            if current_node.left:
                return self.search_below(current_node.left, value)
            else: 
                return False
        elif value > current_node.value:
            # go right
            if current_node.right:
                return self.search_below(current_node.right, value)
            else: 
                return False



    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# # Should be False
print tree.search(6)
