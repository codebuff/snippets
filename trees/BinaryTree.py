class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def add_left_child(self, data):
        if self.left_child:
            t = BinaryTree(data)
            t.left_child = self.left_child
            self.left_child = t
        else:
            self.left_child = BinaryTree(data)

    def add_right_child(self, data):
        if self.right_child:
            t = BinaryTree(data)
            t.right_child = self.right_child
            self.right_child = t
        else:
            self.right_child = BinaryTree(data)

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_node_data(self, data):
        self.data = data

    def get_node_data(self):
        return self.data

