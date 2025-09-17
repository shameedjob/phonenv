def analyze_character(character, file="input.txt"):
	"""
	Analyze the environments of a specific character or substring in a text file.
	Display the environments and the words in which they occur.
	Parameters:
	- character: str, the character or substring to analyze
	- file: str, path to the input text file

	returns: dict, mapping environments to lists of words
	"""
	resources = []
	special_characters = []
	with open('data/special_characters.txt', 'r') as f:
		for line in f:
			special_characters.append(line.strip())
			
	with open(file, 'r') as file:
		for line in file:
			resources.append(line.strip())
	environments = {}
	for r in resources:
		if character in special_characters:
			character = f'({character})'
		for f in special_characters:
			r = r.replace(f, f'({f})')
		test_r = r
		while character in test_r:
			index = test_r.find(character)
			if index > test_r.find('(') and index < test_r.find(')'):
				test_r = test_r[index+len(character):]
				continue
			left = test_r[index-1] if index > 0 else "#"
			if left == ')':
				left_index = test_r.rfind('(', 0, index)
				left = test_r[left_index:index]
			right = test_r[index+len(character)] if index+len(character) < len(test_r) else "#"
			if right == '(':
				right_index = test_r.find(')', index)
				right = test_r[index+len(character):right_index+1]
			env = left+'__'+right
			if not env in environments:
				environments[env] = [r.replace(test_r, test_r.replace(character, f'[{character}]', 1), 1)]
			else: environments[env].append(r.replace(test_r, test_r.replace(character, f'[{character}]', 1), 1))
			test_r = test_r[index+len(character):]
	return environments

def analyze_character_print(character, file="input.txt"):
	environments = analyze_character(character, file)
	
	if len(environments) == 0:
		print(f"No occurrences of '{character}' found in '{file}'")
	else:
		print(f"================================")
		print(f"Local Env\t(Count)\t Words")
		print(f"================================")
		for env in environments:
			print(f"{env}\t\t({len(environments[env])})\t {', '.join(environments[env])}")


def add_special_character(character, delete=False, erase=False):
	"""
	Add a special character to the special_characters.txt file if it doesn't already exist.
	Parameters:
	- character: str, the special character to add
	- remove_character: bool, if True, remove the character from the file
	- erase_existing: bool, if True, clear the file before adding the new character
	"""
	with open('data/special_characters.txt', 'r') as f:
		special_characters = [line.strip() for line in f]

		if delete:
			special_characters = []
			with open('data/special_characters.txt', 'w') as f:
				f.write("")
		if erase:
			if character in special_characters:
				special_characters.remove(character)
				with open('data/special_characters.txt', 'w') as f:
					for char in special_characters:
						f.write(f"{char}\n")
				print(f"Removed '{character}' from special_characters.txt")
			else:
				print(f"'{character}' not found in special_characters.txt")
			return
		if character not in special_characters:
			with open('data/special_characters.txt', 'a') as f:
				f.write(f"{character}\n")
			print(f"Added '{character}' to special_characters.txt")
		else:
			print(f"'{character}' already exists in special_characters.txt")