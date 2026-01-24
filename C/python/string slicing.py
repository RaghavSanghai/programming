s1="Hello World"

'''
Syntax for indexing: string_name[index]
Syntax for slicing: string_name[start_index : end_index : step]
start_index : The starting index from where the slice begins (inclusive).
end_index : The ending index where the slice ends (exclusive).
step : The step value determines the increment between each index for slicing. Default is 1.
''' 
print(s1[2:7:1])  #output: llo W
print(s1[0:5])    #output: Hello
print(s1[:5])     #output: Hello
print(s1[6:])     #output: World
print(s1[:])      #output: Hello World
print(s1[::2])    #output: HloWrd
print(s1[::-1])   #output: dlroW olleH (reverses the string)
print(s1[7:2:-1]) #output: o ll (slices from index 7 to 3 in reverse)
print(s1[-1:-6:-1]) #output: dlroW (slices from last index to 6th last index in reverse)
print(s1[-6:])    #output: World (slices from 6th last index to end) 
print(s1[:-6])    #output: Hello (slices from start to 6th last index) 
print(s1[-3:-8:-1]) #output: roW o (slices from 3rd last index to 8th last index in reverse)
print(s1[-8:-3])  #output: o Wor (slices from 8th last index to 3rd last index)
# Note: In slicing, if start_index is greater than end_index and step is positive, the result will be an empty string.
# Similarly, if start_index is less than end_index and step is negative, the result will also be an empty string.