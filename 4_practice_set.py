# PRACTICE QUESTIONS FOR CHAPTER 3

""" 1. write a python program to display a user entered name followed by good
afternoon using input () function.

2. Write a program to fill in a letter template given below with name and date

code

letter = '''
         dear  <|Name|>,
         You are selected!
         <|Date|> '''
         
3. Write a program to detect double space in a string
4. Replace the double space from problem 3 with single spaces.
5. Write a program to format the following letter using escape sequence
characters.

letter = "dear Harry, this python course is nice. Thank!"

"""



# 1st code 

 
name = input("what is your name")

print(f"good after noon {name}" )


# 2nd code

letter = '''  dear <|Name|>
 you are selected!
 <|Date|>'''
              
           
print(letter.replace("<|Name|>", "harry").replace("<|Date|>", "24 September 2050"))       


# 3rd code double space detecter code


cat = "i want this  cat  "

print(name.find("  "))