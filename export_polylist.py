import binascii

def vertex_to_string(vertex):
	temp_string = ''
	if (len(str(hex(vertex[0]))[2:4]) == 1):
		temp_string += '0'
	temp_string += str(hex(vertex[0]))[2:4]
	temp_string += ' '
	if (len(str(hex(vertex[1]))[2:4]) == 1):
		temp_string += '0'
	temp_string += str(hex(vertex[1]))[2:4]

	return temp_string

fin = open('test_images/board_3.bmp', 'rb')
file_hex = binascii.hexlify(fin.read())
fin.close()

start_pixel_data = int(file_hex[20:22])
pixel_data = (file_hex[(32 * int(str(start_pixel_data)[0:1])) + int(str(start_pixel_data)[1:2]) * 2:]).decode('utf-8')
image_width = int(file_hex[36:38], 16)
image_height = int(file_hex[44:46], 16)

pixels = [[0] * image_width for _ in range(image_height)]
current_address = (32 * int(str(start_pixel_data)[0:1])) + int(str(start_pixel_data)[1:2]) * 2

padding_amount = 0
if (image_width % 4 != 0):
	padding_amount = (4 - (image_width * 3 % 4)) * 2

for y in range(image_height):
	for x in range(image_width):
		if (int(file_hex[current_address:current_address + 2], 16) == 0 or
			int(file_hex[current_address + 2:current_address + 4], 16) == 0 or
			int(file_hex[current_address + 4:current_address + 6], 16) == 0):
			pixels[image_height - y - 1][x] = 1
		current_address += 6
	current_address += padding_amount

vertices = []
coordinate = [-1, -1]
direction = 'right'
complete_circuit = False

for y in range(len(pixels)):
	for x in range(len(pixels[0])):
		if (pixels[y][x] != 0):
			coordinate[0] = x
			coordinate[1] = y
			break
	if (coordinate[0] != -1):
		break

vertices.append(coordinate)

short_direction = False
while (complete_circuit == False):
	if (direction == 'left' and coordinate[0] > 0):
		if (pixels[coordinate[1]][coordinate[0] - 1] != 0):
			coordinate = [coordinate[0] - 1, coordinate[1]]
			short_direction = True
	elif (direction == 'right' and coordinate[0] < len(pixels[0]) - 1):
		if (pixels[coordinate[1]][coordinate[0] + 1] != 0):
			coordinate = [coordinate[0] + 1, coordinate[1]]
			short_direction = True
	elif (direction == 'up' and coordinate[1] > 0):
		if (pixels[coordinate[1] - 1][coordinate[0]] != 0):
			coordinate = [coordinate[0], coordinate[1] - 1]
			short_direction = True
	elif (direction == 'down' and coordinate[1] < len(pixels) - 1):
		if (pixels[coordinate[1] + 1][coordinate[0]] != 0):
			coordinate = [coordinate[0], coordinate[1] + 1]
			short_direction = True

	if (short_direction == False):
		if (direction == 'left'):
			if (pixels[coordinate[1] - 1][coordinate[0]] != 0 and coordinate[1] > 0): 
				vertices.append(coordinate)
				direction = 'up'
			elif (pixels[coordinate[1] + 1][coordinate[0]] != 0 and coordinate[1] < len(pixels[0]) - 1): 
				vertices.append(coordinate)
				direction = 'down'
		elif (direction == 'right'):
			if (pixels[coordinate[1] - 1][coordinate[0]] != 0 and coordinate[1] > 0): 
				vertices.append(coordinate)
				direction = 'up'
			elif (pixels[coordinate[1] + 1][coordinate[0]] != 0 and coordinate[1] < len(pixels) - 1): 
				vertices.append(coordinate)
				direction = 'down'
		elif (direction == 'up'):
			if (pixels[coordinate[1]][coordinate[0] - 1] != 0 and coordinate[0] > 0): 
				vertices.append(coordinate)
				direction = 'left'
			elif (pixels[coordinate[1]][coordinate[0] + 1] != 0 and coordinate[0] < len(pixels[0]) - 1): 
				vertices.append(coordinate)
				direction = 'right'
		elif (direction == 'down'):
			if (pixels[coordinate[1]][coordinate[0] - 1] != 0 and coordinate[0] > 0): 
				vertices.append(coordinate)
				direction = 'left'
			elif (pixels[coordinate[1]][coordinate[0] + 1] != 0 and coordinate[0] < len(pixels[0]) - 1): 
				vertices.append(coordinate)
				direction = 'right'

	short_direction = False

	if (coordinate == vertices[0]):
		complete_circuit = True

# fout = open('polylist.hex', 'wb')

# for vertex in vertices:
#     fout.write(binascii.unhexlify(''.join(vertex_to_string(vertex).split())))

# fout.close()

fout = open('polylist.txt', 'w')

for vertex in vertices:
	fout.write(str(vertex[0]) + ' ' + str(vertex[1]) + ' ')

fout.close()