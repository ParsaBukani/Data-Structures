import sys
import re


class Node:
    def __init__(self, name, line_number, children=None):
        self.name = name
        self.line_number = line_number
        self.children = {} if children is None else children

    def add_child(self, node):
        unique_entry = f'{node.name}#{node.line_number}'
        self.children[unique_entry] = node


class ProgramNode(Node):
    pass


class FunctionDeclaration(Node):
    pass


class IfStatement(Node):
    pass


class SimpleStatement(Node):
    pass


def print_result(program_node):
    condition_counter = 1
    queue = []

    def build_queue(node, queue):
        for function in node.children.values():
                function.name += '()' 
                queue.append(function)
                add_condition_to_queue(function, queue)

    def add_condition_to_queue(node, queue):
        nonlocal condition_counter

        for child in node.children.values():
            if isinstance(child, IfStatement):
                child.name = f'condition_{condition_counter}()'
                queue.append(child)
                condition_counter += 1

        for child in node.children.values():
            if isinstance(child, IfStatement):
                add_condition_to_queue(child, queue)

    def print_item(node):
        print(f'\ndef {node.name}:')
        for child in node.children.values():
            print(f'  {child.name}')


    build_queue(program_node, queue)
    for item in queue:
        print_item(item)


class Handler:
    def __init__(self):
        self.program = ProgramNode('program', 0)
        self.stack = []

    def function(self, name, line_number):
        new_node = FunctionDeclaration(name, line_number)
        self.program.add_child(new_node)
        self.stack.append(new_node)

    def condition(self, line_number):
        new_node = IfStatement('condition', line_number)
        self.stack[-1].add_child(new_node)
        self.stack.append(new_node)

    def statement(self, name, line_number):
        new_node = SimpleStatement(name, line_number)
        self.stack[-1].add_child(new_node)

    def endscope(self):
        self.stack.pop()


class Runner:
    func_regex = re.compile(r'^def (\w+)\(\):$')
    if_regex = re.compile(r'^if True:$')
    statement_regex = re.compile(r'^(\w+)$')
    endscope_regex = re.compile(r'^# end_scope$')

    def __init__(self, input_src):
        self.input = input_src
        self.handler = Handler()

    def run(self):
        for i, line in enumerate(self.input):
            line = line.strip()
            if not line:
                continue

            match_func = self.func_regex.match(line)
            match_if = self.if_regex.match(line)
            match_statement = self.statement_regex.match(line)
            match_endscope = self.endscope_regex.match(line)

            if match_func:
                name = match_func.group(1)
                self.handler.function(name, i)
            elif match_if:
                self.handler.condition(i)
            elif match_statement:
                name = match_statement.group(1)
                self.handler.statement(name, i)
            elif match_endscope:
                self.handler.endscope()
            else:
                print('Invalid syntax', file=sys.stderr)

        print_result(self.handler.program)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == '__main__':
    main()
