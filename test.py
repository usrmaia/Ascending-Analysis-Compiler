list1 = [
  {1: "a"},
  {2: "b"}
]

new_list = [
  {0: "!"}
]

new_list.extend(list1)
print(new_list)