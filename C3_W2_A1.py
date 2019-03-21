import re

fname = input("Enter file name: ")
handle = open(fname)

numlist = list()
for line in handle:
    line = line.rstrip()
    nums = re.findall('[0-9]+',line)
    if len(nums) < 1 : continue
    else:
        numlist = numlist + nums
#print(numlist)
print(sum(int(i) for i in numlist))
