from collections import deque


class Queue(deque):
    """ FIFO """
    def enqueue(self, children):
        self.extend(children)

    def dequeue(self):
        return self.popleft()


class Stack(deque):
    """ LIFO """
    def enqueue(self, children):
        self.extend(children)

    def dequeue(self):
        return self.pop()


def search(structure, root):
    while True:
        yield root
        structure.enqueue(root.children)
        if len(structure) == 0:
            break
        root = structure.dequeue()


def bfs(tree):
    return search(Queue(), tree)


def dfs(tree):
    return search(Stack(), tree)


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
    print([i.value for i in bfs(tree)])
    # [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print([i.value for i in dfs(tree)])
    # [0, 2, 5, 1, 4, 8, 7, 6, 3]
