class Node:
    def __init__(self,value, parent = None):
        self.left = None
        self.right = None
        self.parent = parent
        self.value = value
class BST:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if (self.root == None):
            self.root = Node(value, None)
        else:
            self._insert(value, self.root)
    def _insert(self,value, node):
        if value > node.value:
            if node.right == None:
                node.right = Node(value, parent = node)
            else:
                self._insert(value, node.right)
        elif value < node.value:
            if node.left == None:
                node.left = Node(value, parent = node)
            else:
                self._insert(value, node.left)
            
    def search(self, value):
        if (self.root == None):
             return None
        else:
            self._search(value, self.root)
    def _search(self, value, node):
        if (node.value == value):
            return True
        if value > node.value:
            if node.right != None:
                self._search(value, node.right)
        if value < node.value:
            if node.left != None:
                self._search(value, node.left)
        return None 
    
    def delete(self, value):
        if (self.root == None):
             return None
        else:
            self._delete(value = value, node = self.root)
    def _delete(self, value, node):

        if (value >node.value):
            if node.right != None:
                self._delete(value, node.right)
        if value < node.value:
            if (node.left != None):
                self._delete(value, node.left)
        elif (node.value == value):
            def children_num(node):
                return int(node.left != None) + int(node.right != None)
            
            children = children_num(node)

            if children == 0: 
                parent_node = node.parent

                if node.parent == None:
                    self.root = None
                    return 
                
                elif node == parent_node.left:
                    parent_node.left = None
                elif node == parent_node.right:
                    parent_node.right = None
                
                node.value = None
                del node
            elif children == 1:
                node_parent = node.parent
                
                if node_parent == None:
                    if node.left != None:
                        self.root = node.left
                        node.left.parent = None
                    elif node.right !=None:
                        self.root = node.right
                        node.right.parent = None
                
                elif node.left != None:
                    
                    if node_parent.left == node:
                        node_parent.left = node.left
                    elif node_parent.right == node:
                        node_parent.right = node.left
                    node.left.parent = node_parent
                elif node.right != None :
                    if node_parent.right == node:
                        node_parent.right = node.right
                    elif node_parent.left == node:
                        node_parent.left = node.right
                    node.right.parent = node_parent 
            elif children == 2:
                
                
                smallest = node.left
                while(smallest.left):
                    smallest = smallest.left
                node.value = smallest.value 
                
                self._delete(value = smallest.value, node = smallest)                    
            
    def display(self):
        '''gotten from github name: '''
        if self.root!=None:
            lines, *_ =  self._display_aux(self.root)
            for line in lines:
                print(line)
        else:
            return None    
    def _display_aux(self, node):
    
        if node.right is None and node.left is None:
            line = '%s' % node.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = '%s' % node.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = '%s' % node.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
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
        

