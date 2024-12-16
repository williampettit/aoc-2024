directions = [
  (+0, -1),
  (+1, +0),
  (+0, +1),
  (-1, +0),
  (+1, -1),
  (+1, +1),
  (-1, +1),
  (-1, -1),
]

def main():
  with open("./data/4.in") as fh:
    lines = fh.readlines()

  array: list[list[str]] = []
  for line in lines:
    array.append(list(line.strip()))

  max_x = len(array)
  max_y = len(array[0])
  total = 0
  
  for x in range(max_x):
    for y in range(max_y):
      if array[x][y] != "X":
        continue
      
      for x_step, y_step in directions:
        final_x = x + x_step * 3
        final_y = y + y_step * 3
        if (final_y < 0 or final_y >= max_y) or (final_x < 0 or final_x >= max_x):
          continue

        candidate = ""
        for i in range(4):
          candidate += array[x + i * x_step][y + i * y_step]
          
          if not "XMAS".startswith(candidate):
            break
        
        if candidate == "XMAS":
          total += 1
        
  print(total)
    
if __name__ == "__main__":
  main()