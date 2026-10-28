markbach = float(input("What's your bachillerato mark?"))
mark1 = float(input("What is the mark of the first core suject"))
mark2 = float(input("What is the mark of the second core suject"))
mark3 = float(input("What is the mark of the third core suject"))
mark4 = float(input("What is the mark of the fourth core suject"))
secondarymark = float(input("How many specific subjects did you take?"))
if secondarymark == 1:
    mark5 = float(input("What did you get in the specific subject?"))
if secondarymark == 2:
    mark5 = float(input("What did you get in the first specific subject?"))
    mark6 = float(input("What did you get in the second specific subject?"))

if secondarymark == 1:
    howmuch1 = float(input("Did that subject have a 0.1, 0.15 or 0.2 weighting?"))
if secondarymark == 2:
    howmuch1 = float(input("Did the firts subject have a 0.1, 0.15 or 0.2 weighting?"))
    howmuch2 = float(input("Did the second subject have a 0.1, 0.15 or 0.2 weighting?"))
if secondarymark == 2:
    result = ((mark1 + mark2 + mark3 + mark4)/4)*0.4 + (mark5*howmuch1) + (mark6*howmuch2) + (markbach*0.6)
elif secondarymark == 1:
    result = ((mark1 + mark2 + mark3 + mark4)/4)*0.4 + (mark5*howmuch1) + (markbach*0.6)
elif secondarymark == 0:
    result = ((mark1 + mark2 + mark3 + mark4)/4)*0.4 + (markbach*0.6)
print(result)

    



