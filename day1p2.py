with open("./data/1.in") as fh:
  lines = fh.readlines()

l1, l2 = [], []
for line in lines:
  a, b = line.split()
  l1.append(int(a))
  l2.append(int(b))

assert len(l1) == len(l2)
total = 0
for num in l1:
  total += num * l2.count(num)

print(total)