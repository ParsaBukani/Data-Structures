import sys
import re


INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'


class MinHeap:
    class Node:
        pass

    def __init__(self):
        self.heap = []

    def bubble_up(self, index):
        self._checkValidation(index)

        father = self._father(index)
        while index > 0 and self.heap[father] > self.heap[index]:
            self.heap[father], self.heap[index] = self.heap[index], self.heap[father]
            index = father
            father = self._father(index)

    def bubble_down(self, index):
        self._checkValidation(index)

        while True:
            left = self._left(index)
            right = self._right(index)
            smallest = index

            if left is not None and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right is not None and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def heap_push(self, value):
        self.heap.append(value)
        self.bubble_up(len(self.heap) - 1)

    def heap_pop(self):
        if len(self.heap) == 0:
            raise Exception(EMPTY)

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        root = self.heap.pop()
        if len(self.heap) > 0:
            self.bubble_down(0)
        return root

    def find_min_child(self, index):
        self._checkValidation(index)

        left = self._left(index)
        right = self._right(index)

        if left is not None and right is not None:
            if self.heap[left] <= self.heap[right]:
                return left
            else:
                return right
        elif left is not None:
            return left
        return None

    def heapify(self, *args):
        for value in args:
            self.heap.append(value)
        start_index = self._father(len(self.heap) - 1)
        for i in range(start_index, -1, -1):
            self.bubble_down(i)

    def _checkValidation(self, index):
        if (not isinstance(index, int)):
            raise Exception(INVALID_INDEX)
        elif index >= len(self.heap) or index < 0:
            raise Exception(OUT_OF_RANGE_INDEX)


    def _father(self, index):
        if index == 0:
            return 0
        return (index - 1) // 2

    def _right(self, index):
        r = 2 * index + 2
        if r < len(self.heap):
            return r
        return None

    def _left(self, index):
        l = 2 * index + 1
        if l < len(self.heap):
            return l
        return None


class HuffmanTree:
    class Node:
        def __init__(self, frequency):
            self.left = None
            self.right = None
            self.frequency = frequency
            self.code = ""
        

    def __init__(self):
        self.letters = []
        self.repetitions = []
        self.root = None

    def set_letters(self, *args):
        for letter in args:
            self.letters.append(letter)

    def set_repetitions(self, *args):
        for frac in args:
            self.repetitions.append(frac)

    def set_text(self, text):
        for char in text:
            if char not in self.letters:
                self.letters.append(char)
                self.repetitions.append(1)
            else:
                index = self.letters.index(char) 
                self.repetitions[index] += 1

    def build_tree(self):
        tree = []
        
        for i in range(len(self.letters)):
            tree.append(HuffmanTree.Node(self.repetitions[i]))

        while len(tree) > 1:
            least = HuffmanTree._find_min(tree)
            tree.remove(least)
            second_least = HuffmanTree._find_min(tree)
            if second_least is not None:
                tree.remove(second_least)
            
            new_Node = HuffmanTree.Node(least.frequency + second_least.frequency)
            new_Node.left = least
            new_Node.right = second_least
            tree.append(new_Node)

        self.root = tree[0]
        

    def get_compressed_length(self):
        HuffmanTree._encode(self.root)
        return HuffmanTree._sum_of_bits(self.root)
        

    def _find_min(tree):
        if len(tree) == 0:
            return None
        min = tree[0]
        for node in tree:
            if node.frequency < min.frequency:
                min = node
        return min
    
    def _encode(root, code = ''):
        if root == None:
            return
        
        root.code = code
        HuffmanTree._encode(root.left, code + '0')
        HuffmanTree._encode(root.right, code + '1')

    def _sum_of_bits(root):
        if root == None:
            return 0
        if root.left == None:
            return root.frequency * len(root.code)
        
        return HuffmanTree._sum_of_bits(root.left) + HuffmanTree._sum_of_bits(root.right)
    

class Bst:
    class Node:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.val = key

    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Bst.Node(key)
        else:
            self._search_insert(self.root, key)

    def _search_insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Bst.Node(key)
            else:
                self._search_insert(root.left, key)
        else:
            if root.right is None:
                root.right = Bst.Node(key)
            else:
                self._search_insert(root.right, key)

    def preorder(self):
        result = []
        Bst._preorder(self.root, result)
        return ' '.join(map(str, result))

    def _preorder(root, result):
        if root:
            result.append(root.val)
            Bst._preorder(root.left, result)
            Bst._preorder(root.right, result)

    def inorder(self):
        result = []
        Bst._inorder(self.root, result)
        return ' '.join(map(str, result))

    def _inorder(root, result):
        if root:
            Bst._inorder(root.left, result)
            result.append(root.val)
            Bst._inorder(root.right, result)

    def postorder(self):
        result = []
        Bst._postorder(self.root, result)
        return ' '.join(map(str, result))

    def _postorder(root, result):
        if root:
            Bst._postorder(root.left, result)
            Bst._postorder(root.right, result)
            result.append(root.val)


class Runner:
    ds_map = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    call_regex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

    def __init__(self, input_src):
        self.input = input_src
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            action_method = getattr(self, action, None)
            if action_method is None:
                return
            action_method(param)

    def make(self, params):
        item_type, item_name = params.split()
        self.items[item_name] = self.ds_map[item_type]()

    def call(self, params):
        regex_res = self.call_regex.match(params)
        item_name, func_name, args_list = regex_res.groups()

        args = [x.strip() for x in args_list.split(',')] if args_list != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[item_name], func_name)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
