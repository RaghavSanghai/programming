num = {1, 3, 2, 0, -1}

#in not in operator
print(1 in num)  # Output: True
print(5 in num)  # Output: False
print(-1 in num)  # Output: True
print(0 not in num)  # Output: False
print(4 not in num)  # Output: True

#concatenation of sets
s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1 + s2)  # Output: Error: unsupported operand type(s) for +: 'set' and 'set'


#repetition of sets
s1 = {1, 2, 3}
print(s1 * 2)  # Output: Error: unsupported operand type(s) for *: 'set' and 'int'

s1 = {2, 0, -1}
print(s1)  # Output: {0, 2, -1} (sets are unordered, so the output may vary)
s1.add(3)
print(s1)  # Output: {0, 2, 3, -1} (the new element 3 is added to the set)
s1.remove(0)
print(s1)  # Output: {2, 3, -1} (the element 0 is removed from the set)
s1.add(2)
print(s1)  # Output: {2, 3, -1} (the duplicate element 2 is ignored)
s1.remove(5)  # Output: Error: KeyError: 5 (the element 5 is not in the set)
s1.discard(5)  # Output: No error, the element 5 is not in the set, but discard does not raise an error
print(s1)  # Output: {2, 3, -1} (the set remains unchanged)

#intersection of sets
#if there is no common element between the sets, the result will be an empty set
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 & s2)  # Output: {3, 4} (the common elements between s1 and s2)
print(s1.intersection(s2))  # Output: {3, 4} (the common elements between s1 and s2)

#union of sets
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 | s2)  # Output: {1, 2, 3, 4, 5, 6} (all unique elements from both sets)
print(s1.union(s2))  # Output: {1, 2, 3, 4, 5, 6} (all unique elements from both sets)

#difference of sets
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 - s2)  # Output: {1, 2} (elements that are in s1 but not in s2)
print(s1.difference(s2))  # Output: {1, 2} (elements that are in s1 but not in s2)
