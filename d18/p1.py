def read(filename):
    with open(filename) as f:
        return [eval(line.strip()) for line in f.readlines()]


# Struct for binary tree node with parent & depth data
class Node:
    def __init__(self, val=None, depth=0, parent=None, left=None, right=None):
        self.val = val
        self.depth = depth
        self.parent = parent
        self.left = left
        self.right = right


# Convert snailfish number from nested list to binary tree.
# Leaves are equivalent to regular numbers. Pairs `[x, y]` are `Node`s `n` with `n.left == x`,
# `n.right == y`
def build_tree(sn, depth=0):
    if type(sn) == int:
        return Node(sn, depth)

    left, right = build_tree(sn[0], depth + 1), build_tree(sn[1], depth + 1)
    root = Node(depth=depth, left=left, right=right)
    left.parent = right.parent = root
    return root


# Increment depths of all nodes at and below `node`.
def incr_depths(node):
    node.depth += 1
    if node.left:
        incr_depths(node.left)
    if node.right:
        incr_depths(node.right)


# Add snailfish numbers (represented by trees)
def add(tree_1, tree_2):
    incr_depths(tree_1)
    incr_depths(tree_2)
    root = Node(left=tree_1, right=tree_2)
    tree_1.parent = tree_2.parent = root
    return root


# Find leaf node (regular number) nearest `node` on the right.
def right_neighbor(node):
    while node.parent and node.parent.right == node:
        node = node.parent
    if not node.parent:
        return
    node = node.parent.right
    while node.left:
        node = node.left
    return node


# Find leaf node (regular number) nearest `node` on the left.
def left_neighbor(node):
    while node.parent and node.parent.left == node:
        node = node.parent
    if not node.parent:
        return
    node = node.parent.left
    while node.right:
        node = node.right
    return node


# Search from left to right starting at `node` for an explodable pair and explode it.
# Return whether or not an explosion occurred.
def explode(node):
    if node.depth == 4 and node.left and node.right:
        ln, rn = left_neighbor(node), right_neighbor(node)
        if ln:
            ln.val += node.left.val
        if rn:
            rn.val += node.right.val
        node.val = 0
        node.left = node.right = None
        return True
    return node.left and explode(node.left) or node.right and explode(node.right)


# Search from left to right starting at `node` for a splittable regular number and split it
# Return whether or not a split occurred.
def split(node):
    if node.val is not None and node.val >= 10:
        node.left = Node(node.val // 2, node.depth + 1, node)
        node.right = Node((node.val + 1) // 2, node.depth + 1, node)
        node.val = None
        return True
    return node.left and split(node.left) or node.right and split(node.right)


# Repeatedly explode and split snailfish number representation given by `tree` until no more
# can occur.
def reduce(tree):
    while explode(tree) or split(tree):
        pass
    return tree


def magnitude(node):
    if node.val is not None:
        return node.val
    return 3 * magnitude(node.left) + 2 * magnitude(node.right)


if __name__ == "__main__":
    sns = read("input.txt")
    sum_tree = build_tree(sns[0])
    for sn in sns[1:]:
        sum_tree = add(sum_tree, build_tree(sn))
        reduce(sum_tree)
    print(magnitude(sum_tree))

