import itertools 

#  *** FUNCTION 1 | LIST_SAYER ***

empty_list = []
my_list = [10, 11, 21, 31, 41, 51, 61, 71]
def list_sayer(list):
  if len(list) > 0:
    for item in list:
      print(f"Index: {list.index(item)} has value: {item}") 
    return True
  else:
    print("This list is empty")
    return False

list_sayer(empty_list)
list_sayer(my_list)


#  *** FUNCTION 2 | DICT_SAYER ***

empty_dict = {}
full_dict = {"Tree" : "Madrone", "Fruit": "Persimmon", "Seed": "Chestnut"}

def dict_sayer(dictionary):
  if len(dictionary) == 0:
    print("This dictionary is empty")
    return False
  elif len(dictionary) > 0:
    print(f"Here are all the items in your dictionary.. ")
    for key, value in dictionary.items():
        print(f"Key: '{key}', Value: '{value}'")
    return True    
  else:
    print("I don't know what's going on but I taking your dictionary into the shop, I've never seen this before.")  

dict_sayer(empty_dict)
dict_sayer(full_dict)


#  *** FUNCTION 3 | GREATEST ***

too_many_wheels = {"Tractor Wheels": 4, "Van Wheels": 4, "Bus Wheels": 6, "Bike Wheels": 2, "Burley Wheels": 2}

def greatest(dictionary):
  highest_value = max(dictionary, key=dictionary.get)
  highest_tuple = (highest_value, too_many_wheels[highest_value])
  return highest_tuple
  
greatest(too_many_wheels)


#  *** FUNCTION 4 | ZIPPER ***

same_list1 = ["dogwood", "peach", "pear", "pawpaw"]
same_list2 = ["flower", "fruit", "cider ingredient", "northern tropical relative"]
diff_list1 = ["wooly bear", "fox", "bear"]
diff_list2 = ["caterpillar", "stinkbug"]
zipped_dict = {}
zipped_tuple = ()

def zipper(list1, list2):
  if len(list1) == len(list2):
    for (list_item_1, list_item_2) in zip(list1, list2):
      dict_item =  {list_item_1: list_item_2}
      zipped_dict.update(dict_item)
    return zipped_dict
  
  else:
    zipped_tuple = (list1, len(list1), list2, len(list2))
    return zipped_tuple

zipper(same_list1, same_list2)
zipper(diff_list1, diff_list2)
























