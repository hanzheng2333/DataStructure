class Node:
    val = ""
    next = None

    def __init__(self, val):
        self.val = val


def get():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    a.next = b
    b.next = c
    c.next = d
    return a


list = get()


# 遍历
def node_print(node: Node):
    current = node
    while (current != None):
        print(current.val)
        current = current.next


def node_fide(node: Node):
    current = node
    while (current != None):
        current = current.next

        if current.val == 3:
            return current


def insert(list, val):
    f = Node(val)
    f.next = list
    return f


old = None
new_list = insert(old, 1)
new_list = insert(new_list, 2)
new_list = insert(new_list, 3)

node_print(list)
_ = 1


def new_print(list):
    if (list == None):
        return
    print(list.val)
    new_print(list.next)


def new_print_2(list):
    if (list == None):
        return
    new_print_2(list.next)
    print(list.val)



print("-------------")
new_print_2(list)

