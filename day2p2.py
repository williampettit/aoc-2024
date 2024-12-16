def is_safe(nums: list[int]) -> bool:
  if nums[0] > nums[1]:
    nums.reverse()
  
  for i in range(len(nums) - 1):
    curr_num = nums[i]
    next_num = nums[i + 1]
    if next_num <= curr_num:
      return False
    if next_num - 3 > curr_num:
      return False
  return True

def main():
  with open("./data/2.in") as fh:
    lines = fh.readlines()

  total_safe = 0
  for line in lines:
    nums = line.split()
    nums = [int(x) for x in nums]
    
    if is_safe(nums):
      total_safe += 1
    else:
      for i in range(len(nums)):
        temp = nums.copy()
        temp.pop(i)
        if is_safe(temp):
          total_safe += 1
          break
  
  print(total_safe)

if __name__ == "__main__":
  main()