from snippets.trees.node import Node


class BinarySearchTree:

    def __init__(self, key=None, value=None):
        if key:
            self.root = Node(key, value)
        else:
            self.root = None

    def get_root(self):
        return self.root

    def set_root(self, node):
        self.root = node

    def insert(self, key, value=None):
        if value is None:
            # in most common scenarios, key is itself used as value
            value = key

        #  empty tree
        if not self.get_root():
            self.set_root(Node(key, value))
            return

        current = self.get_root()

        # deliberately not kept recursive, less memory required
        while True:
            if current.get_key() == key:
                current.set_value(value)
                return

            if current.get_key() > key:
                if current.has_left_child():
                    current = current.get_left_child()
                    continue
                else:
                    current.set_left_child(Node(key, value, parent=current))
                    return

            elif current.get_key() < key:
                if current.has_right_child():
                    current = current.get_right_child()
                    continue
                else:
                    current.set_right_child(Node(key, value, parent=current))
                    return
            # some other condition
            break

    def merge_tree(self, start_node, node_to_be_inserted):
        if start_node is None and node_to_be_inserted is None:
            return None
        if start_node is None:
            return node_to_be_inserted
        if node_to_be_inserted is None:
            return start_node
        current = start_node
        while True:
            if current.get_key() > node_to_be_inserted.get_key():
                if current.has_left_child():
                    current = current.get_left_child()
                    continue
                else:
                    current.set_left_child(node_to_be_inserted)
                    node_to_be_inserted.set_parent(current)
                    return start_node

            elif current.get_key() < node_to_be_inserted.get_key():
                if current.has_right_child():
                    current = current.get_right_child()
                    continue
                else:
                    current.set_right_child(node_to_be_inserted)
                    node_to_be_inserted.set_parent(current)
                    return start_node
            # some other condition
            break

    def delete(self, key):
        # empty tree
        if self.get_root() is None:
            return

        root = self.get_root()
        if root.get_key() == key:
            if root.is_leaf():
                self.set_root(None)
                return
            else:
                self.set_root(self.merge_tree(root.get_left_child(), root.get_right_child()))
                return

        del_node = self.get_key(key)
        if del_node is None:
            return
        parent = del_node.get_parent()
        if parent.has_left_child():
            lc = parent.get_left_child()
            if lc.get_key() == key:
                parent.set_left_child(self.merge_tree(lc.get_left_child(), lc.get_right_child()))
                return
            else:
                rc = parent.get_right_child()
                parent.set_right_child(self.merge_tree(rc.get_left_child(), rc.get_right_child()))
        else:
            rc = parent.get_right_child()
            parent.set_right_child(self.merge_tree(rc.get_left_child(), rc.get_right_child()))

    def get_key(self, key):
        current = self.get_root()
        while current:
            current_key = current.get_key()
            if current_key == key:
                return current
            elif current_key < key:
                current = current.get_right_child()
            elif current_key > key:
                current = current.get_left_child()
        return None





