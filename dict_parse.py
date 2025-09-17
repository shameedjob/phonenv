def process_dictionary(input_file, append=None, print_dict=False, delete_substring=None, clear_file=False):
	"""
	Process a dictionary of words from an input file.
	
	Parameters:
	- input_file: str, path to the input file containing words
	- append: str to append to existing dictionary file or None
	- print_dict: bool, whether to print the dictionary to console
	- delete_substring: str or None, substring to delete words containing it from the dictionary
	- clear_file: bool, whether to clear the existing dictionary file before processing
	"""
	print(f"Processing dictionary from '{input_file}'")
	# Read words from the input file
	with open(input_file, 'r') as f:
		words = set(line.strip() for line in f if line.strip())
	
	if clear_file:
		words = set()
	# If append is provided add word to the set
	if append:
		words.add(append)
		
	# If delete_substring is provided, filter out words containing it
	if delete_substring:
		words = {word for word in words if delete_substring not in word}
	

	
	# Write the updated dictionary back to the append_file or a new file
	with open(input_file, 'w') as f:
		for word in sorted(words):
			f.write(f"{word}\n")
	
	# Print the dictionary if requested
	if print_dict:
		for word in sorted(words):
			print(word)