with open('prac1_text.txt', 'w') as f:
    f.write('Hello, world!\n')

with open('prac2_text.txt', 'r') as f:
    contents = f.read()
    print(contents)

with open('prac1_text.txt', 'a') as f:
    f.write('This is a new line.\n')

with open('prac1_text.txt', 'r') as f:
    contents = f.read()
    print(contents)
