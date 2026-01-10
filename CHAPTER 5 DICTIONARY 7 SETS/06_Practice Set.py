# HERE IS SOME PRACTICE QUESTIONS.

'''

1. Write program to create a dictionary of hindi words with values as their English
translation. Provide user with an option to look it up!

2. Write a program to input eight numbers from the user and display all the unique
numbers (once).

3. Can we have a set with 18 (int) and '18' (str) as a value in it?
4. What will be the length of following set s:
 
 s = set()
 s.add(20)
 s.add(20.0)
 s.add('20')

5. s = {}
   
what is the type of 's'?

6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the name are unique.

7. If the names of 2 friends are same; what will happen to the program in problem 6?

8. If language of two friends are same; what will happen to the program in problem 6?.

9. Can you change the values inside a list which is contained in set S?
  
    s = {8, 7, 12, "Harry", [1,2]}



'''



# Problem 1 ( Write program to create a dictionary of hindi words with values as their English
# translation. Provide user with an option to look it up! )

'''                             here is code for problem (1)

words = {
    " madad": "help",
    "chor dena": "forgive",
    "nevermind": "koi baat nahi",
}

word = input("enter the word you want meaning of: ")

print(words[word])


'''


# Problem 2 ( write a program to input eight numbers from the user and display all the unique numbers (once) )

'''   here is code of Problem (2) 


n = set()

s = input("enter number: ")
n.add(int(s))
s = input("enter number: ")
n.add(int(s))
s = input("enter number: ")
n.add(int(s))
s = input("enter number: ")
n.add(int(s))
s = input("enter number: ")
n.add(int(s))
s = input("enter number: ")
n.add(int(s))
s = input("enter number: ")
n.add(int(s))
s = input("enter number: ")
n.add(int(s))

print(n)



'''          





# Problem (3) Can we have a set with 18 (int) and '18' (str) as a value in it?


# s = set()
 
# s.add("18")
# s.add(18)
 
 
# print(s)





# problem (4)   What will be the length of following set s:
 
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20')

# print(len(s))


# Problem (5)  5. s = {}
   
# what is the type of 's'?


# s = {}

# print(type(s))






# Problem (6)  Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the name are unique.



d = {}

name = input(" Enter friends name: ")
lang = input(" Enter language name: ")

d.update({name: lang})
name = input(" Enter friends name: ")
lang = input(" Enter language name: ")

d.update({name: lang})
name = input(" Enter friends name: ")
lang = input(" Enter language name: ")

d.update({name: lang})
name = input(" Enter friends name: ")
lang = input(" Enter language name: ")

d.update({name: lang})

print(d)