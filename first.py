python_course = True
java_course = False
int(python_course) == 1
int(java_course) == 0
str(python_course) == "True"

number = 5
print(f"index is {number}")
print("another index is {0}+{1}={2}".format(number, number, (number + number)))

if number:
    print("number is 5")
else:
    print("number is not 5")
