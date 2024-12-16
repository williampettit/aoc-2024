import re

def main():
  with open("./data/3.in") as fh:
    data = fh.read()

  total = 0
  enabled = True
  for groups in re.findall(r"(mul\(([0-9]+),([0-9]+)\))|(do\(\))|(don't\(\))", data):
    if groups[3] == "do()":
      enabled = True
      continue
    
    if groups[4] == "don't()":
      enabled = False
      continue
    
    if enabled:
      a, b = groups[1], groups[2]
      total += int(a) * int(b)
  
  print(total)
    

if __name__ == "__main__":
  main()