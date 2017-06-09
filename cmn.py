def foo(words, key):
	count = len(words) // key
	if len(words) % key != 0:
		count += 1
	k = []
	for x in range(0, key):
		k.append(words[x::key])
	return ''.join(k)
	
words = input("> ")
key = int(input("> "))

print(foo(words, key))