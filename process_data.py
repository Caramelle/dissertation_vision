with open("sara_tracking_data.txt") as inputfile, open('sara_data.txt', 'w') as outfile:
	for line in inputfile:
		if len(line) > 1:
			if "HI" not in line:
				outfile.writelines(line)
			else:
				outfile.writelines('\n')
