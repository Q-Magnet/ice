import os
import sys


v = '1.0'
prompt = f'Ice-{v}:'
vars = {}
filepath = input('File>')
with open(filepath,'r') as file:
    content = file.read().split('\n')
for Input in content:
    s = '__UnSet__'
    si = []
    #Input = input(prompt)
    for i in range(len(Input)):
        if Input[i] == ' ':
            s = Input[:i]
            si = [s]
            for j in Input[i+1:].split(','):
                si.append(j)
            break
    if s == '__UnSet__':
        s = Input
        si = [s]
    
    # Special
    if s == 'C':
        'comment' == 'comment'
    elif s == 'finish':
        exit()
    # Output
    elif s == 'print':
        print(si[1], end='')
    elif s == 'printv':
        print(vars[si[1]], end='')
    elif s == 'nl':
        print('')
    # Set Var
    elif s == 'set':
        vars[si[1]] = si[2]
    elif s == 'setinput':
        vars[si[1]] = input(si[2])
    # Math
    elif s == 'add':
        if si[1] in vars:
            if si[2] in vars:
                out = int(vars[si[1]]) + int(vars[si[2]])
            else:
                out = int(vars[si[1]]) + int(si[2])
        else:
            if si[2] in vars:
                out = int(si[1]) + int(vars[si[2]])
            else:
                out = int(si[1]) + int(si[2])
        vars[si[3]] = str(out)

    # System
    elif s.isspace():
        print()
    elif s == 'END':
        print('Exitted Successfully with "END" command')
        sys.exit()
    else:
        print(s + ' is not defined')