marks1={"maths":88.5, "eng": 76.0, "phy":80.0}
#fetch the marks of phy
print(marks1["phy"])  # Output: 80.0
print(marks1["chem"])  # Output: Error: KeyError: 'chem' (the key "chem" does not exist in the dictionary)

#get()
print(marks1.get("phy"))  # Output: 80.0
print(marks1.get("chem"))  # Output: None (the key "chem" does not exist in the dictionary, but get() returns None instead of raising an error)

#in not in operator
print(76.0 in marks1)  # Output: False (76.0 is a value in the dictionary, but we are checking for the presence of the value, not the key)
print("eng" in marks1)  # Output: True (the key "eng" exists in the dictionary)

#update()
marks2={"chem":81.5, "bio": 90.5}
marks1.update(marks2)
print(marks1)  # Output: {'maths': 88.5, 'eng': 76.0, 'phy': 80.0, 'chem': 81.5, 'bio': 90.5}

#pop()
marks1.pop("maths")
print(marks1)  # Output: {'eng': 76.0, 'phy': 80.0, 'chem': 81.5, 'bio': 90.5}

m1={"milk":60, "rice":100, "biscuits":20, "milk":65}
print(m1)  # Output: {'milk': 65, 'rice': 100, 'biscuits': 20} (the key "milk" is duplicated, but only the last value (65) is retained in the dictionary, as keys must be unique)

d1={[1, 3, 5]: 9, [1,2,1]: 4}
print(d1)  # Output: Error: TypeError: unhashable type: 'list' (lists cannot be used as keys in a dictionary because they are mutable and unhashable)

#not allowed keys -> lists, sets, dictionaries (mutable and unhashable types)
#allowed keys -> int, float, string, tuple (immutable and hashable types)
#keys of dictionary can only be immutable datatypes
#values of dictionary can be of any datatype (mutable or immutable)

st={"id": 1001, "name": "John", "marks": [89.5, 71.5, 81.0]}
print(st["marks"])  # Output: [89.5, 71.5, 81.0] (the value associated with the key "marks" is a list containing the marks of the student in different subjects)
print(st["marks"][0])  # Output: 89.5 (accessing the first element of the list associated with the key "marks")

st1= {"id": 1001, "name": "John", "marks": {"eng": 89.5, "bio": 81.0}}
print(st1["marks"])  # Output: {'eng': 89.5, 'bio': 81.0} (the value associated with the key "marks" is a nested dictionary containing the marks of the student in different subjects)
print(st1["marks"]["eng"])  # Output: 89.5 (accessing the value associated with the key "eng" in the nested dictionary "marks")

st2= {"id": 1001, "name": "John", "marks": {"eng": 89.5, "maths": 71.5}}
#fetch the keys -> keys() method
print(st2.keys())  # Output: dict_keys(['id', 'name', 'marks']) (returns a view object containing the keys of the dictionary)
#fetch the values -> values() method
print(st2.values())  # Output: dict_values([1001, 'John', {'eng': 89.5, 'maths': 71.5}]) (returns a view object containing the values of the dictionary)
#fetch the key-value pairs -> items() method
print(st2.items())  # Output: dict_items([('id', 1001), ('name', 'John'), ('marks', {'eng': 89.5, 'maths': 71.5})]) (returns a view object containing the key-value pairs of the dictionary