def assignGrade(grade):
    print grade
    letter = ''
    if grade <= 59:
        letter = 'F'
    elif grade <=69 and grade >=60:
        letter = 'D'

    elif grade <=79 and grade >= 70:
        letter = 'C'

    elif grade <=89 and grade >= 80:
        letter = 'B'

    elif grade <=100 and grade >= 90:
        letter = 'A'

    return letter

#Test Function

for count in range (1,10):
    print "Please enter test score: "
    grade = input()
    print "You Letter Grade is %s" % (assignGrade(grade))
