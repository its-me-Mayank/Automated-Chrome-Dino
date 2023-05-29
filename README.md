Hello!

I have automated the chrome dinosaur game. It works fine and gets a score of around 700 consistently. After that point,
the night comes and the code 'fails' because it only detects black objects. 

                                            What I did to make this work

{i} I wrote a program that gives me the coordinates of points on an image (I have included the exact screenshot of the
    dino game I used to make a note of the coordinates). 
    
    ***You can potentially use the same code format to optimise the game to run at resolutions other than 1920 x 1080!***

{ii} Wrote the main program. Essentially, it defines a box in front of the dinosaur which takes images in grayscale.  So,
    it jumps when it 'sees' a black object.
