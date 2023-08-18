def strchr(string, char)
	for i in range(len(string)):
		if string[i] == char:
			return string[i:]
		return None