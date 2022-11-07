import itertools 

#  *** FUNCTION 1 | LIST_SAYER | DECLARATIONS ***
empty_list = []
my_list = [10, 11, 21, 31, 41, 51, 61, 71]

#  *** FUNCTION 2 | DICT_SAYER  | DECLARATIONS ***
empty_dict = {}
full_dict = {"Tree" : "Madrone", "Fruit": "Persimmon", "Seed": "Chestnut"}

#  *** FUNCTION 3 | GREATEST | DECLARATIONS ***
too_many_wheels = {"Tractor Wheels": 4, "Van Wheels": 4, "Bus Wheels": 6, "Bike Wheels": 2, "Burley Wheels": 2}

#  *** FUNCTION 4 | ZIPPER | DECLARATIONS ***
same_list1 = ["dogwood", "peach", "pear", "pawpaw"]
same_list2 = ["flower", "fruit", "cider ingredient", "northern tropical relative"]
diff_list1 = ["wooly bear", "fox", "bear"]
diff_list2 = ["caterpillar", "stinkbug"]
zipped_dict = {}
zipped_tuple = ()

#  *** FUNCTION 1 | LIST_SAYER ***
def list_sayer(list):
  if len(list) > 0:
    for item in list:
      print(f"Index: {list.index(item)} has value: {item}") 
    return True
  else:
    print("This list is empty")
    return False

#  *** FUNCTION 2 | DICT_SAYER ***
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

#  *** FUNCTION 3 | GREATEST ***
def greatest(dictionary):
  highest_value = max(dictionary, key=dictionary.get)
  highest_tuple = (highest_value, dictionary[highest_value])
  return highest_tuple
  
#  *** FUNCTION 4 | ZIPPER ***
def zipper(list1, list2):
  if len(list1) == len(list2):
    for (list_item_1, list_item_2) in zip(list1, list2):
      dict_item =  {list_item_1: list_item_2}
      zipped_dict.update(dict_item)
    return zipped_dict
  
  else:
    zipped_tuple = (list1, len(list1), list2, len(list2))
    return zipped_tuple


#  *** FUNCTION 1 | LIST SAYER | FUNCTION CALL***
list_sayer(empty_list)
list_sayer(my_list)

#  *** FUNCTION 2 | DICT_SAYER | FUNCTION CALL***
dict_sayer(empty_dict)
dict_sayer(full_dict)

#  *** FUNCTION 3 | GREATEST | FUNCTION CALL ***
greatest(too_many_wheels)

#  *** FUNCTION 4 | ZIPPER | FUNCTION CALL***
zipper(same_list1, same_list2)
zipper(diff_list1, diff_list2)























