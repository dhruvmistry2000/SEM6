import re

# read in the input file
with open('prac2_input.c', 'r') as f:
    contents = f.read()

# remove single-line comments (//)
contents = re.sub('//.*?\n', '\n', contents)

# remove multi-line comments (/* ... */)
contents = re.sub('/\*.*?\*/', '', contents, flags=re.DOTALL)

# write the result to the output file
with open('prac2_output.c', 'w') as f:
    f.write(contents)
