### The Challenge

'''
You are given a list of numbers stored in a list, A. 
Your challenge is to build a [Binary Search Tree] (https://en.wikipedia.org/wiki/Binary_search_tree) to store these numbers. 
You will need to:
    Represent each node of the tree (including its data, left child and right child).
    Print the tree out in an understandable form.
    Make a function to insert a list of numbers (A) into the tree.
    Check if you can insert all the numbers in A into your tree, and that it prints out as expected.
Use the language of your choice to solve this challenge, but only submissions in languages taught by Codecademy are eligible to “win”.
'''

### Intermediate difficulty
'''
Write a function to check if the Binary Search Tree that you’ve created is balanced.
A tree is considered balanced when the difference between the min height and max height does not exceed 1, 
i.e. if the list had n elements in it the height of the tree would be log(n) (base 2).
'''

### Hard Difficulty

'''        
Adapt your function to insert a list of n numbers so that it runs in O(n log n) time. 
Bear in mind that this is just the average case for a random sequence of numbers.
If the list A was sorted it would take O(n^2).
Adapt your function to check if the tree is balanced so that it runs in O(n) time.
If your BST is balanced then the insert function would have only taken O(n log n) time, see if you can figure out why.
'''

# Create a node
class TreeNode(object):
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None       
        
    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.value)
    
    def __str__(self):
        return "{}".format(self.value)    
    
# Create a binary search tree
class BinarySearchTree(object):
    
    def __init__(self, values):
        self.root = TreeNode(values.pop(0))
        self.add_nodes(values)
    
    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self.root.value)
        
    def __str__(self):  
        lines, *_ = self._display()
        output = ""
        for line in lines:
            output += line + "\n"
        return output

    # Borrowed and adapted from: 
    # https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/34014370     
    # Returns list of strings, width, height, and horizontal coordinate of the root.      
    def _display(self, node=None):
        
        if not self.root:
            print("Empty Tree")
              
        else:
            if node is None:
                node = self.root
        
            # No children
            if not node.right and not node.left:
                line = '%s' % node.value
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child
            if not node.right:
                lines, n, p, x = self._display(node.left)
                s = '%s' % node.value
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child
            if not node.left:
                lines, n, p, x = self._display(node.right)
                s = '%s' % node.value
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children
            left, n, p, x = self._display(node.left)
            right, m, q, y = self._display(node.right)
            s = '%s' % node.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2
        
    # Insert a node
    def add_node(self, value):
        node = self.root
        while node: 
            if value == node.value:
                break
            elif value < node.value:
                if node.left is None:
                    node.left = TreeNode(value)
                    return
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(value)
                    return
                else:
                    node = node.right

    # Insert multiple nodes from a list
    def add_nodes(self, values):
        for value in values:
            self.add_node(value)  

    # Calculate tree height:
    def height(self, node=None):
        if not node:
            node = self.root
        if node.left:
            left_height = self.height(node.left) + 1
        else:
            left_height = 0
        if node.right: 
            right_height = self.height(node.right) + 1
        else:
            right_height = 0
        return max(left_height, right_height)
    
    # Return if a tree balanced
    def balanced(self, node=None, height=0):
        if not node:
            node = self.root
        if node.left:
            left_height = self.height(node.left)
            self.balanced(node.left, left_height)
        else:
            left_height = 0
        if node.right: 
            right_height = self.height(node.right)
            self.balanced(node.right, right_height)
        else:
            right_height = 0
        if abs(left_height - right_height) > 1:
            return False
        else:
            return True
        
# Tests
import random

random_integer = [random.randint(0, 100)]
myTree = BinarySearchTree(random_integer)
print(myTree)
print(myTree.height())
print(myTree.balanced())

random_integers = [random.randint(0, 100) for _ in range(10)]
myTree = BinarySearchTree(random_integers)
print(myTree)
print(myTree.height())
print(myTree.balanced())

sorted_integers = [_ * 10 for _ in range(10)]
myTree = BinarySearchTree(sorted_integers)
print(myTree)
print(myTree.height())
print(myTree.balanced())

random_integer = random.randint(0, 100)
myTree.add_node(random.randint(0, 100))
print(myTree)
print(myTree.height())
print(myTree.balanced())

random_integers = [random.randint(0, 100) for _ in range(10)]
myTree.add_nodes(random_integers)
print(myTree)
print(myTree.height())
print(myTree.balanced())

balanced_numbers = [50, 25, 75, 12, 36, 60, 80, 6, 16, 18, 38, 55, 65, 75, 85]
myTree = BinarySearchTree(balanced_numbers)
print(myTree)
print(myTree.height())
print(myTree.balanced())