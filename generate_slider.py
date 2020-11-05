#generate a keyboard with marks for 3 fingers/colours and 6 references 
#run from nodeBox
 
size_x = 800 #size of the keyboard in pixels
size_y= size_x/3.5
size_line= size_x -40
keys = 5 # size of keyboard in keys

size(size_x, size_y)

R = color(255,0,0)
G = color(0,255,0)
B = color(0,0,255)
C = color(0,255,255)
Y = color(255,255,0)

colours = [R, G, B, C, Y]
    
for clr in colours:
    canvas.clear()
    stroke(0)
    strokewidth(2)
    fill(1)
    line(0, size_y/2, size_x, size_y/2, draw=True)
    fill(0.2)
    font("Helvetica", 20)
    text("Not at all", 10, 50)
    text("A lot", 740, 50)
        
        
    for origin in range(0+20, size_x, size_line/keys):
        print(range(0+20, size_line, size_line/keys))
        strokewidth(1)
        line(origin, size_y/1.5, origin, size_y/3)

    newfilename1 =  'slider' + ".jpg"  # alternates are ".tiff", ".jpg", ".eps"
    canvas.save(newfilename1)
          	


        


