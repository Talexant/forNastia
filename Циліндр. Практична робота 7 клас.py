import math
from turtle import *

def calcVolumeOfСylinder(diameter, height):
    return math.pi * diameter ** 2 / 4 * height


def compareVolumeOfCylinders(volume1, volume2):
    result = 'Об’єм {indexOfCylinder} циліндра більший'

    if volume1 > volume2:
        return result.format(indexOfCylinder = 'першого')
    elif volume1 == volume2:
        return 'Об’єми обох циліндрів рівні'
    else:
        return result.format(indexOfCylinder = 'другого')
    
def drawCylinder(cx, cy, diameter, height):
    
    def setPos(cx, cy):
        up()
        setpos(cx, cy)
        down()
    
    def draw(cor1 = -90, cor2 = -45):
        radius = diameter / 2 * 1.375
        seth(cor1)
        circle(radius / 4, 45)
        seth(cor2)
        circle(radius, 90)
        circle(radius / 4, 45)
        

    def drawLowerSemiOval():
        draw()
        
    def drawUpperSemiOval():
        draw(90, 135)


    hideturtle()
    setPos(cx, cy)
    seth(-90)
    forward(height)    
    drawLowerSemiOval()
    seth(90)
    forward(height)
    fillcolor("#CCCCCC")
    pencolor("black")
    begin_fill()
    drawUpperSemiOval()
    drawLowerSemiOval()
    end_fill()
    
def calcScaleToFitScreen(w, h):
    return min(window_width(), window_height()) / 3 / max(w, h)

diameter = float(input('Введіть діаметр першого циліндра: '))
height = float(input('Введіть висоту першого циліндра: '))

volumeOfСylinder1 = calcVolumeOfСylinder(diameter, height)
volumeOfСylinder2 = calcVolumeOfСylinder(height, diameter)

print(f'Об’єм перщого циліндра: {volumeOfСylinder1}')
print(f'Об’єм другого циліндра: {volumeOfСylinder2}')
print(compareVolumeOfCylinders(volumeOfСylinder1, volumeOfСylinder2))

print('Малюю...')

scale = calcScaleToFitScreen(diameter, height)
drawCylinder((-diameter - diameter / 4) * scale, height / 2 * scale ,  diameter * scale, height * scale)
drawCylinder(10, diameter / 2 * scale , height * scale, diameter * scale)

print('Зроблено.')

done()