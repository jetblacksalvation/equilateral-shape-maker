import turtle
walk = turtle.Turtle()

def equilateral(radius:int, vertices:int):
    #create a new turtle
    if vertices <3 :
        print("has to be bigger/equal to 3")
        return
    temp_tert = turtle.Turtle()
    angle = 180-(((180*(vertices-3))+180)/vertices)#find angle given vertices 
    if angle == 60:
        print("is ")
    for i in range(vertices):
        temp_tert.forward(radius)
        temp_tert.right(angle)
        

    return






equilateral(10,25)
     
turtle.done()