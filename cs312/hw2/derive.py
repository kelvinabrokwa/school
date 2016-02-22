#!/usr/bin/env python3

import sys

def derive():

    n, grammar_file = parse_arguments()

    grammar, start_symbol = parse_grammar_file(grammar_file)

    worklist = [start_symbol] # used as stack

    while len(worklist) > 0:
        s = worklist.pop()
        if len(s.split(' ')) > n:
            continue
        if has_no_nonterms(s, grammar):
            print(s)
            continue
        nt_idx = find_leftmost_nonterm(s, grammar)
        nt = s.split(' ')[nt_idx]
        for prod in grammar[nt]:
            tmp = s.split(' ')
            tmp[nt_idx] = prod
            worklist.append(' '.join(tmp))

def find_leftmost_nonterm(s, grammar):
    s = s.split(' ')
    for i in range(len(s)):
        if s[i] in grammar:
            return i
    return None

def has_no_nonterms(s, grammar):
    s = s.split(' ')
    for sym in s:
        if sym in grammar:
            return False
    return True

def parse_arguments():
    n = 3 # default length

    if len(sys.argv) == 2:
        grammar_file = sys.argv[1]
    elif len(sys.argv) > 2:
        n = int(sys.argv[1][2:])
        grammar_file = sys.argv[2]
    else:
        print('incorrect command line arguments')
        sys.exit(1)

    return n, grammar_file

def parse_grammar_file(grammar_file):
    dic = {}
    start = None
    with open(grammar_file) as f:
        for line in f:
            line = line.strip().split(' ')
            if start == None:
                start = line[0]
            key = line[0]
            if key not in dic:
                dic[key] = []
            dic[key].append(' '.join(line[2:]))
    return dic, start

if __name__ == '__main__':
    derive()
