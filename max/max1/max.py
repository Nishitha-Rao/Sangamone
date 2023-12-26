def find_maximum():
  list1=[27,15,8,1,64]
  max_val = list1[0]
  for num in list1:
    if num > max_val:
      max_val = num
  return max_val