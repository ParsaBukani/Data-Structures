import sys
import re


class Queue:
    def __init__(self):
        self.queue = []  
        self.head = 0 
        self.tail = 0 

    def enqueue(self, value):
        self.queue.append(value)
        self.tail += 1

    def dequeue(self):
        value = self.queue[self.head]
        self.head += 1
        return value

    def size(self):
        return self.tail - self.head

    def empty(self):
        return self.head == self.tail

    def one_line_str(self):
        return ' '.join(str(x) for x in self.queue[self.head:self.tail])


class Stack:
    def __init__(self, capacity=10):
        self.stack = []  
        self.top = -1  
        self._capacity = capacity

    def push(self, value):
        self.stack.append(value)  
        self.top += 1 

    def pop(self):
        value = self.stack.pop()  
        self.top -= 1  
        return value  

    def put(self, value):
        self.stack[self.top] = value

    def peek(self):
        return self.stack[self.top]

    def expand(self):
        self._capacity *= 2

    def capacity(self):
        return self._capacity

    def size(self):
        return self.top + 1  

    def empty(self):
        return self.top == -1

    def one_line_str(self):
        return ' '.join(str(x) for x in self.stack)


class Node:
    def __init__(self, value):
        self.value = value    
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_back(self, value):
        new_node = Node(value)

        last_pointer = self.head
        while True:
            if last_pointer == None:
                self.head = new_node
                break
            elif last_pointer.next == None:
                last_pointer.next = new_node
                break
            last_pointer = last_pointer.next

    def reverse(self):
        prev = None  
        current = self.head  
        while current:    
            next_node = current.next   
            current.next = prev    
            prev = current    
            current = next_node  
        self.head = prev

    def one_line_str(self):
        current = self.head
        line = ''
        while current != None:
            line += str(current.value) + ' '
            current = current.next
        return line


class Runner:
    ds_map = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    call_regex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

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
        args = args_list.split(',') if args_list != '' else []

        method = getattr(self.items[item_name], func_name)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
