from linklist import LList


def print_reverse_list(linked_list):
    llist = LList()
    for node in linked_list:
        llist.prepend(node)
    llist.print_all()


if __name__ == '__main__':
    link = LList()
    for i in range(10):
        link.append(i)
    link.print_all()
    print_reverse_list(link)
