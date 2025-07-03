class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])  # The first value is the root
    queue = [root]  # This queue will help in assigning children nodes
    index = 1  # Start inserting nodes after the root
    
    while index < len(values):
        current = queue.pop(0)  # Pop the first element in the queue
        
        # Add the left child if it exists
        if index < len(values):
            current.left = TreeNode(values[index])
            queue.append(current.left)  # Append the left child to the queue
            index += 1
        
        # Add the right child if it exists
        if index < len(values):
            current.right = TreeNode(values[index])
            queue.append(current.right)  # Append the right child to the queue
            index += 1
    
    return root

def create_bst(values):
    if not values:
        return None
    
    # Sort the values first to maintain the BST property
    values.sort()
    
    # Helper function to create a BST from a sorted list of values
    def build_bst_from_sorted_list(values):
        if not values:
            return None
        
        mid = len(values) // 2
        root = TreeNode(values[mid])
        root.left = build_bst_from_sorted_list(values[:mid])
        root.right = build_bst_from_sorted_list(values[mid+1:])
        return root
    
    return build_bst_from_sorted_list(values)

def preorder_traverse(root):
    if not root:
        return
    
    print(root.val, "=>", end="")
    preorder_traverse(root.left)
    preorder_traverse(root.right)
    
def inorder_traverse(root):
    if not root:
        return
    
    inorder_traverse(root.left)
    print(root.val, "=>", end="")
    inorder_traverse(root.right)
    
def postorder_traverse(root):
    if not root:
        return

    postorder_traverse(root.left)
    postorder_traverse(root.right)            
    print(root.val, "=>", end="")
        
def tree_heigth(root):
    if not root:
        return 0
        
    left_height = tree_heigth(root.left)
    right_height = tree_heigth(root.right)
    
    return 1 + max(left_height, right_height)

# test    
nodes = [5, 3, 7, 2, 4, 8 , 6, 1]

root = create_tree(nodes)
print("Pre-Order:")
preorder_traverse(root)
print()

print("In-Order:")
inorder_traverse(root)
print()

print("Post-Order:")
postorder_traverse(root)
print()

nodes = [1, 8, 3, 4, 7, 6 , 5, 2]
root = create_bst(nodes)
print("Pre-Order:")
preorder_traverse(root)
print()

print("In-Order:")
inorder_traverse(root)
print()

print("Post-Order:")
postorder_traverse(root)
print()

print("Tree Height:", tree_heigth(root))