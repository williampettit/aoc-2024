with open("./data/1.in") as fh:
  lines = fh.readlines()

l1, l2 = [], []
for line in lines:
  a, b = line.split()
  l1.append(int(a))
  l2.append(int(b))

assert len(l1) == len(l2)
l1.sort(); l2.sort()
total = 0
for i in range(len(l1)):
  total += abs(l1[i] - l2[i])

print(total)