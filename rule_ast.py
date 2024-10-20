class RuleNode:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type
        self.left = left  
        self.right = right  
        self.value = value  

    def __repr__(self):
        if self.type == "operator":
            return f"({self.left} {self.value} {self.right})"
        else:
            return f"{self.value}"
