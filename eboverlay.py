import picamera
import time
import numpy
from PIL import Image, ImageDraw, ImageFont
from time import sleep
from random import randint



with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
    camera.framerate = 24
    camera.start_preview()
    #camera.start_recording('timestamped.h264')
    # Load the arbitrarily sized image
    mepd = Image.open('mepd_blackbg.png')
    mepd.putalpha(128)
    newsize = (100,100)
    mepd = mepd.resize(newsize)
    img = Image.open('blankoverlay2.png')
    img.paste(mepd, (40,470))
    updown = 0
    crossHairPixels = img.load()

        #crossHairPixels[1030, 100] = (51, 255, 51)
        #crossHairPixels[1000, 100] = (255, 0, 0)
        #for i in range (0, 400, 10):
            #crossHairPixels[1100, 100 + i] = (255, 0, 0)
        
    #for x in range (0, 5):
        
        #for i in range (0, 400, 10):
            #crossHairPixels[1000 + x, 100 + i] = (51, 255, 51)
            #crossHairPixels[1000, 100 + x] = (255, 0, 0)
            #crossHairPixels[1040 + x, 100 + i] = (51, 255, 51)
            #crossHairPixels[100 + i, 998] = (51, 255, 51)
        #crossHairPixels[70 - x, 250 + x] = (51, 153, 255)

    #for x in range(100, 400, 20):
    #    for i in range (0, 5):
    #       crossHairPixels[x + i, 700] = (51, 153, 255)

    #left side starts at 1110 and 110 top
    #Verticle Lines
    
    for x in range(110, 550, 80):  #(vertical, lenght, gaps)
        for i in range (0, 40): #lenght of line
           crossHairPixels[1128, x + i] = (51, 255, 51) #Good  

    for x in range(150, 600, 80):  #(vertical, lenght, gaps)
        for i in range (0, 40): #lenght of line
           crossHairPixels[1125, x + i] = (51, 255, 51) #Good  

    for x in range(120, 600, 20):  #(vertical, lenght, gaps)
        for i in range (0, 10): #lenght of line
           crossHairPixels[1142, x + i] = (51, 255, 51) #Good Vertical
        
           crossHairPixels[1108, x + i] = (51, 255, 51)
    for x in range(110, 600, 70):
        for i in range (0, 50):
           crossHairPixels[1115, x + i] = (51, 255, 51)
           crossHairPixels[1120, x + i + 20] = (51, 255, 51)
    
    
    for x in range(110, 600, 20):
        for i in range (0, 10):
           crossHairPixels[1148, x + i] = (51, 255, 51) #Good
           crossHairPixels[1102, x + i] = (51, 255, 51)
    for x in range(110, 600, 40):
        for i in range (0, 20):        
           crossHairPixels[1132, x + i] = (51, 255, 51) #Good
           #crossHairPixels[1025, x + i + 10] = (51, 255, 51)
    for x in range(130, 600, 40):
        for i in range (0, 20):        
           crossHairPixels[1135, x + i] = (51, 255, 0) #Good
    #for x in range (195, 1080, 10):
    #    for i in range (0, 5):
    #       crossHairPixels[x + i, 460] = (51, 153, 255)
       #crossHairPixels[x, 200] = (51, 153, 255)

    #Horizontal Lines
    for x in range(110, 600, 10):
        for i in range(0, 10):
           crossHairPixels[1140 + i, x] = (51, 255, 51) #Good
           crossHairPixels[1100 + i, x] = (51, 255, 51) #Good
    for x in range(110, 600, 20):  
        for i in range(0, 10):
           
           crossHairPixels[1130 + i, x] = (51, 255, 51) #Good
    for x in range(110, 600, 30):
        for i in range(0, 20):
           #crossHairPixels[1055 + i, x] = (51, 255, 51) #Good
           crossHairPixels[1105 + i, x] = (51, 255, 51)            
    for x in range(110, 600, 40):
        for i in range(0, 10):
           crossHairPixels[1125 + i, x] = (51, 255, 51) #Good

    #Single Horizontal Lines
    #for x in range (1010, 1120):
    #   crossHairPixels[x, 170] = (51, 153, 255)       
    #   crossHairPixels[x, 370] = (51, 153, 255)      
           
           
    #Blue Crosshairs
    #horizontal line
    for x in range (190, 1060):
       crossHairPixels[x, 360] = (51, 153, 255)
       #crossHairPixels[x, 200] = (51, 153, 255)
    #vertical line
    for x in range(75, 650): 
       crossHairPixels[640, x] = (51, 153, 255)
    
    
    
    
    # Create an image padded to the required size with
    # mode 'RGB'
    pad = Image.new('RGBA', (
        ((img.size[0] + 31) // 32) * 32,
        ((img.size[1] + 15) // 16) * 16,
        ))

    # Paste the original image into the padded one
    pad.paste(img, (0, 0))
    
    
    text = time.strftime('%H:%M:%S', time.gmtime())
    
    pada = pad.copy()
    #draw = ImageDraw.Draw(pada)
    #draw.font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/Aurebesh.ttf", 20)
    #draw.text((600, 600), text, (51, 153, 255))
    
    
    # Add the overlay with the padded image as the source,
    # but the original image's dimensions
    o = camera.add_overlay(pada.tobytes(), size=img.size)
    # By default, the overlay is in layer 0, beneath the
    # preview (which defaults to layer 2). Here we make
    # the new overlay semi-transparent, then move it above
    # the preview
    #o.alpha = 128
    o.layer = 3
    sleep(1)
    #sleep(4)
    # Wait indefinitely until the user terminates the script
    while True:
       
        #try:
        while True:
             texttime = time.strftime('%H:%M:%S', time.localtime())
             textid = 'TK-3195'
             textimp = '}'
             img = pad.copy()
             draw = ImageDraw.Draw(img)
             draw.font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/Aurebesh.ttf", 20)
             fnt = ImageFont.truetype("/usr/share/fonts/truetype/freefont/Aurebesh.ttf", 100)
             #draw.text((600, 600), text, (255, 255, 255))
             #draw.text((10, 100), text, (0, 255, 255))
             #draw.text((10, 200), text, (255, 0, 255))
             draw.text((30, 440), texttime, (255, 255, 0))
             draw.textsize(textimp)
             draw.text((50, 100), textimp, font=fnt, fill=(255, 255, 0))
             draw.text((30, 580), textid, (255, 255, 0))
             #draw.text((200, 10), text, (255, 255, 255))
             #draw.text((300, 100), text, (0, 255, 255))
             #draw.text((400, 200), text, (255, 0, 255))
             #draw.text((500, 300), text, (255, 255, 0))
    #bracket
             crossHairPixels = img.load()
             #updown = randint(0, 400)
             updown = updown + 1
             if updown > 450:
                 updown = 0
             else:
                 updown = updown + 1
             
             for x in range (0, 20):
            
                crossHairPixels[1070 + x, 140 + x + updown] = (255, 255, 255)
                crossHairPixels[1070 + x, 140 - x + updown] = (255, 255, 255)
    
            #short
             for x in range (0, 5):
                crossHairPixels[1090 + x, 115 - x + updown] = (255, 255, 255)
                crossHairPixels[1090 + x, 165 + x + updown] = (255, 255, 255)

                crossHairPixels[1155 + x, 110 + x + updown] = (255, 255, 255)
                crossHairPixels[1160 - x, 165 + x + updown] = (255, 255, 255)

             for x in range (0, 50):    
                crossHairPixels[1090, 115 + x + updown] = (255, 255, 255)
                crossHairPixels[1160, 115 + x + updown] = (255, 255, 255)

#Right Signal display
    #Verticle Lines
             ransignal = randint(0, 10)
             for x in range(110, 550, 80):  #(vertical, lenght, gaps)
                 for i in range (0, 40): #lenght of line
                   crossHairPixels[1128, x + i] = (51, 255, 51) #Good  

             for x in range(150, 600, 80):  #(vertical, lenght, gaps)
                 for i in range (0, 40): #lenght of line
                   crossHairPixels[1125, x + i] = (51, 255, 51) #Good  

             for x in range(120, 600, 20):  #(vertical, lenght, gaps)
                 for i in range (0, 10): #lenght of line
                   crossHairPixels[1142, x + i] = (51, 255, 51) #Good Vertical
        
                   crossHairPixels[1108, x + i] = (51, 255, 51)

             for x in range(110, 600, 70):
                 for i in range (0, 50):
                   crossHairPixels[1115 + ransignal, x + i] = (51, 255, 51)
                   crossHairPixels[1120, x + i + 20] = (51, 255, 51)
    
    
             for x in range(110, 600, 20):
                 for i in range (0, 10):
                   crossHairPixels[1148, x + i] = (51, 255, 51) #Good
                   crossHairPixels[1102, x + i] = (51, 255, 51)
             for x in range(110, 600, 40):
                 for i in range (0, 20):        
                   crossHairPixels[1132 + ransignal, x + i ] = (51, 255, 51) #Good
           #crossHairPixels[1025, x + i + 10] = (51, 255, 51)
             for x in range(130, 600, 40):
                 for i in range (0, 20):        
                   crossHairPixels[1135, x + i] = (51, 255, 0) #Good
    #for x in range (195, 1080, 10):
    #    for i in range (0, 5):
    #       crossHairPixels[x + i, 460] = (51, 153, 255)
       #crossHairPixels[x, 200] = (51, 153, 255)

    #Horizontal Lines
             for x in range(110, 600, 10):
                 for i in range(0, 10):
                   crossHairPixels[1140 + i, x] = (51, 255, 51) #Good
                   crossHairPixels[1100 + i, x + ransignal] = (51, 255, 51) #Good
             for x in range(110, 600, 20):  
                 for i in range(0, 10):
           
                   crossHairPixels[1130 + i, x + ransignal] = (51, 255, 51) #Good
             for x in range(110, 600, 30):
                 for i in range(0, 20):
           #crossHairPixels[1055 + i, x] = (51, 255, 51) #Good
                   crossHairPixels[1105 + i, x] = (51, 255, 51)            
             for x in range(110, 600, 40):
                 for i in range(0, 10):
                   crossHairPixels[1125 + i, x + ransignal] = (51, 255, 51) #Good
             #sleep(1)


             o.update(img.tobytes())
             #camera.wait_recording(0.9)
    sleep(1)
        #finally:
          #camera.remove_overlay(o)
          #camera.stop_recording()
