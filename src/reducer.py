#!/usr/bin/env python

import sys
from operator import itemgetter

prev_index = None
value_list = []
run_activation = int(sys.argv[1])

for line in sys.stdin:
    curr_index, index, value = line.rstrip().split("\t")
    index, value = int(index), float(value)
    if curr_index == prev_index:
        value_list.append((index,value))
    else:
        if prev_index:
            value_list = sorted(value_list,key=itemgetter(0))
            i = 0
            result = 0
            while i < len(value_list) - 1:
                if value_list[i][0] == value_list[i + 1][0]:
                    result += value_list[i][1]*value_list[i + 1][1]
                    i += 2
                else:
                    i += 1

            if run_activation == 1:
                result = max(0, result)

            print (f"A,{prev_index},{result}")

        prev_index = curr_index
        value_list = [(index,value)]

if curr_index == prev_index:
    value_list = sorted(value_list,key=itemgetter(0))
    i = 0
    result = 0
    while i < len(value_list) - 1:
        if value_list[i][0] == value_list[i + 1][0]:
            result += value_list[i][1]*value_list[i + 1][1]
            i += 2
        else:
            i += 1

    if run_activation == 1:
        result = max(0, result)

    print (f"A,{prev_index},{result}")