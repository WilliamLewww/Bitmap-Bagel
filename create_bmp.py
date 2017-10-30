import binascii

fout = open('output_image.bmp', 'wb')
file_line = []

#BMP Header
file_line.append('42 4D')          #ID field
file_line.append('46 00 00 00')    #size of the BMP file
file_line.append('00 00')          #application specific
file_line.append('00 00')          #application specific
file_line.append('36 00 00 00')    #offset where the pixel array can be found

#DIB Header
file_line.append('28 00 00 00')    #number of bytes in DIB header
file_line.append('02 00 00 00')    #width of the bitmap in pixels
file_line.append('02 00 00 00')    #height of the bitmap in pixels
file_line.append('01 00')          #number of color planes
file_line.append('18 00')          #number of bits per pixel
file_line.append('00 00 00 00')    #compression Method
file_line.append('10 00 00 00')    #size of the raw bitmap data
file_line.append('13 0B 00 00')    #print resolution of image
file_line.append('13 0B 00 00')    
file_line.append('00 00 00 00')    #number of colors in the palette
file_line.append('00 00 00 00')    #important colors

#Bitmap Data
file_line.append('00 00 FF')       #Pixel (0, 1)
file_line.append('FF FF FF')		  #Pixel (1, 1)
file_line.append('00 00')          #Padding for 4 byte alignment
file_line.append('FF 00 00')       #Pixel (0, 0)
file_line.append('00 FF 00')       #Pixel (1, 0)
file_line.append('00 00')          #Padding for 4 byte alignment

for line in file_line:
    fout.write(binascii.unhexlify(''.join(line.split())))

fout.close()