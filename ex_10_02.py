name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    else:
       sline = line.split()

       time = sline[5].split(':')
       hour = time[0]
       counts[hour] = counts.get(hour,0) + 1

lst = list()
lst = sorted(counts.items())
for (key,val) in lst:
	print(key,val)
