vocabulary = {
    'object': 'Class example',
    'source_code': 'The raw code written by the programmer',
    'Variable': 'A container used to store data during program execution',
    'Function': 'A block of code defining a series of operations',
    'Algorithm': 'A series of steps defined to solve a specific '
    'problem or perform a task',
    'Set': '独一无二的元素',
}

for key, value in vocabulary.items():
    print(f"术语是{key.title()}, 解释是{value.lower()}.")
