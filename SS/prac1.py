with open('example.txt', 'w') as f:
    f.write('Hello, world!\n')

with open('example.txt', 'r') as f:
    contents = f.read()
    print(contents)

with open('example.txt', 'a') as f:
    f.write('This is a new line.\n')

with open('example.txt', 'r') as f:
    contents = f.read()
    print(contents)
