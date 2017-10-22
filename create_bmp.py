import binascii

fout = open('output_image.bmp', 'wb')
fileLine = []

#BMP Header
fileLine.append('42 4D')          #ID field
fileLine.append('46 00 00 00')    #size of the BMP file
fileLine.append('00 00')          #application specific
fileLine.append('00 00')          #application specific
fileLine.append('36 00 00 00')    #offset where the pixel array can be found

#DIB Header
fileLine.append('28 00 00 00')    #number of bytes in DIB header
fileLine.append('02 00 00 00')    #width of the bitmap in pixels
fileLine.append('02 00 00 00')    #height of the bitmap in pixels
fileLine.append('01 00')          #number of color planes
fileLine.append('18 00')          #number of bits per pixel
fileLine.append('00 00 00 00')    #compression Method
fileLine.append('10 00 00 00')    #size of the raw bitmap data
fileLine.append('13 0B 00 00')    #print resolution of image
fileLine.append('13 0B 00 00')    
fileLine.append('00 00 00 00')    #number of colors in the palette
fileLine.append('00 00 00 00')    #important colors

#Bitmap Data
fileLine.append('00 00 FF')       #Pixel (0, 1)
fileLine.append('FF FF FF')		  #Pixel (1, 1)
fileLine.append('00 00')          #Padding for 4 byte alignment
fileLine.append('FF 00 00')       #Pixel (0, 0)
fileLine.append('00 FF 00')       #Pixel (1, 0)
fileLine.append('00 00')          #Padding for 4 byte alignment

for line in fileLine:
    fout.write(binascii.unhexlify(''.join(line.split())))