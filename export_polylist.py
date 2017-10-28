import binascii

fin = open('test_1.bmp', 'rb')
hex = binascii.hexlify(fin.read())

start_pixel_data = int(hex[20:22])
pixel_data = (hex[(32 * int(str(start_pixel_data)[0:1])) + int(str(start_pixel_data)[1:2]) * 2:]).decode('utf-8')
image_width = int(hex[36:38])
image_height = int(hex[44:46])

pixels = [[0] * image_height for _ in range(image_width)]
current_address = 2 + (32 * int(str(start_pixel_data)[0:1])) + int(str(start_pixel_data)[1:2]) * 2

padding_amount = 0
if (image_width % 4 != 0):
	padding_amount = 4 - (image_width * 3 % 4)

for y in range(image_height):
	for x in range(image_width):
		if (int(hex[current_address:current_address + 2], 16) == 0 or
			int(hex[current_address + 2:current_address + 4], 16) == 0 or
			int(hex[current_address + 4:current_address + 6], 16) == 0):
			pixels[image_height - y - 1][x] = 1
		current_address += 6
	current_address += padding_amount

print(pixels)