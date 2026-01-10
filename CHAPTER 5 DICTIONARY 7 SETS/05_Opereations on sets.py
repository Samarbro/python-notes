# Consider the following set:


s = {1, 8, 2, 3}

'''


* lens(s): Returns 4, the length of the set
* s.remove(8): Updates the set s and removes 8 from s.
* s.pop(): Removes an arbitrary element from the set and return the element
   removed.
• s.clear():empties the set s.
• s.union({8,11}): Returns a new set with all items from both sets. {1,8,2,3,11}.
• s.intersection({8,11}): Return a set which contains only item in both sets {8}.



'''


# example of union

s1 = {1, 45, 6}
s2 = {7, 8, 1, 78}


print(s1.union(s2))
print(s1,intersection(s2))