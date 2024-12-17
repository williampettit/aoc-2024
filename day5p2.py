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
    
    # p2 cares about invalud entries
    if not update_is_valid:
      temp: list[int] = []
      for i, num in enumerate(update):
        if i == 0:
          temp.append(num)
          continue

        # num has to be before every b
        # so pick the minimum idx of any b already in temp
        # or default to inserting at end
        new_idx = i
        for b in rules[num]:
          if b in temp:
            b_idx = temp.index(b)
            if b_idx < new_idx:
              new_idx = b_idx
        temp.insert(new_idx, num)
      
      # accumulate middle entries
      total += temp[len(temp) // 2]
  
  print(total)

if __name__ == "__main__":
  main()
