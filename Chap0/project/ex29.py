people = 20
cats = 30
dogs = 15
# by using if to valuate the result. the result of line 5, true, consist with the setting.
if people < cats:
    print("Too many cats! The world is doomed!")
# line 8 false so the printout is banned.
if people > cats:
    print("Not many cats! The world is saved!")
# false to not printout
if people < dogs:
    print("The world is drooled on!")
# true to print out the string.
if people > dogs:
    print("The world is dry!")

# now the amount of dogs is 15 + 5 == 20, so all three assumptions are true to the setting.
dogs += 5
# in other words, the original values affect the result, the modification of values will switch the output.
if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    # explaination of if, indent.
    print("people are less than or equeal to dogs.")

if people == dogs:
    print("people are dogs.")

if cats > dogs:
    print("doggy, who is the king of world?")
    
