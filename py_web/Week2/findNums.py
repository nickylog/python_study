import re

fhand = open('regex_sum_1450903.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    xlist = re.findall('[0-9]+', line)
    if len(xlist) > 0:
        for x in xlist:
            count += int(x)
print("count=", count)