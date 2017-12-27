class Node(object):

    def __init__(self):
        self.count = 0
        self.children = [None for i in range(26)]


class Trie(object):

    def __init__(self):
        self.root = Node()

    def add(self, word):
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = Node()
            curr = curr.children[index]

        curr.count += 1

    def find(self, text):
        curr = self.root
        text_count, match_count = 0, 0
        for c in text:
            index = ord(c) - ord('a')
            if curr.children[index]:
                curr = curr.children[index]
            else:
                return False

        return True if curr.count else False


if __name__ == "__main__":
    t = Trie()
    t.add('ajay')
    t.add('aj')
    t.add('hello')
    t.add('hell')
    print('now printing...', t)
    print(t.find('aj'))
    print(t.find('help'))
    print('now printing...', t)
