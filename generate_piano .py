#generate a keyboard with marks for 3 fingers/colours and 6 references 
#run from nodeBox
 
size_x = 640 #size of the keyboard in pixels
size_y= size_x/3.5
keys = 4 # size of keyboard in keys

size(size_x, size_y)
circle_size = size_x/15


R = color(255,0,0)
G = color(0,255,0)
B = color(0,0,255)
C = color(0,255,255)
Y = color(255,255,0)

colours = [R, G, B, C, Y]
referencesdx = [2,3,4,7,8]
referencessx = [2,3,4,7,8,9]
    
for finger in range(0,size_x, size_x/keys):
    print finger
    
    for clr in colours:
        canvas.clear()
        stroke(0)
        strokewidth(2)
        fill(1)
        rect(0,0,size_x, size_y)

        for origin in range(0,size_x, size_x/keys):
            strokewidth(1)
            line(origin, 0, origin, size_y)
        
        for ref in referencesdx:
            fill(0)
          #  rect((ref-1)*size_x/keys+size_x/54, size_y-20, size_x/(keys*2), 5) 
            rect((ref-1)*size_x/keys, size_y-1350, size_x/(keys), (size_y)) ####larghezza back keys
 
        for r in referencessx:
            fill(0)
          #  rect((ref-1)*size_x/keys+size_x/54, size_y-20, size_x/(keys*2), 5) 
            rect((r-1)*size_x/keys-15, size_y-350, size_x/(keys*5), (size_y+50)) ####altezza back keys
 
        newfilename1 =  'K0F0' + ".jpg"  # alternates are ".tiff", ".jpg", ".eps"
        canvas.save(newfilename1)
        
        strokewidth(1)
        stroke(clr)
        fill(clr)
        oval(finger+size_x/(keys*2)  - circle_size/2 , size_y/1.5, circle_size, circle_size)
        
        
       # newfilename =  'K' + str((finger/(size_x/keys))+1) + 'F' + str(colours.index(clr)+1) + ".jpg"  # alternates are ".tiff", ".jpg", ".eps"
       # canvas.save(newfilename)


