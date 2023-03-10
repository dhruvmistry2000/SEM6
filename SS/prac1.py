# create a file
with open('example.txt', 'w') as f:
    f.write('Hello, world!\n')

# read from the file
with open('example.txt', 'r') as f:
    contents = f.read()
    print(contents)

# write to the file
with open('example.txt', 'a') as f:
    f.write('This is a new line.\n')

# read from the file again
with open('example.txt', 'r') as f:
    contents = f.read()
    print(contents)
