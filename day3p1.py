import re

def main():
  with open("./data/3.in") as fh:
    data = fh.read()

  total = 0
  for (a, b) in re.findall(r"mul\(([0-9]+),([0-9]+)\)", data):
    total += int(a) * int(b)
  print(total)
    

if __name__ == "__main__":
  main()