from collections import deque


class Queue(deque):
    def enqueue(self, children):
        self.extend(children)

    def dequeue(self):
        return self.popleft()


class Stack(deque):
    def enqueue(self, children):
        self.extend(children)

    def dequeue(self):
        return self.pop()


def search(structure, root, children_of):
    while True:
        yield root
        structure.enqueue(children_of(root))
        if len(structure) == 0:
            break
        root = structure.dequeue()


def bfs(tree, children_of):
    return search(Queue(), tree, children_of)


def dfs(tree, children_of):
    return search(Stack(), tree, children_of)


if __name__ == "__main__":
    # create example tree
    class Node(object):
        def __init__(self, value, *children):
            self.value = value
            self.children = list(children)

        def __repr__(self):
            return "Node({})".format(self.value)

    tree = Node(
        0,
        Node(1, Node(3), Node(4, Node(6), Node(7), Node(8))),
        Node(2, Node(5)),
    )
    print([i.value for i in bfs(tree, lambda node: node.children)])
    print([i.value for i in dfs(tree, lambda node: node.children)])

    # nodes can be in any format. these nodes are 2-tuples of
    # the value and a list of its children.
    tree = (
        0,
        [
            (1, [(3, []), (4, [(6, []), (7, []), (8, [])])]),
            (2, [(5, [])])
        ]
    )
    print([i[0] for i in bfs(tree, lambda node: node[1])])
    print([i[0] for i in dfs(tree, lambda node: node[1])])
