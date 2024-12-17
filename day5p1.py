def main():
  with open("./data/5.in") as fh:
    lines = fh.readlines()

  rules: dict[int, list[int]] = {}
  updates: list[list[int]] = []

  for line in lines:
    line = line.strip()
    if line == "":
      continue
    
    if "|" in line:
      a, b = line.split("|")
      a = int(a)
      b = int(b)
      if a not in rules:
        rules[a] = []
      rules[a].append(b)
    elif "," in line:
      pages = line.split(",")
      updates.append([int(page) for page in pages])
    
  total = 0
  for update in updates:
    seen: list[int] = []
    update_is_valid = True
    for num in update:
      seen.append(num)
      for b in rules[num]:
        if b in seen:
          update_is_valid = False
          break
      if not update_is_valid:
        break
    if update_is_valid:
      total += update[len(update) // 2]
  
  print(total)

if __name__ == "__main__":
  main()
