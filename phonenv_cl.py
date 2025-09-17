import argparse
import environment_analyzer
import dict_parse

parser = argparse.ArgumentParser(description="Derive environement details for a specific phonemic character or substring.")
subparsers = parser.add_subparsers(dest='command', help='sub commands')
analyze_parser = subparsers.add_parser('analyze', help='Analyze environment variable')
analyze_parser.add_argument('character', type=str, help='Character or substring to analyze')
analyze_parser.add_argument('--file', type=str, help='input file', default='data/input.txt')

dict_parser = subparsers.add_parser('dict', help='Generate dictionary of words')
dict_parser.add_argument('--file', type=str, help='input file', default='data/input.txt')
dict_parser.add_argument('-a', '--append', type=str, help='append to existing dictionary file', default=None)
dict_parser.add_argument('-p', '--print', action='store_true', help='print the dictionary to console')
dict_parser.add_argument('-d', '--delete', type=str, help='delete words containing this substring from the dictionary', default=None)

special_parser = subparsers.add_parser('add_special', help='Add a special character to special_characters.txt')
special_parser.add_argument('character', type=str, help='Special character to add')
special_parser.add_argument('-d', '--delete', action='store_true', help='Delete the character from special_characters.txt')
special_parser.add_argument('-e', '--erase', action='store_true', help='Clear the file before adding the character')
args = parser.parse_args()

if args.command is None:
	parser.print_help()
	exit(1)

if args.command == 'dict':
	dict_parse.process_dictionary(input_file=args.file, append=args.append, print_dict=args.print, delete_substring=args.delete)
elif args.command == 'analyze':
	environment_analyzer.analyze_character_print(character=args.character, file=args.file)
elif args.command == 'add_special':
	environment_analyzer.add_special_character(character=args.character, delete=args.delete, erase=args.erase)