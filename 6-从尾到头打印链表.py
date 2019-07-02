from linklist import LList


def print_reverse_list(linked_list):
    llist = LList()
    for node in linked_list:
        llist.prepend(node)
    print(llist)


if __name__ == '__main__':
    link = LList()
    for i in range(10):
        link.append(i)
    print(link)
    print_reverse_list(link)
