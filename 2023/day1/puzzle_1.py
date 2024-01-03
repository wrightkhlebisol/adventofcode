#!/usr/bin/python3
import sys

file_name = sys.argv[1]
sum_star = 0


with open(file_name, 'r') as f:
    lines = f.readlines()
    line_list = []

    for line in lines:
        last_int = None
        first_int = None
        joined_int = None
        line_list = list(line)

        for i in range(len(line_list)):
            if line_list[i].isdigit() and first_int is None:
                first_int = line_list[i]

                if last_int is not None:
                    break

            if line_list[len(line_list) - 1 - i].isdigit() and last_int is None:
                last_int = line_list[len(line_list) - 1 - i]

                if first_int is not None:
                    break

        joined_int = first_int + last_int
        sum_star += int(joined_int)

print(sum_star)
