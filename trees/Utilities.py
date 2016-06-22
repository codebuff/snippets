def traverse_preorder(tree, operation):
    if tree:
        operation(tree.get_value())
        traverse_preorder(tree.get_left_child(), operation)
        traverse_preorder(tree.get_right_child(), operation)


def traverse_inorder(tree, operation):
    if tree:
        traverse_inorder(tree.get_left_child(), operation)
        operation(tree.get_value())
        traverse_inorder(tree.get_right_child(), operation)


def traverse_postorder(tree, operation):
    if tree:
        traverse_postorder(tree.get_left_child(), operation)
        traverse_postorder(tree.get_right_child(), operation)
        operation(tree.get_value())


def traverse_levelorder(tree, operation):
    from collections import deque
    dq = deque()
    dq.append(tree)
    while dq:
        current = dq.popleft()
        operation(current.get_value())
        if current.has_left_child():
            dq.append(current.get_left_child())
        if current.has_right_child():
            dq.append(current.get_right_child())
