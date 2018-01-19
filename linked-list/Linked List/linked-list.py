class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class LinkedList(object):

    def __init__(self):
        self.head = None

    def add_value(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def delete_value(self, val):
        cur = self.head
        if cur.data == val:
            self.head = cur.next
            return

        while cur.next:
            if cur.next.data == val:
                if cur.next.next:
                    cur.next = cur.next.next
                else:
                    cur.next = None
                break
            cur = cur.next

    def __repr__(self):
        res = []
        curr = self.head
        while curr:
            res.append(str(curr.data))
            curr = curr.next
        return '->'.join(res)

    def _print_backward(self, head):
        if not head:
            return None

        self._print_backward(head.next)
        print(head.data)

    def print_backward(self):
        return self._print_backward(self.head)

    def reverse(self):
        if self.head == None or self.head.next == None:
            return
        current = self.head
        prev = None
        while current:
            nextt = current.next
            current.next = prev
            prev = current
            current = nextt

        self.head = prev

    def _recursive_reverse(self, h):
        if not h.next:
            self.head = h
            return
        self._recursive_reverse(h.next)
        q = h.next
        q.next = h
        h.next = None

    def recursive_reverse(self):
        return self._recursive_reverse(self.head)


if __name__ == "__main__":
    l = LinkedList()
    l.add_value(1)
    l.add_value(32)
    l.add_value(19)
    l.add_value(9)
    l.add_value(6)
    print(l)
    print('printing backward...')
    l.print_backward()
    l.reverse()
    print(l)
    l.recursive_reverse()
    print(l)
