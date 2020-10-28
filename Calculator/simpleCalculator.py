import regex

print ("Calculadora")
print("Type 'quit' to exit\n")
previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""

    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    if equation == "quit":
        print("Finish")
        run = False
    else:
        equation = regex.sub('[a-zA-Z:,.()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

        print("You typed", previous)

while run:
    performMath()
