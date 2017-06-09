key = int(input("Key: "))

choice = input("What do you want to do? ")

text = input("Type the string to cipher/decipher: ")

alp = list("abcdefghijklmnñopqrstuvwxyz")

def cipher(key, alp, text):
	n = 0
	dcph = list(text)
	cph = []
	
	while key > 26:
		key -= 26
		
	for i in dcph:
		x = dcph[n]
		if x == ' ':
			cph.append(x)
			n += 1
			y = 0
			z = 0
			continue
		y = alp.index(x)
		y += key
		if y > 26:
			y -= 27
		z = alp[y]
		cph.append(z)
		n += 1
		y = 0
		z = 0
		
	print(''.join(cph))

def decipher(key, alp, text):
	n = 0
	cph = list(text)
	dcph = []
	
	while key > 26:
		key -= 26
	
	for i in cph:
		x = cph[n]
		if x == ' ':
			dcph.append(x)
			n += 1
			y = 0
			z = 0
			continue
		y = alp.index(x)
		y -= key
		if y < 0:
			y += 27
		z = alp[y]
		dcph.append(z)
		n += 1
		y = 0
		z = 0
		
	print(''.join(dcph))
	
	
key, choice, text

if choice == "cipher":
	cipher(key, alp, text)
if choice == "decipher":
	decipher(key, alp, text)