from PIL import Area, ImageOps
import pyautogui
import time
import numpy as np
 
class coordinates():

	play_again =(964, 550)

	dinosaur = (149, 633 )

def space():

	pyautogui.keyUp('down')

	pyautogui.keyDown('space')
	
	time.sleep(0.1 - speed * 0.01)

	pyautogui.keyUp('space')

	pyautogui.keyDown('down')

def Area():
 
	box = (coordinates.dinosaur[0]+350, coordinates.dinosaur[1],
		coordinates.dinosaur[0]+450, coordinates.dinosaur[1]+2)  
 
	image = Area.grab(box)
 
	grayImage = ImageOps.grayscale(image)
 
	a = np.array(grayImage.getcolors()) 
  
	print(a.sum())
	return a.sum()

   
def retry():
    pyautogui.click(coordinates.replaybutton)
    pyautogui.keyDown('down')
    
speed = 1
    
retry()
while True:
  
	if(Area()!= 455):
		
		space() 

	speed = speed + 1
	time.sleep(speed * time)