class Node:
    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = parent
        self.height = None
        self.depth = None

    def get_key(self):
        return self.key

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_left_child(self, left_child):
        self.left_child = left_child

    def set_right_child(self, right_child):
        self.right_child = right_child

    def get_parent(self):
        return self.parent

    def set_parent(self, node):
        self.parent = node

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height

    def get_depth(self):
        return self.depth

    def set_depth(self, depth):
        self.depth = depth

    def has_right_child(self):
        if self.right_child is None:
            return False
        else:
            return True

    def has_left_child(self):
        if self.left_child is None:
            return False
        else:
            return True

    def is_leaf(self):
        return self.left_child is None and self.right_child is None
