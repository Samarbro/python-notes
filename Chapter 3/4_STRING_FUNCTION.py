""" some of the commonly used functions to perform 
operation on or manipulate strings are as follows. 
let us assume there is a string 'str' as follows: """



str = 'harry'
print(len(str)) # Output: 5


# now when operated on this string 'str' these functions do the following

# len() function - This function returns the length of the strings.

#___________________________________________________

""" 2.   String.endswith("rry") - This function_tells 
whether the variable string ends with the string "rry" or not.
If string is "harry", it returns true for 'rry' since Harry ends with rry.
"""

str = "harry"
print(str.endswith("rry"))  # output : true



""" 3. string.count("c") - counts the total numbers of occurrences of any character."""

str = "harry"
count = str.count("rry")
print(count)  # output : 2


# 4. the first character of a given string.


str = "harry"
capitalized_string = str.capitalize()
print(capitalized_string) # output "harry"


# 5. string.find(word) - This function friends a word and return the index of first occurrence of that word in the  string.

str = "harry"

index = str.find("rry")
print(index) # Output: 2 

""" 6. string.replace (old word , new word) - This function replace 
the old word with new word in the entire string. """

str = "harry"
replaced_string = str.replace("r", "1")
print(replaced_string)  # output: €"hally"