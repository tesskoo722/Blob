import Myro
from Myro import *
from Graphics import *
from random import *

#init("sim")

width = 500
height = 500
sim = Simulation("Maze World", width, height, Color("gray"))

#outside walls
sim.addWall((10, 10), (490, 20), Color("black"))
sim.addWall((10, 10), (20, 490), Color("black"))
sim.addWall((480, 10), (490, 490), Color("black"))
sim.addWall((10, 480), (490, 490), Color("black"))

#blue spot
poly = Circle((50, 50), 45)
poly.bodyType = "static"
poly.color = Color("blue")
poly.outline = Color("black")
sim.addShape(poly)

#red spot
poly = Circle((450, 50), 45)
poly.bodyType = "static"
poly.color = Color("red")
poly.outline = Color("black")
sim.addShape(poly)

#green spot
poly = Circle((50, 450), 45)
poly.bodyType = "static"
poly.color = Color("green")
poly.outline = Color("black")
sim.addShape(poly)

#yellow spot
poly = Circle((450, 450), 45)
poly.bodyType = "static"
poly.color = Color("yellow")
poly.outline = Color("black")
sim.addShape(poly)

#begin simulation and sets robot's position
makeRobot("SimScribbler", sim)
sim.setPose(0, width/2, height/2, 0)

sim.setup()

# 1-RED
# 2-GREEN
# 3-BLUE
# 4-YELLOW

#The following is a helper function 
#Inputs: A picture and a color represented by the list above
#Returns the average x location of the color in the picture or -1 if the robot has found the color spot

def findColorSpot(picture, color):
    xPixelSum = 0
    totalPixelNum = 0
    averageXPixel = 0

    show(picture)

    for pixel in getPixels(picture):
        if(color == 1 and getRed(pixel) > 150 and getGreen(pixel) < 50 and getBlue(pixel) < 50):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 2 and getRed(pixel) < 50 and getGreen(pixel) > 100 and getBlue(pixel) < 50):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 3 and getRed(pixel) < 50 and getGreen(pixel) < 50  and getBlue(pixel) > 150):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 4 and getRed(pixel) > 200 and getGreen(pixel) > 150 and getBlue(pixel) < 50):
            
            xPixelSum += getX(pixel)
            totalPixelNum += 1
    if(totalPixelNum != 0):
        averageXPixel = xPixelSum/totalPixelNum

    #Handles the case where robot has found the spot if it is near it
    #If necessary adjust the value
    if(totalPixelNum/(getWidth(picture)*getHeight(picture)) > 0.21):
        averageXPixel = -1

    return averageXPixel


# Use the following integers for colors:
# 1-RED
# 2-GREEN
# 3-BLUE
# 4-YELLOW

######################Code Starts Here##################################

y=0
answer=askQuestion("Which blob would you like to find, or would you prefer a random one?",["Red", "Green", "Blue", "Yellow", "Random"])
if (answer=="Red"):
    y=1
if (answer=="Green"):
    y=2
if (answer=="Blue"):
    y=3
if (answer=="Yellow"):
    y=4
if (answer=="Random"):
    y=randrange(1,4)

#FIND THE BLOB

turnBy(randrange(30,60))   
pic=takePicture()
show(pic)  

x=findColorSpot(pic,y)

while (x==0):
    turnBy(randrange(30,60))
    pic=takePicture()
    show(pic)
    x=findColorSpot(pic,y)
#WE NEED SOME SORT OF UNTIL
       
   
while (0 < x < 90):
    turnBy(10)
    pic=takePicture()
    show(pic)
    x=findColorSpot(pic,y)
    
while (150 < x < 256):
    turnBy(350)
    pic=takePicture()
    show(pic)
    x=findColorSpot(pic,y)
    
if (90 < x <150):
    forward(2,3)
    pic=takePicture()
    x=findColorSpot(pic,y)
    if (x ==-1):
        print ("You found the blob!")
    
