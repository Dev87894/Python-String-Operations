# Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
# import time
# current_date = time.localtime()
# date = time.strftime("%D", current_date)
# Name = "Devesh"

# print("Dear",Name,"\nYou are selected! \n",date)

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("Name","Devesh").replace("Date","9 July 2026"))