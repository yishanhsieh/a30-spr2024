import turtle

 # other function definitions followed by the main function definition
def main():
    # The main code of the program goes here
    filename = input("Please enter drawing filename: ")
    
    #create a Turtle Graphics to draw in
    t = turtle.Turtle()

    #the screen is used in the end of the program
    screen = t.getscreen()
    
    # r for reading, w for writing
    file = open(filename, "r")  

    for line in file:
        text = line.strip()

        commandList = text.split(",")

        command = commandList[0]

        if command == "goto":
            x = float(commandList[1])
            y = float(commandList[2])
            width = float(commandList[3])
            color = commandList[4].strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x,y)
        elif command == "circle":
            radius = float(commandList[1])
            width = float(commandList[2])
            color = commandList[3].strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command == "beginfill":
            color = commandList[1].strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command == "endfill":
            t.end_fill()
        elif command == "penup":
            t.penup()
        elif command == "pendown":
            t.pendown()
        else:
            print("Unknown command found in file:",command)

    file.close()
    t.ht()

    screen.exitonclick()
    print("Program Execution Completed.")



# this code calls the main function to get everything started. The condition in this
# if statement evaluates to True when the module is executed by the interpreter, but
# not when it is imported into another module.
if __name__ == "__main__":
    main()
