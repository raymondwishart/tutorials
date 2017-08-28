import turtle
'''
The turtle module (with a lowercase ’t’) provides a function called Turtle (with an uppercase ’T’) that creates a Turtle object, which we assign to a variable named bob. Printing bob displays something like:
<turtle.Turtle object at 0xb7bfbf4c>
This means that bob refers to an object with type Turtle as defined in module turtle.
mainloop tells the window to wait for the user to do something, although in this case there’s not much for the user to do except close the window.

Once you create a Turtle, you can call a method to move it around the window. A method is similar to a function, but it uses slightly different syntax. For example, to move the turtle forward:

bob.fd(100)
The method, fd, is associated with the turtle object we’re calling bob. Calling a method is like making a request: you are asking bob to move forward.
The argument of fd is a distance in pixels, so the actual size depends on your display.

Other methods you can call on a Turtle are bk to move backward, lt for left turn, and rt right turn. The argument for lt and rt is an angle in degrees.

Also, each Turtle is holding a pen, which is either down or up; if the pen is down, the Turtle leaves a trail when it moves. The methods pu and pd stand for “pen up” and “pen down”.

To draw a right angle, add these lines to the program (after creating bob and before calling mainloop):


for i in range(4):
    print('Hello!')

bob = turtle.Turtle()
print(bob)

bob.fd(100)
bob.lt(90)

bob.fd(100)
bob.lt(90)

bob.fd(100)
bob.lt(90)

bob.fd(100)

turtle.mainloop()
'''

bob = turtle.Turtle()
for i in range(20):
    bob.fd(100)
    bob.lt(90)

    

