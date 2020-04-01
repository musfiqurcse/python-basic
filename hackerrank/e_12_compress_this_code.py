import fileinput
from itertools import groupby
if __name__ == "__main__":
    for line in fileinput.input():
        group_item = []
        item = []
        for k,g in groupby(line):
            item.append("({0}, {1})".format(len(list(g)),k))
        print(" ".join(item))
