directions = [
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

  all_letter_a_locations: set[tuple[int, int]] = set()
  total = 0

  for x in range(max_x):
    for y in range(max_y):
      if array[x][y] != "M":
        continue
      
      for (x_step, y_step) in directions:
        final_x = x + x_step * 2
        final_y = y + y_step * 2
        if (final_y < 0 or final_y >= max_y) or (final_x < 0 or final_x >= max_x):
          continue

        candidate = ""
        for i in range(3):
          candidate += array[x + i * x_step][y + i * y_step]
          
          if not "MAS".startswith(candidate):
            break
        
        if candidate == "MAS":
          letter_a_location = (x + x_step, y + y_step)
          
          if letter_a_location in all_letter_a_locations:
            total += 1
          else:
            all_letter_a_locations.add(letter_a_location)
  
  print(total)
    
if __name__ == "__main__":
  main()