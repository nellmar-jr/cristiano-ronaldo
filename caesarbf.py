msg = "ZFBI. J'N QSFUUZ TVSF NZ DBU XPVME FBU NF."
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for key in range(len(letters)):
	translated = ''
	for let in msg:
		if let in letters:
			num = letters.find(let)
			num = num - key
			if num < 0:
				num += 26
			translated += letters[num]
		else:
			translated += let
	
	print(f"The key is: {key} and the message is: {translated} ")
