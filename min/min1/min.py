def find_minimum():
  list1=[10,55,2,4,6]
  min_val = list1[0]
  for num in list1:
    if num < min_val:
      min_val = num
  return min_val