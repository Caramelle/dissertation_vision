with open("track.txt") as inputfile, open('tracking_data.txt', 'w') as outfile:
	for line in inputfile:
		if len(line) > 1:
			if "HI" not in line:
				elems = line.split(' ')
				coord = elems[1][1:]
				print(coord)
				elems[1] = 'x ' + coord
				line = ' '.join(elems)
				outfile.writelines(line)
			else:
				outfile.writelines('\n')
