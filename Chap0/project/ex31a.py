print("True and True")

side = input("~ ")

if side == "true":
    print("It's straight forward.")

elif side == "false":
    print("emm, good try.")
else:
    print("wanna another little game?")


print("1 == 1 and 2 == 1")
answer = input("~ ")

if answer == "true":
    print("interesting!")
elif answer == "false":
    print("off course!")
else:
    print("sight!!")


print("1 == 1 and not('testing' == 1 or 1 == 0)")
mind = input("~ ")

if mind == "true" or mind == "false":
    print("yep! logic!")
else:
    print("back off!")


print("'chunky' == 'bacon' and not(3 == 4 or 3 == 3)")
mind_2 = input("~ ")

if mind_2 == "false":
    print("bravo!")
elif mind_2 == "true":
    print("is that just a guess?")
else:
    print("wanna try again?")
