import binascii

fin = open('test_2.bmp', 'rb')
hex = binascii.hexlify(fin.read())

start_pixel_data = int(hex[20:22])
pixel_data = (hex[(32 * int(str(start_pixel_data)[0:1])) + int(str(start_pixel_data)[1:2]) * 2:]).decode('utf-8')
image_width = int(hex[36:38])
image_height = int(hex[44:46])

pixels = [[None] * image_width for _ in range(image_height)]