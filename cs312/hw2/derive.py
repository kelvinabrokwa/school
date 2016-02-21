#!/usr/bin/env python3

import sys

def derive():
    n = 3 # default length

    # parse command line arguments
    if len(sys.argv):
        grammar_file = sys.argv[1]
    if len(sys.argv) > 2:
        n = int(sys.argv[1][2:])
        grammar_file = sys.argv[2]

    grammar, start_symbol = parse_grammar_file(grammar_file)

    worklist = [start_symbol] # used as stack

    while len(worklist) > 0:
        break

def parse_grammar_file(grammar_file):
    dic = {}
    start = None
    with open(grammar_file) as f:
        for line in f:
            line = line.strip().split(' ')
            if start == None:
                start = line[0]
            s = line[0]
            t = ' '.join(line[2:])
            if s not in dic:
                dic[s] = []
            dic[s].append(t)
    return dic, start

if __name__ == '__main__':
    derive()
