with open("andreea_rand1.txt") as inputfile, open('andreea_rand1_clean.txt', 'w') as outfile:
	for line in inputfile:
		if len(line) > 1:
			if "HI" not in line:
				outfile.writelines(line)
			else:
				outfile.writelines('\n')
